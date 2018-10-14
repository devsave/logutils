#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 23:24
# @Author  : Tony Tian
# @Email   : tiantangtl@foxmail.com
# @File    : UiApp.py

import sys
from PyQt5.QtWidgets import QApplication
from core.singleton import singleton


@singleton
class ApplicationGuard:
    def __init__(self):
        self.app = QApplication(sys.argv)
        # sys.exitfunc = self.app.exec_()

    def get_application(self):
        return self.app
