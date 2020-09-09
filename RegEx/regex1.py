#!/usr/bin/python3
# coding=utf-8


import re

#ret = re.match(".", "M")
#print(ret.group())

#ret = re.match("t.o", "two")
#print(ret.group())
#
#ret = re.match("...", "too")
#print(ret.group())
#
#ret = re.match("h", "hello Python")
#print(ret.group())
#
#ret = re.match("H", "Hello Python")
#print(ret.group())

#ret = re.match("[hH]", "hello Python")
#print(ret.group())
#ret = re.match("[hH]", "Hello Python")
#print(ret.group())
#ret = re.match("[hH]ello Python", "Hello Python")
#print(ret.group())
#
#ret = re.match("[0123456789]Hello Python", "7Hello Python")
#print(ret.group())
#
#ret = re.match("[0-9]Hello Python", "7Hello Python")
#print(ret.group())
#
#ret = re.match("[0-35-9]Hello Python", "7Hello Python")
#print(ret.group())
#
#ret = re.match("[0-35-9]Hello Python", "4Hello Python")
#print(ret.group())

ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥2号", "嫦娥2号发射成功")
print(ret.group())
ret = re.match("嫦娥3号", "嫦娥3号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

match_obj = re.match("\D", "f")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

match_obj = re.match("hello\sworld", "hello world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("hello\sworld", "hello\tworld")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("hello\Sworld", "hello&world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("hello\Sworld", "hello$world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("\w", "A")
if match_obj:
    print(match_obj.group())
else:
    print("match fail")

match_obj = re.match("\W", "&")
if match_obj:
    print(match_obj.group())
else:
    print("match fail")



