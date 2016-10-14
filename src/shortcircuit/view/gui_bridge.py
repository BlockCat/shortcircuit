# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_bridge.ui'
#
# Created: Fri Oct 14 18:53:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BridgeDialog(object):
    def setupUi(self, BridgeDialog):
        BridgeDialog.setObjectName("TripwireDialog")
        BridgeDialog.resize(400, 255)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BridgeDialog.sizePolicy().hasHeightForWidth())
        BridgeDialog.setSizePolicy(sizePolicy)
        BridgeDialog.setMinimumSize(QtCore.QSize(400, 255))
        BridgeDialog.setMaximumSize(QtCore.QSize(400, 255))
        font = QtGui.QFont()
        font.setFamily("Arial")
        BridgeDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BridgeDialog.setWindowIcon(icon)
        BridgeDialog.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(BridgeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(BridgeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.label_4 = QtGui.QLabel(BridgeDialog)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/tripwire_banner.png"))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.lineEdit_url = QtGui.QLineEdit(BridgeDialog)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.gridLayout.addWidget(self.lineEdit_url, 1, 1, 1, 1)
        self.label = QtGui.QLabel(BridgeDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(BridgeDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BridgeDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BridgeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BridgeDialog)

    def retranslateUi(self, BridgeDialog):
        BridgeDialog.setWindowTitle(QtGui.QApplication.translate("TripwireDialog", "Tripwire Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TripwireDialog", "URL:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
