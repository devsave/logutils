# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegexCheckerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegexCheckerDialog(object):
    def setupUi(self, RegexCheckerDialog):
        RegexCheckerDialog.setObjectName("RegexCheckerDialog")
        RegexCheckerDialog.resize(505, 657)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        RegexCheckerDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/regex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RegexCheckerDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(RegexCheckerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(RegexCheckerDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leRegex = QtWidgets.QLineEdit(RegexCheckerDialog)
        self.leRegex.setObjectName("leRegex")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leRegex)
        self.label_2 = QtWidgets.QLabel(RegexCheckerDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cbMode = QtWidgets.QComboBox(RegexCheckerDialog)
        self.cbMode.setObjectName("cbMode")
        self.cbMode.addItem("")
        self.cbMode.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbMode)
        self.verticalLayout.addLayout(self.formLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(RegexCheckerDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pteTarget = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.pteTarget.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.pteTarget.setObjectName("pteTarget")
        self.horizontalLayout.addWidget(self.pteTarget)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.btnRun = QtWidgets.QPushButton(RegexCheckerDialog)
        self.btnRun.setObjectName("btnRun")
        self.verticalLayout.addWidget(self.btnRun)
        self.groupBox = QtWidgets.QGroupBox(RegexCheckerDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leMessage = QtWidgets.QLabel(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.leMessage.setPalette(palette)
        self.leMessage.setText("")
        self.leMessage.setObjectName("leMessage")
        self.verticalLayout_2.addWidget(self.leMessage)
        self.lwResult = QtWidgets.QListWidget(self.groupBox)
        self.lwResult.setObjectName("lwResult")
        self.verticalLayout_2.addWidget(self.lwResult)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(RegexCheckerDialog)
        QtCore.QMetaObject.connectSlotsByName(RegexCheckerDialog)

    def retranslateUi(self, RegexCheckerDialog):
        _translate = QtCore.QCoreApplication.translate
        RegexCheckerDialog.setWindowTitle(_translate("RegexCheckerDialog", "正则表达式校验器"))
        self.label.setText(_translate("RegexCheckerDialog", "正则表达式："))
        self.label_2.setText(_translate("RegexCheckerDialog", "模式："))
        self.cbMode.setItemText(0, _translate("RegexCheckerDialog", "匹配(Match)"))
        self.cbMode.setItemText(1, _translate("RegexCheckerDialog", "搜索(Search)"))
        self.groupBox_2.setTitle(_translate("RegexCheckerDialog", "目标字符串"))
        self.btnRun.setText(_translate("RegexCheckerDialog", "运行"))
        self.groupBox.setTitle(_translate("RegexCheckerDialog", "结果："))

import regex_rc