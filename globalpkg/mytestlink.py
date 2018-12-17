#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'laifuyu'

from testlink import TestLinkHelper, TestlinkAPIClient
#from testlink.testlinkerrors import TLResponseError
from globalpkg.log import logger

class TestLink():
    def __init__(self):
        tlk_helper = TestLinkHelper(server_url='http://192.168.202.174/testlink-1.9.17/lib/api/xmlrpc/v1/xmlrpc.php', devkey='0b839ca6b6a4d8b78139e5f5f93c38f1')
        try:
            self.testlink = tlk_helper.connect(TestlinkAPIClient)  # 连接TestLink
        except Exception as e:
            logger.error('连接testlink失败：%s' % e)
            exit()

    def get_testlink(self):
        return self.testlink


