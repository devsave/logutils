#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 16:15
# @Author  : Tony Tian
# @Email   : tiantangtl@foxmail.com
# @File    : regex_checker.py

import re
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from Ui_RegexCheckerDialog import Ui_RegexCheckerDialog


class RegexCheckerDialog(QDialog):
    def __init__(self):
        super(RegexCheckerDialog, self).__init__()
        self.ui = Ui_RegexCheckerDialog()
        self.ui.setupUi(self)

        # Connect the slot
        self.ui.btnRun.clicked.connect(self.run_regex)

    def run_regex(self):
        # Clear old results
        self.ui.lwResult.clear()

        regex_string = self.ui.leRegex.text()
        if not regex_string:
            msg = QMessageBox()
            msg.warning(self, "提示", "请输入正则表达式！", QMessageBox.Ok)
            msg.show()
            return

        is_match = True if self.ui.cbMode.currentIndex() == 0 else False
        target_string = self.ui.pteTarget.toPlainText()
        if not target_string:
            msg = QMessageBox()
            msg.warning(self, "提示", "请输入目标字符串！", QMessageBox.Ok)
            msg.show()
            return

        pattern = re.compile(regex_string)
        if is_match:
            result = pattern.match(target_string)
        else:
            result = pattern.search(target_string)

        if result:
            self.ui.leMessage.setText("匹配成功！")
            self.print_result(result)
        else:
            self.ui.leMessage.setText("匹配失败！")

    def print_result(self, regex_result):
        group_count = regex_result.re.groups
        for idx in range(group_count + 1):
            self.ui.lwResult.addItem('Group[%d]: %s' % (idx, regex_result.group(idx)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = RegexCheckerDialog()
    dialog.show()
    sys.exit(app.exec_())
