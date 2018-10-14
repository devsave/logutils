#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 22:34
# @Author  : Tony Tian
# @Email   : tiantangtl@foxmail.com
# @File    : filesystem.py

import os
import re
import datetime
from PyQt5.QtWidgets import QFileDialog

from logutils.ui_support import ApplicationGuard


class StreamReader:
    """
    A stream reader that can cycle from a root folder recursively(or not) to provide each line of the excepted files
    """
    def __init__(self, root_folder: str = '', file_filter: str='', recursive: bool = False,  remove_end: bool=True):
        """
        Initializer
        :param root_folder: The start root folder
        :param recursive: If cycle child folders
        :param file_filter: If a file is the expected one
        :param remove_end: If '\n' of each line will be removed
        """
        self.root_folder = root_folder
        self.recursive = recursive
        self.remove_line_end = remove_end
        self.file_filter = file_filter
        self.file_pattern = None
        if file_filter:
            self.file_pattern = re.compile(file_filter)

    def enumerate(self) -> tuple:
        """
        Cycle each line of the expected files
        :return: tuple of line and file path
        """
        if not self.root_folder:
            # Popup a dialog to choose the start folder
            ApplicationGuard()
            dialog = QFileDialog()
            self.root_folder = dialog.getExistingDirectory(caption='请选择起始目录')
            if not self.root_folder:
                print("没有选择有效目录")
                return

        assert os.path.exists(self.root_folder) and os.path.isdir(self.root_folder), "Input root folder is invalid."

        for root, folders, files in os.walk(self.root_folder, self.recursive):
            for base_name in files:

                # Check if the file is an expected one
                if self.file_pattern and not self.file_pattern.match(base_name):
                    continue

                file_path = os.path.join(root, base_name)
                with open(file_path, errors='ignore') as reader:
                    for line in reader:
                        if self.remove_line_end:
                            line = line.strip('\n')
                            yield (line, file_path)


class StreamWriter:
    """
    Stream writer class to write a list or dict into a csv file
    """
    def __init__(self, output_folder: str = '', file_name: str = ''):
        self.folder = output_folder
        self.file = file_name
        if not self.file:
            self.file = self.auto_file_name()
        self.file += '.csv'

    @staticmethod
    def auto_file_name() -> str:
        now_time = datetime.datetime.now()
        # Year_Month_Day_Hour_Minute_Second_Microsecond
        time_stamp = now_time.strftime('%Y_%m_%d_%H_%M_%S_%f')
        file_name = "log_analyzer_result_" + time_stamp
        return file_name

    def write_list(self, result: list):
        """
        Write list = [[],[],...] into csv files
        :param result:
        :return:
        """
        if not self.folder:
            # Popup a dialog to choose the start folder
            ApplicationGuard()
            dialog = QFileDialog()
            self.folder = dialog.getExistingDirectory(caption='请选择输出目录')
            if not self.folder:
                print("没有选择有效目录")
                return

        file_path = os.path.join(self.folder, self.file)
        with open(file_path, 'w') as writer:
            for item in result:
                writer.write(','.join(item))
                writer.write('\n')

    def write_dict(self, result: dict):
        """
        Write dict = {row -> {column -> value}} into csv files
        :param result:
        :return:
        """
        list_result = []
        row_count = len(result)
        for row_idx in range(row_count):
            row = result.get(row_idx, None)
            if row:
                line_result = []
                column_count = max(row.keys())
                for col_idx in range(column_count):
                    value = row.get(col_idx, '')
                    line_result.append(value)
                list_result.append(line_result)

        self.write_list(list_result)


def test():
    reader = StreamReader()
    for line, file in reader.enumerate():
        print(line)

    writer = StreamWriter()
    writer.write_list([])


if __name__ == '__main__':
    test()
