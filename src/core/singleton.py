#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 23:25
# @Author  : Tony Tian
# @Email   : tiantangtl@foxmail.com
# @File    : singleton.py


def singleton(cls):
    """
    Singleton pattern
    :param cls: The class to be singleton
    :return: The instance of the class
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
