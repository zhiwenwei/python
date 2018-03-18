#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
 * Created on 2017/6/6 21:49.
 * @author: Chinge_Yang.
'''

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_HOME = "{}/home".format(BASE_DIR)
LOG_DIR = "{}/log".format(BASE_DIR)
LOG_LEVEL = "DEBUG"

ACCOUNT_FILE = "{}/conf/accounts.cfg".format(BASE_DIR)

HOST = "0.0.0.0"
PORT = 9999


