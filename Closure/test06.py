#!/usr/bin/python3
# coding=utf-8


def make_div(func):
    def inner(*args, **kwargs):
        return "<div>" + func() + "</div>"
    return inner

def make_p(func):
    def inner(*args, **kwargs):
        return "<p>" + func() + "</p>"
    return inner

@make_div
@make_p
def content():
    return "人生苦短"

result = content()

print(result)
