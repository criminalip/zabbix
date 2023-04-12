#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import sys

if sys.version_info.major == 2:
    fileNotFoundError = IOError
else:
    fileNotFoundError = FileNotFoundError

if __name__ == '__main__':
    try:
        # 파일에서 JSON 데이터 읽기
        with open("/tmp/criminalip_cachefile.txt", "r") as f:
            data = json.load(f)

        # Prepare discovery data for Zabbix
        discovery_data = {"data": []}
        if isinstance(data, dict) and "current_opened_port_value" in data:
            data = data["current_opened_port_value"]
        for port_value in data:
            if isinstance(port_value, dict):
                discovery_data["data"].append({
                    "{#SOCKEY_TYPE}": port_value["socket_type"],
                    "{#PROTOCOL}": port_value["protocol"],
                    "{#PORT}": port_value["port"],
                    "{#PRODUCT_NAME}": port_value["product_name"],
                    "{#PRODUCT_VERSION}": port_value["product_version"],
                    "{#HAS_VULNERABILITY}": port_value["has_vulnerability"],
                    "{#CONFIRMED_TIME}": port_value["confirmed_time"]
                })

        # Print discovery data to Zabbix
        print(json.dumps(discovery_data))

    except fileNotFoundError:
        print("Error: criminalip_cachefile.txt not found.")
