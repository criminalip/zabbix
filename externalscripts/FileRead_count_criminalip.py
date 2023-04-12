#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pyzabbix import ZabbixMetric, ZabbixSender
import json
import socket
import sys

ZABBIX_SERVER = ''
ZABBIX_PORT = 10051
ZABBIX_HOSTNAME = socket.gethostname()

if sys.version_info.major == 2:
    fileNotFoundError = IOError
else:
    fileNotFoundError = FileNotFoundError

if __name__ == '__main__':
    try:
        # 파일에서 JSON 데이터 읽기
        with open("/tmp/criminalip_cachefile.txt", "r") as f:
            data = json.load(f)

        # 필요한 데이터 추출
        webcam_count = data["webcam_count"]
        scanning_record_count = data["scanning_record_count"]
        vulnerability_count = data["vulnerability_count"]
        ids_count = data["ids_count"]

        # Prepare data for Zabbix
        hostname = ZABBIX_HOSTNAME
        items = [
            ZabbixMetric(hostname, "criminalip.vulnerability.snort.count", ids_count),
            ZabbixMetric(hostname, "criminalip.vulnerability.cve.count", vulnerability_count),
            ZabbixMetric(hostname, "criminalip.vulnerability.webcam.count", webcam_count),
            ZabbixMetric(hostname, "criminalip.vulnerability.honeypot.count", scanning_record_count)
        ]

        # Send data to Zabbix
        zabbix_sender = ZabbixSender(ZABBIX_SERVER, ZABBIX_PORT)
        result = zabbix_sender.send(items)
        print("Zabbix sender result: {0}".format(str(result)))
    except fileNotFoundError:
        print("Error: criminalip_cachefile.txt not found.")

