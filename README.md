
# Criminalip Zabbix Template
## 1. About (Criminal IP integrated with Zabbix) 
Criminal IP is a comprehensive OSINT-based Cyber Threat Intelligence (CTI) search engine that can be used as an automated Attack Surface Management solution. 

We have created a template that integrates Criminal IP with Zabbix's monitoring to detect all security threats related to your exposed IP and open ports. It will notify you once a day about the number of exposed CVEs, the number of Honeypot attacks, and more. 

To retrieve data, you need a Criminal IP API key. You can register for a free account at https://www.criminalip.io/ and find your API key on the My Information page.

Please note that this template was created using malicious IP info from https://www.criminalip.io/en/developer/api/get-ip-malicious-info.  

In addition to the alarm service, you can also check out more detailed insights through Criminal IP integrated with Zabbix. You can search for suitable APIs and use them easily.

For more information or customization, please refer to the Web Filter and API Development Guide below: 
- Web Filter: https://www.criminalip.io/en/developer/filters-and-tags/filters
- API Development Guide: https://www.criminalip.io/en/developer/api/post-user-me


## 2. Zabbix Template Structure 
### 1) Macros used

<table class="wrapped fixed-table"><colgroup><col style="width: 221.0px;" /><col style="width: 97.0px;" /><col style="width: 70.0px;" /><col style="width: 88.0px;" /></colgroup>
<thead>
<tr>
<th>
<p>Name</p></th>
<th>
<p>Description</p></th>
<th>
<p>Default</p></th>
<th>
<p>Type</p></th></tr></thead>
<tbody>
<tr>
<td>
<p>{$CRIMINALIP_TARGET_PUBLIC_IP}</p></td>
<td>
<p>-</p></td>
<td><br /></td>
<td>
<p>Text macro</p></td></tr></tbody></table>

### 2) Template links
There are no template links in this template.

