#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse
import requests
import re
import socket
import json
import datetime

# Set up the API endpoint and API key
API_URL = 'https://api.criminalip.io/v1/feature/ip/malicious-info'
API_KEY = ''
SAVE_FILE = '/tmp/criminalip_cachefile.txt'
ZABBIX_HOSTNAME = socket.gethostname()

# Define a function to check if an IP address is valid
def is_valid_ip(ip):
    pattern = '^([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.' \
              '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.' \
              '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.' \
              '([01]?\\d\\d?|2[0-4]\\d|25[0-5])$'
    return bool(re.match(pattern, ip))

# Define a function to get data for a given IP address
def get_ip_data(ip):
    if not is_valid_ip(ip):
        raise ValueError("Invalid IP address")
    headers = {'x-api-key': API_KEY}
    params = {
        'ip': ip,
    }
    payload = {}
    response = requests.request("GET", API_URL, headers=headers, params=params, data=payload)
    if response.status_code != 200:
        raise ValueError("Invalid API response")
    try:
        data = json.loads(response.text)
    except ValueError:
        raise ValueError("Invalid JSON response")
    ids_count = data.get('ids', {}).get('count', 0)
    vulnerability_count = data.get('vulnerability', {}).get('count', 0)
    webcam_count = data.get('webcam', {}).get('count', 0)
    scanning_record_count = data.get('scanning_record', {}).get('count', 0)
    current_opened_port_value = data.get('current_opened_port', {}).get('data', 0)
    return ids_count, vulnerability_count, webcam_count, scanning_record_count, current_opened_port_value

# Main function to parse command line arguments and call get_ip_data function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get data for an IP address')
    parser.add_argument('ip_address', help='IP address to check')
    args = parser.parse_args()
    try:
        ids_count, vulnerability_count, webcam_count, scanning_record_count, current_opened_port_value = get_ip_data(args.ip_address)
    except ValueError as e:
        print("Error: {0}".format(str(e)))
    else:
        # Prepare data for saving
        now = datetime.datetime.now()
        data = {
            "datetime": now.isoformat(),
            "ip": args.ip_address,
            "ids_count": ids_count,
            "vulnerability_count": vulnerability_count,
            "webcam_count": webcam_count,
            "scanning_record_count": scanning_record_count,
            "current_opened_port_value": current_opened_port_value
        }
        # Save data to file
        with open(SAVE_FILE, 'w') as f:
            f.write(json.dumps(data) + '\n')
        print("Data saved to file: {0}".format(SAVE_FILE))
