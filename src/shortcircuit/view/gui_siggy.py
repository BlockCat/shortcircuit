# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\gui_siggy.ui'
#
# Created: Wed Mar 01 13:13:44 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SiggyDialog(object):
    def setupUi(self, SiggyDialog):
        SiggyDialog.setObjectName("SiggyDialog")
        SiggyDialog.resize(400, 255)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SiggyDialog.sizePolicy().hasHeightForWidth())
        SiggyDialog.setSizePolicy(sizePolicy)
        SiggyDialog.setMinimumSize(QtCore.QSize(400, 255))
        SiggyDialog.setMaximumSize(QtCore.QSize(400, 255))
        font = QtGui.QFont()
        font.setFamily("Arial")
        SiggyDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SiggyDialog.setWindowIcon(icon)
        SiggyDialog.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(SiggyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(SiggyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 3)
        self.label_4 = QtGui.QLabel(SiggyDialog)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/siggy_banner.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 3)
        self.lineEdit_user_siggy = QtGui.QLineEdit(SiggyDialog)
        self.lineEdit_user_siggy.setObjectName("lineEdit_user_siggy")
        self.gridLayout.addWidget(self.lineEdit_user_siggy, 2, 3, 1, 1)
        self.lineEdit_pass_siggy = QtGui.QLineEdit(SiggyDialog)
        self.lineEdit_pass_siggy.setEnabled(True)
        self.lineEdit_pass_siggy.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass_siggy.setObjectName("lineEdit_pass_siggy")
        self.gridLayout.addWidget(self.lineEdit_pass_siggy, 5, 3, 1, 1)
        self.label_8 = QtGui.QLabel(SiggyDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_9 = QtGui.QLabel(SiggyDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.retranslateUi(SiggyDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SiggyDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SiggyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SiggyDialog)

    def retranslateUi(self, SiggyDialog):
        SiggyDialog.setWindowTitle(QtGui.QApplication.translate("SiggyDialog", "Tripwire Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SiggyDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SiggyDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
