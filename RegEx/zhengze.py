#!/usr/bin/python3
# coding=utf-8

import re 

result = re.match("itcast", "itcast.cn")
info = result.group()
print(info)
