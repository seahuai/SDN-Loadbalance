#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt
import time
import httplib2
import json

class ODLUtil:
    url = ""
    http = httplib2.Http()
    http.add_credentials('admin', 'admin')
    def __init__(self, host, port):
        self.url = "http://" + host + ":" + port



    def installFlows(self):
        headers = {'Content-type': 'application/json'}

        h1tos1 = '{"flow": [{"id": "1","match": {"in-port": "1"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "2"},"order": "0"}]}}]},'\
            	'"priority": "101","cookie": "667","table_id": "0"}]}'

        s1toh1 = '{"flow": [{"id": "2","match": {"in-port": "2"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "1"},"order": "0"}]}}]},'\
            	'"priority": "101","cookie": "667","table_id": "0"}]}'

        s3toh1 = '{"flow": [{"id": "3","match": {"in-port": "1"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "3"},"order": "0"},{"output-action":{'\
                '"output-node-connector": "2"},"order": "1"}]}}]},'\
            	'"priority": "100","cookie": "667","table_id": "0"}]}'

        h1tos3 = '{"flow": [{"id": "4","match": {"in-port": "3"},'\
            	'"instructions": {"instruction": [{"order": "0",'\
                '"apply-actions": {"action": [{"output-action": {'\
                '"output-node-connector": "1"},"order": "0"}]}}]},'\
            	'"priority": "100","cookie": "667","table_id": "0"}]}'

        flows1 = [
            (h1tos1, 1),
            (s1toh1, 2),
            (s3toh1, 3),
            (h1tos3, 4)
        ]


        success = False
        # s1 流表
        for flow in flows1:
            endpoint = '/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/' + str(flow[1])
            response, content = self.http.request(uri=self.url + endpoint, body=flow[0], method='PUT',headers=headers)
            print (flow[1])
            if response['status'] != '200' :
                print ('流表加载失败', content.decode('utf-8'))
                success = False
                break
            success = True

        h2tos1 = '{"flow": [{"id": "1","match": {"in-port": "1"},' \
                 '"instructions": {"instruction": [{"order": "0",' \
                 '"apply-actions": {"action": [{"output-action": {' \
                 '"output-node-connector": "4"},"order": "0"}]}}]},' \
                 '"priority": "101","cookie": "667","table_id": "0"}]}'

        s1toh2h3 = '{"flow": [{"id": "2","match": {"in-port": "4" },' \
                 '"instructions": {"instruction": [{"order": "0",' \
                 '"apply-actions": {"action": [{"output-action": {' \
                 '"output-node-connector": "1"},"order": "0"}, {"output-action": {' \
                 '"output-node-connector": "2"},"order": "1"}]}}]},' \
                 '"priority": "101","cookie": "667","table_id": "0"}]}'

        h3tos1 = '{"flow": [{"id": "3","match": {"in-port": "2"},' \
                 '"instructions": {"instruction": [{"order": "0",' \
                 '"apply-actions": {"action": [{"output-action": {' \
                 '"output-node-connector": "4"},"order": "0"}]}}]},' \
                 '"priority": "101","cookie": "667","table_id": "0"}]}'

        h2tos1ts3 = '{"flow": [{"id": "4","match": {"in-port": "1"},' \
                 '"instructions": {"instruction": [{"order": "0",' \
                 '"apply-actions": {"action": [{"output-action": {' \
                 '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                 '"output-node-connector": "4"},"order": "1"}]}}]},' \
                 '"priority": "100","cookie": "667","table_id": "0"}]}'

        h3tos1ts3 = '{"flow": [{"id": "5","match": {"in-port": "2"},' \
                 '"instructions": {"instruction": [{"order": "0",' \
                 '"apply-actions": {"action": [{"output-action": {' \
                 '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                 '"output-node-connector": "4"},"order": "1"}]}}]},' \
                 '"priority": "100","cookie": "667","table_id": "0"}]}'


        flows2 = [
            (h2tos1, 1),
            (s1toh2h3, 2),
            (h3tos1, 3),
            (h2tos1ts3, 4),
            (h3tos1ts3, 5)
            # (h2toh3, 4)
        ]

        headers = {'Content-type': 'application/json'}
        success = False
        # s2 流表
        for flow in flows2:
            endpoint = '/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/' + str(
                flow[1])
            response, content = self.http.request(uri=self.url + endpoint, body=flow[0], method='PUT', headers=headers)
            print (flow[1])
            if response['status'] != '200':
                print ('流表加载失败', content.decode('utf-8'))
                success = False
                break
            success = True


        s3s1 = '{"flow": [{"id": "1","match": {"in-port": "1"},' \
               '"instructions": {"instruction": [{"order": "0",' \
               '"apply-actions": {"action": [{"output-action": {' \
               '"output-node-connector": "2"},"order": "0"}]}}]},' \
               '"priority": "101","cookie": "667","table_id": "0"}]}'

        s3s2 = '{"flow": [{"id": "2","match": {"in-port": "2"},' \
               '"instructions": {"instruction": [{"order": "0",' \
               '"apply-actions": {"action": [{"output-action": {' \
               '"output-node-connector": "1"},"order": "0"}]}}]},' \
               '"priority": "101","cookie": "667","table_id": "0"}]}'

        flows3 = [
            (s3s1, 1),
            (s3s2, 2)
        ]

        for flow in flows3:
            endpoint = '/restconf/config/opendaylight-inventory:nodes/node/openflow:3/flow-node-inventory:table/0/flow/' + str(
                flow[1])
            response, content = self.http.request(uri=self.url + endpoint, body=flow[0], method='PUT', headers=headers)
            print (flow[1])
            if response['status'] != '200':
                print ('流表加载失败', content.decode('utf-8'))
                success = False
                break
            success = True

        if success:
            print ('流表项加载完成')


    def nodeState(self, switchid, port):
        # http = httplib2.Http()
        # http.add_credentials('admin', 'admin')
        uri =  self.url + "/restconf/operational/opendaylight-inventory:nodes/node/openflow:" + str(switchid) + \
               "/node-connector/openflow:" + str(switchid) + ":" + str(port)
        response, content = self.http.request(uri=uri, method='GET')
        if response['status'] == '200':
            # with open('output.txt', 'w') as outputFile:
            #     outputFile.write(content)
            content = json.loads(content)
            statistics = content['node-connector'][0]['opendaylight-port-statistics:flow-capable-node-connector-statistics']
            bytes = statistics['bytes']['transmitted']
            duration = statistics['duration']['second']

            return  float(bytes) / float(duration)

    def loadbalance(self, speed):
        endpoint2 = '/restconf/config/opendaylight-inventory:nodes/node/openflow:2/flow-node-inventory:table/0/flow/'
        endpoint1 = '/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/flow/'
        headers = {'Content-type': 'application/json'}
        if speed > 400:


            print ("route: s2 - s3 - s1")

            s3toh1 = '{"flow": [{"id": "3","match": {"in-port": "1"},' \
                     '"instructions": {"instruction": [{"order": "0",' \
                     '"apply-actions": {"action": [{"output-action": {' \
                     '"output-node-connector": "3"},"order": "0"},{'\
                '"output-node-connector": "3"},"order": "0"}]}}]},' \
                     '"priority": "101","cookie": "667","table_id": "0"}]}'

            h1tos3 = '{"flow": [{"id": "4","match": {"in-port": "3"},' \
                     '"instructions": {"instruction": [{"order": "0",' \
                     '"apply-actions": {"action": [{"output-action": {' \
                     '"output-node-connector": "1"},"order": "0"}]}}]},' \
                     '"priority": "101","cookie": "667","table_id": "0"}]}'

            h2tos1ts3 = '{"flow": [{"id": "4","match": {"in-port": "1"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"output-action": {' \
                        '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                 '"output-node-connector": "4"},"order": "1"}]}}]},' \
                        '"priority": "101","cookie": "667","table_id": "0"}]}'

            h3tos1ts3 = '{"flow": [{"id": "5","match": {"in-port": "2"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"output-action": {' \
                        '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                 '"output-node-connector": "4"},"order": "1"}]}}]},' \
                        '"priority": "101","cookie": "667","table_id": "0"}]}'


            response, content = self.http.request(uri=self.url + endpoint1 + '3', body=s3toh1, method='PUT', headers=headers)
            response, content = self.http.request(uri=self.url + endpoint1 + '4', body=h1tos3, method='PUT',
                                                  headers=headers)
            response, content = self.http.request(uri=self.url + endpoint2 + '4', body=h2tos1ts3, method='PUT',
                                                  headers=headers)
            response, content = self.http.request(uri=self.url + endpoint2 + '5', body=h3tos1ts3, method='PUT',
                                                  headers=headers)



        else:

            print ("route: s2 - s1")

            s3toh1 = '{"flow": [{"id": "3","match": {"in-port": "1"},' \
                     '"instructions": {"instruction": [{"order": "0",' \
                     '"apply-actions": {"action": [{"output-action": {' \
                     '"output-node-connector": "3"},"order": "0"},{' \
                     '"output-node-connector": "3"},"order": "0"}]}}]},' \
                     '"priority": "100","cookie": "667","table_id": "0"}]}'

            h1tos3 = '{"flow": [{"id": "4","match": {"in-port": "3"},' \
                     '"instructions": {"instruction": [{"order": "0",' \
                     '"apply-actions": {"action": [{"output-action": {' \
                     '"output-node-connector": "1"},"order": "0"}]}}]},' \
                     '"priority": "100","cookie": "667","table_id": "0"}]}'

            h2tos1ts3 = '{"flow": [{"id": "4","match": {"in-port": "1"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"output-action": {' \
                        '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                        '"output-node-connector": "4"},"order": "1"}]}}]},' \
                        '"priority": "100","cookie": "667","table_id": "0"}]}'

            h3tos1ts3 = '{"flow": [{"id": "5","match": {"in-port": "2"},' \
                        '"instructions": {"instruction": [{"order": "0",' \
                        '"apply-actions": {"action": [{"output-action": {' \
                        '"output-node-connector": "3"},"order": "0"},{"output-action":{' \
                        '"output-node-connector": "4"},"order": "1"}]}}]},' \
                        '"priority": "100","cookie": "667","table_id": "0"}]}'


            response, content = self.http.request(uri=self.url + endpoint1 + '3', body=s3toh1, method='PUT', headers=headers)
            response, content = self.http.request(uri=self.url + endpoint1 + '4', body=h1tos3, method='PUT',
                                                  headers=headers)
            response, content = self.http.request(uri=self.url + endpoint2 + '4', body=h2tos1ts3, method='PUT',
                                                  headers=headers)
            response, content = self.http.request(uri=self.url + endpoint2 + '5', body=h3tos1ts3, method='PUT',
                                                  headers=headers)



def loadbalance():
    while(1):
        time.sleep(1)
        speed = odl.nodeState(2, 4)
        speed1 = odl.nodeState(2, 3)
        print ('端口4速度：' + str(speed) + " byte/s")
        print ('端口3速度：' + str(speed1) + " byte/s")
        odl.loadbalance(speed)

ops, args =  getopt.getopt(sys.argv[1:], "h", ["init", "loadbalance"])
odl = ODLUtil("127.0.0.1", "8181")
for op, value in ops:
    if op == "-h":
        helpstr ="""
        --init: 初始化流表
        --loadbalance: 启动负债均衡
        """
        print (helpstr)
    elif op == "--init":
        print ("初始化中...")
        odl.installFlows()
    elif op == "--loadbalance":
        print ("启动负债均衡")
        loadbalance()