### 3) Discovery rules
<table class="wrapped fixed-table"><colgroup><col style="width: 218.0px;" /><col style="width: 226.0px;" /><col style="width: 326.0px;" /><col style="width: 703.0px;" /></colgroup>
<thead>
<tr>
<th>
<p>Name</p></th>
<th>
<p>Type</p></th>
<th>
<p>Key</p></th>
<th colspan="1"><span style="color: rgb(0,0,0);">Additional info&nbsp;</span></th></tr></thead>
<tbody>
<tr>
<td>
<p>LLD Current Opened Ports</p></td>
<td>
<p><code>Zabbix Agent<br />Zabbix Agent (Active)</code></p></td>
<td>
<p>lld.criminalip.ports</p>
<p>Update: 60s</p></td>
<td colspan="1">
<p>You can check the open ports and vulnerability information of the target public IP.&nbsp;&nbsp;</p>
<p>For more information, please refer to the Asset Search page at <a href="https://www.criminalip.io/en/asset">https://www.criminalip.io/en/asset</a>.&nbsp;</p></td></tr>
<tr>
<td colspan="1">
<p><span class="selected">Item prototypes</span></p></td>
<td colspan="1"><code>Zabbix Agent<br />Zabbix Agent (Active)</code></td>
<td colspan="1">
<p>check.criminalip.port[{#SOCKEY_TYPE}, {#PORT}]</p>
<p>Update: 60s</p></td>
<td colspan="1"><span style="color: rgb(0,0,0);">It creates the Socket type and Port of the current open port data and shows you the V<span style="color: rgb(68,68,68);">ulnerability category.</span></span></td></tr>
<tr>
<td colspan="1">Trigger prototypes</td>
<td colspan="1"><br /></td>
<td colspan="1">last(/Template Security Criminalip/check.criminalip.port[{#SOCKEY_TYPE}, {#PORT}])&gt;0</td>
<td colspan="1">
<p>The vulnerability is exposed to an open port of the target IP.</p>
<p>For more information, please refer to the Asset Search page at <a href="https://www.criminalip.io/en/asset">https://www.criminalip.io/en/asset</a>.&nbsp;</p></td></tr></tbody></table>

### 4) Items collected
<table class="wrapped fixed-table"><colgroup><col style="width: 183.0px;" /><col style="width: 97.0px;" /><col style="width: 236.0px;" /><col style="width: 335.0px;" /><col style="width: 822.0px;" /></colgroup>
<thead>
<tr>
<th>
<p>Name</p></th>
<th>
<p>Description</p></th>
<th>
<p>Type</p></th>
<th>
<p>Key</p></th>
<th colspan="1">Additional info&nbsp;</th></tr></thead>
<tbody>
<tr>
<td>
<p>Criminalip: Get Criminalip API</p></td>
<td>
<p>-</p></td>
<td><span>Zabbix Agent<br />Zabbix Agent(Active)</span></td>
<td>
<p>get.criminalip.api[{$CRIMINALIP_TARGET_PUBLIC_IP}]</p>
<p>Update: 1d</p></td>
<td colspan="1">
<p>You&nbsp;can&nbsp;get&nbsp;the&nbsp;get-ip-malicious-info&nbsp;information&nbsp;from&nbsp;<a href="https://api.criminalip.io">https://api.criminalip.io</a> and save it to a local file.&nbsp;</p>
<p><span style="color: rgb(0,0,0);text-decoration: none;">(Saved file</span><span style="color: rgb(0,0,0);text-decoration: none;">:&nbsp;/tmp/criminalip_cache.txt)</span></p>
<p><span style="color: rgb(0,0,0);text-decoration: none;">You&nbsp;can&nbsp;check&nbsp;more&nbsp;details&nbsp;at&nbsp;</span><span><span style="color: rgb(0,82,204);text-decoration: none;"><u><a href="https://www.criminalip.io/en/asset">https://www.criminalip.io/en/asset</a>.&nbsp;</u></span></span></p></td></tr>
<tr>
<td>
<p>Criminalip: Sender Criminalip Malicious</p></td>
<td>
<p>-</p></td>
<td>
<p><span>Zabbix Agent<br />Zabbix Agent(Active)</span></p></td>
<td>
<p>sender.criminalip.malicious.count</p>
<p>Update: 1h</p></td>
<td colspan="1"><span style="color: rgb(0,0,0);">The saved local file, criminalip_cache.txt is read and sends you the number of vulnerabilities to the items of each Trigger type.&nbsp;&nbsp;</span></td></tr>
<tr>
<td>
<p>Criminalip: Vulnerabilities CVE stats</p></td>
<td>
<p>-</p></td>
<td>
<p>Zabbix Triggers&nbsp;</p></td>
<td>
<p>criminalip.vulnerability.cve.count</p></td>
<td colspan="1">It counts <span style="color: rgb(0,0,0);">the number of times the server has been exposed to a CVE vulnerability.</span></td></tr>
<tr>
<td>
<p>Criminalip: Vulnerabilities Honypot stats</p></td>
<td>
<p>-</p></td>
<td>
<p>Zabbix Triggers&nbsp;</p></td>
<td>
<p>criminalip.vulnerability.honeypot.count</p></td>
<td colspan="1">
<p><span style="color: rgb(0,51,102);"><span style="text-decoration: none;">It&nbsp;counts&nbsp;the&nbsp;number&nbsp;of&nbsp;</span><span style="text-decoration: none;">Honeypot attacks.&nbsp;</span></span></p></td></tr>
<tr>
<td>
<p>Criminalip: Vulnerabilities Snort stats</p></td>
<td>
<p>-</p></td>
<td>
<p>Zabbix Triggers&nbsp;</p></td>
<td>
<p>criminalip.vulnerability.snort.count</p></td>
<td colspan="1">
<p><span style="color: rgb(0,51,102);">It counts the number of registered Public IPs at <a href="https://www.snort.org/" style="color: rgb(0,51,102);">https://www.snort.org/</a>.&nbsp;</span></p></td></tr>
<tr>
<td>
<p>Criminalip: Vulnerabilities Webcam stats</p></td>
<td>
<p>-</p></td>
<td>
<p>Zabbix Triggers&nbsp;</p></td>
<td>
<p>criminalip.vulnerability.webcam.count</p></td>
<td colspan="1"><span style="color: rgb(0,0,0);">It counts the number of webcam exposure.&nbsp;</span></td></tr></tbody></table>

### 5) Triggers
<table class="fixed-table wrapped"><colgroup><col style="width: 107.0px;" /><col style="width: 358.0px;" /><col style="width: 347.0px;" /><col style="width: 739.0px;" /></colgroup>
<thead>
<tr>
<th style="text-align: left;">
<p>Severit</p></th>
<th style="text-align: left;">
<p>Name</p></th>
<th style="text-align: left;">
<p>Expression</p></th>
<th colspan="1" style="text-align: left;">
<p><span style="color: rgb(0,0,0);">Additional info&nbsp;</span></p></th></tr></thead>
<tbody>
<tr>
<td style="text-align: left;">High</td>
<td style="text-align: left;">Criminalip: Vulnerability exposed in {$CRIMINALIP_TARGET_PUBLIC_IP}</td>
<td style="text-align: left;">
<p><span style="color: rgb(0,0,0);">last(/Template Security Criminalip/criminalip.vulnerability.cve.count)&gt;0</span></p></td>
<td colspan="1" style="text-align: left;">
<p><span style="color: rgb(0,0,0);">It triggers when the number of exposures to CVE vulnerability is greater than 0.&nbsp;</span></p>
<p><span style="color: rgb(0,0,0);">You can check details at <span style="color: rgb(0,0,0);"><a href="https://www.criminalip.io/en/asset">https://www.criminalip.io</a></span></span></p></td></tr>
<tr>
<td style="text-align: left;">Average</td>
<td style="text-align: left;">Criminalip: {$CRIMINALIP_TARGET_PUBLIC_IP} has exposed the webcam externally.</td>
<td style="text-align: left;"><span style="color: rgb(0,0,0);">last(/Template Security Criminalip/criminalip.vulnerability.webcam.count)&gt;0</span></td>
<td colspan="1" style="text-align: left;">
<p><span style="color: rgb(0,0,0);">It triggers when the webcam exposure is greater than 0.&nbsp;</span></p>
<p><span style="color: rgb(0,0,0);">You can check details at <a href="https://www.criminalip.io/en/asset">https://www.criminalip.io</a></span></p></td></tr>
<tr>
<td style="text-align: left;">Warning</td>
<td style="text-align: left;">Criminalip: {$CRIMINALIP_TARGET_PUBLIC_IP} is detected by Honeypot as a threat.</td>
<td style="text-align: left;"><span style="color: rgb(0,0,0);">last(/Template Security Criminalip/criminalip.vulnerability.honeypot.count)&gt;0</span></td>
<td colspan="1" style="text-align: left;">
<p><span style="color: rgb(0,0,0);">It triggers when Honeypot detection is greater than 0.&nbsp;</span></p>
<p><span style="color: rgb(0,0,0);">You can check details at <a href="https://www.criminalip.io/en/asset">https://www.criminalip.io</a></span></p></td></tr>
<tr>
<td style="text-align: left;">Warning</td>
<td style="text-align: left;">Criminalip: {$CRIMINALIP_TARGET_PUBLIC_IP} is detected by Snort as a threat.</td>
<td style="text-align: left;">
<p><span style="color: rgb(0,0,0);">last(/Template Security Criminalip/criminalip.vulnerability.snort.count)&gt;0</span></p></td>
<td colspan="1" style="text-align: left;">
<p><span style="color: rgb(0,0,0);">It triggers when IDS(snort) detection is greater than 0.<span style="color: rgb(255,0,0);">&nbsp;</span></span></p>
<p><span style="color: rgb(0,0,0);">You can check details at <a href="https://www.criminalip.io/en/asset">https://www.criminalip.io</a></span></p></td></tr></tbody></table>

### 6) Graph
<table class="wrapped fixed-table"><colgroup><col style="width: 214.0px;" /><col style="width: 600.0px;" /><col style="width: 94.0px;" /></colgroup>
<tbody>
<tr>
<th>&nbsp;Graph name&nbsp;</th>
<th>Item Name&nbsp;</th>
<th><br /></th></tr>
<tr>
<td rowspan="4">Criminalip: malicious info<br /><br /><br /></td>
<td><span>Template Security Criminalip: Criminalip: Vulnerabilities<span style="color: rgb(255,0,0);"> <span style="color: rgb(0,51,102);">Honeypot </span></span>stats&nbsp;<span style="color: rgb(255,0,0);"> &nbsp;</span></span></td>
<td>all</td></tr>
<tr>
<td><span>Template Security Criminalip: Criminalip: Vulnerabilities Snort stats</span></td>
<td>all</td></tr>
<tr>
<td colspan="1"><span>Template Security Criminalip: Criminalip: Vulnerabilities CVE stats</span></td>
<td colspan="1">all</td></tr>
<tr>
<td colspan="1"><span>Template Security Criminalip: Criminalip: Vulnerabilities Webcam stats</span></td>
<td colspan="1">all</td></tr></tbody></table>

## 4. Zabbix Server Settings
Edit ExternalScripts in the Zabbix server.
<BR/><BR/>
__vi /etc/zabbix/zabbix_server.conf :__
```
ExternalScripts=/usr/lib/zabbix/externalscripts
```

__Restart the Zabbix server.__
```
$ systemctl restart zabbix-server
```

## 5. Zabbix Agent Settings
__Mandatory installation__
- The Zabbix-sender must be installed. 

Register UserParameter 
Create and save the /etc/zabbix/zabbix_agentd.d/criminalip.conf file
<BR/><BR/>
__vi /etc/zabbix/zabbix_agentd.d/criminalip.conf :__
```
UserParameter=get.criminalip.api[*],/usr/lib/zabbix/externalscripts/Get_criminalip_data.py $1
UserParameter=sender.criminalip.malicious.count,/usr/lib/zabbix/externalscripts/FileRead_count_criminalip.py
UserParameter=lld.criminalip.ports,/usr/lib/zabbix/externalscripts/FileRead_lld_criminalip.py
UserParameter=check.criminalip.port[*],/usr/lib/zabbix/externalscripts/Check_has_vulnerability.py $1 $2
```

Save the following Python script (UserParameter), which is stored in GIT, to the /usr/lib/zabbix/externalscripts/ directory
<BR/><BR/>
__ls /usr/lib/zabbix/externalscripts/ :__
```
Get_criminalip_data.py
FileRead_count_criminalip.py
Check_has_vulnerability.py
FileRead_lld_criminalip.py
```
<BR/>
Changing permissions with Zabbix 
```
$ chown -Rf zabbix:zabbix /usr/lib/zabbix/externalscripts/
```

Edit the file /usr/lib/zabbix/externalscripts/Get_criminalip_data.py
- ${CRIMINALIP_API_KEY}: Register API_KEY issued from https://www.criminalip.io/
<BR/><BR/>
__vi /usr/lib/zabbix/externalscripts/Get_criminalip_data.py :__
```
API_KEY = '${CRIMINALIP_API_KEY}'
```
Edit the file /usr/lib/zabbix/externalscripts/FileRead_count_criminalip.py
- ${ZABBIX_SERVER_IP}: Enter the Zabbix server or Proxy IP 
- ${ZABBIX_SERVER_PORT}: Enter the Zabbix server or Proxy IP 
<BR/><BR/>
__vi /usr/lib/zabbix/externalscripts/FileRead_count_criminalip.py :__
```
ZABBIX_SERVER = '${ZABBIX_SERVER_IP}'
ZABBIX_PORT = '${ZABBIX_SERVER_PORT}'
```
<BR/>
Install the Python library to use the UserParameter script 
```
$ pip install requests
$ pip install py-zabbix
```

Restart Zabbix agent
```
$ systemctl restart zabbix-agent
```
<BR/>
## 6. Test Process
__Run on a Zabbix server__

Check the Criminal IP API to verify if the searched information is stored properly to ***/tmp/criminalip_cache.txt***

- ${ZABBIX_AGENT_IPADDRESS}: Enter the Access IP where the Zabbix agent is installed, accessed by the Zabbix server (or proxy) 
- ${CRIMINALIP_TARGET_PUBLIC_IP}: Enter the Public IP target (macro registration) to detect threats 

```
$ zabbix_get -s ${ZABBIX_AGENT_IPADDRESS} -k get.criminalip.api[${CRIMINALIP_TARGET_PUBLIC_IP}]
```
<BR/>
Data saved to file: /tmp/criminalip_cachefile.txt

__cat /tmp/criminalip_cachefile.txt :__
```
{
    "datetime": "2023-03-28T12:34:06.038880",
    "ip": "${CRIMINALIP_TARGET_PUBLIC_IP}",
    "ids_count": 0,
    "vulnerability_count": 39,
    "webcam_count": 0,
    "scanning_record_count": 0,
    "current_opened_port_value":
    [
        {"socket_type": "tcp", "port": 22, "protocol": "ssh", "product_name": "openssh", "product_version": "7.4", "has_vulnerability": true, "confirmed_time": "2023-02-21 16:58:52"},
        {"socket_type": "tcp", "port": 80, "protocol": "http", "product_name": "openssl", "product_version": "1.0.2k", "has_vulnerability": true, "confirmed_time": "2023-02-22 03:24:31"},
        {"socket_type": "tcp", "port": 443, "protocol": "https", "product_name": "openssl", "product_version": "1.0.2k", "has_vulnerability": true, "confirmed_time": "2023-02-05 03:01:50"}
    ]
}
```
Check whether the discovery function of the saved local file works correctly
- ${ZABBIX_AGENT_IPADDRESS}: Enter the Access IP where the Zabbix agent is installed, accessed by the zabbix_server (or proxy) 

```
{
    "data":
    [
        {"{#SOCKEY_TYPE}": "tcp", "{#PROTOCOL}": "ssh", "{#PORT}": 22, "{#PRODUCT_NAME}": "openssh", "{#PRODUCT_VERSION}": "7.4", "{#HAS_VULNERABILITY}": true, "{#CONFIRMED_TIME}": "2023-02-21 16:58:52"},
        {"{#SOCKEY_TYPE}": "tcp", "{#PROTOCOL}": "http", "{#PORT}": 80, "{#PRODUCT_NAME}": "openssl", "{#PRODUCT_VERSION}": "1.0.2k", "{#HAS_VULNERABILITY}": true, "{#CONFIRMED_TIME}": "2023-02-22 03:24:31"},
        {"{#SOCKEY_TYPE}": "tcp", "{#PROTOCOL}": "https", "{#PORT}": 443, "{#PRODUCT_NAME}": "openssl", "{#PRODUCT_VERSION}": "1.0.2k", "{#HAS_VULNERABILITY}": true, "{#CONFIRMED_TIME}": "2023-02-05 03:01:50"}
    ]
}
```
