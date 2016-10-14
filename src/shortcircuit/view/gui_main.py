# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created: Fri Oct 14 18:59:22 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 856)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_banner = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_banner.setMinimumSize(QtCore.QSize(420, 132))
        self.graphicsView_banner.setMaximumSize(QtCore.QSize(16777215, 132))
        self.graphicsView_banner.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_banner.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_banner.setObjectName("graphicsView_banner")
        self.verticalLayout.addWidget(self.graphicsView_banner)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(330, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_source = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_source.sizePolicy().hasHeightForWidth())
        self.lineEdit_source.setSizePolicy(sizePolicy)
        self.lineEdit_source.setMaxLength(32)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout.addWidget(self.lineEdit_source, 1, 1, 1, 1)
        self.label_destination = QtGui.QLabel(self.groupBox)
        self.label_destination.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_destination.setObjectName("label_destination")
        self.gridLayout.addWidget(self.label_destination, 3, 0, 1, 1)
        self.lineEdit_destination = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_destination.setMaxLength(32)
        self.lineEdit_destination.setPlaceholderText("")
        self.lineEdit_destination.setObjectName("lineEdit_destination")
        self.gridLayout.addWidget(self.lineEdit_destination, 3, 1, 1, 1)
        self.label_source = QtGui.QLabel(self.groupBox)
        self.label_source.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_source.setObjectName("label_source")
        self.gridLayout.addWidget(self.label_source, 1, 0, 1, 1)
        self.pushButton_player_location = QtGui.QPushButton(self.groupBox)
        self.pushButton_player_location.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/crest_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_player_location.setIcon(icon1)
        self.pushButton_player_location.setObjectName("pushButton_player_location")
        self.gridLayout.addWidget(self.pushButton_player_location, 1, 2, 1, 1)
        self.pushButton_find_path = QtGui.QPushButton(self.groupBox)
        self.pushButton_find_path.setObjectName("pushButton_find_path")
        self.gridLayout.addWidget(self.pushButton_find_path, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_status = QtGui.QLabel(self.groupBox)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 4, 1, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.tableWidget_path = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_path.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_path.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_path.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_path.setRowCount(0)
        self.tableWidget_path.setColumnCount(0)
        self.tableWidget_path.setObjectName("tableWidget_path")
        self.tableWidget_path.setColumnCount(0)
        self.tableWidget_path.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_path)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_set_dest = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_set_dest.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_set_dest.setMaxLength(32)
        self.lineEdit_set_dest.setObjectName("lineEdit_set_dest")
        self.gridLayout_3.addWidget(self.lineEdit_set_dest, 0, 1, 1, 1)
        self.pushButton_set_dest = QtGui.QPushButton(self.groupBox)
        self.pushButton_set_dest.setEnabled(False)
        self.pushButton_set_dest.setIcon(icon1)
        self.pushButton_set_dest.setObjectName("pushButton_set_dest")
        self.gridLayout_3.addWidget(self.pushButton_set_dest, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_short_format = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_short_format.setReadOnly(True)
        self.lineEdit_short_format.setObjectName("lineEdit_short_format")
        self.gridLayout_3.addWidget(self.lineEdit_short_format, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox__options = QtGui.QGroupBox(self.centralwidget)
        self.groupBox__options.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox__options.setMaximumSize(QtCore.QSize(280, 16777215))
        self.groupBox__options.setObjectName("groupBox__options")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox__options)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_trip_get = QtGui.QPushButton(self.groupBox__options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_trip_get.sizePolicy().hasHeightForWidth())
        self.pushButton_trip_get.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/tripwire_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_trip_get.setIcon(icon2)
        self.pushButton_trip_get.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_trip_get.setObjectName("pushButton_trip_get")
        self.gridLayout_4.addWidget(self.pushButton_trip_get, 1, 0, 1, 1)
        self.pushButton_trip_config = QtGui.QPushButton(self.groupBox__options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_trip_config.sizePolicy().hasHeightForWidth())
        self.pushButton_trip_config.setSizePolicy(sizePolicy)
        self.pushButton_trip_config.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_trip_config.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/config_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_trip_config.setIcon(icon3)
        self.pushButton_trip_config.setObjectName("pushButton_trip_config")
        self.gridLayout_4.addWidget(self.pushButton_trip_config, 1, 1, 1, 1)
        self.pushButton_crest_config = QtGui.QPushButton(self.groupBox__options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_crest_config.sizePolicy().hasHeightForWidth())
        self.pushButton_crest_config.setSizePolicy(sizePolicy)
        self.pushButton_crest_config.setIcon(icon3)
        self.pushButton_crest_config.setObjectName("pushButton_crest_config")
        self.gridLayout_4.addWidget(self.pushButton_crest_config, 0, 1, 1, 1)
        self.pushButton_eve_login = QtGui.QPushButton(self.groupBox__options)
        self.pushButton_eve_login.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eve_login.sizePolicy().hasHeightForWidth())
        self.pushButton_eve_login.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/eve_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_eve_login.setIcon(icon4)
        self.pushButton_eve_login.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_eve_login.setObjectName("pushButton_eve_login")
        self.gridLayout_4.addWidget(self.pushButton_eve_login, 0, 0, 1, 1)
        self.pushButton_bridge = QtGui.QPushButton(self.groupBox__options)
        self.pushButton_bridge.setObjectName("pushButton_bridge")
        self.gridLayout_4.addWidget(self.pushButton_bridge, 2, 0, 1, 1)
        self.pushButton_bridge_conf = QtGui.QPushButton(self.groupBox__options)
        self.pushButton_bridge_conf.setIcon(icon3)
        self.pushButton_bridge_conf.setObjectName("pushButton_bridge_conf")
        self.gridLayout_4.addWidget(self.pushButton_bridge_conf, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.label_trip_status = QtGui.QLabel(self.groupBox__options)
        self.label_trip_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trip_status.setObjectName("label_trip_status")
        self.verticalLayout_3.addWidget(self.label_trip_status)
        self.label_evescout_status = QtGui.QLabel(self.groupBox__options)
        self.label_evescout_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_evescout_status.setObjectName("label_evescout_status")
        self.verticalLayout_3.addWidget(self.label_evescout_status)
        self.groupBox_restrictions = QtGui.QGroupBox(self.groupBox__options)
        self.groupBox_restrictions.setObjectName("groupBox_restrictions")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_restrictions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtGui.QLabel(self.groupBox_restrictions)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_size = QtGui.QComboBox(self.groupBox_restrictions)
        self.comboBox_size.setObjectName("comboBox_size")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_size)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.checkBox_eol = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_eol.setObjectName("checkBox_eol")
        self.verticalLayout_5.addWidget(self.checkBox_eol)
        self.checkBox_masscrit = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_masscrit.setObjectName("checkBox_masscrit")
        self.verticalLayout_5.addWidget(self.checkBox_masscrit)
        self.checkBox_ignore_old = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_ignore_old.setObjectName("checkBox_ignore_old")
        self.verticalLayout_5.addWidget(self.checkBox_ignore_old)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.doubleSpinBox_hours = QtGui.QDoubleSpinBox(self.groupBox_restrictions)
        self.doubleSpinBox_hours.setDecimals(1)
        self.doubleSpinBox_hours.setMinimum(1.0)
        self.doubleSpinBox_hours.setMaximum(48.0)
        self.doubleSpinBox_hours.setSingleStep(0.5)
        self.doubleSpinBox_hours.setProperty("value", 16.0)
        self.doubleSpinBox_hours.setObjectName("doubleSpinBox_hours")
        self.horizontalLayout_6.addWidget(self.doubleSpinBox_hours)
        self.label_4 = QtGui.QLabel(self.groupBox_restrictions)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addWidget(self.groupBox_restrictions)
        self.groupBox_security = QtGui.QGroupBox(self.groupBox__options)
        self.groupBox_security.setObjectName("groupBox_security")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_security)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_prio_hs = QtGui.QSpinBox(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_prio_hs.sizePolicy().hasHeightForWidth())
        self.spinBox_prio_hs.setSizePolicy(sizePolicy)
        self.spinBox_prio_hs.setStyleSheet("QSpinBox { background-color: #DFF0D8; }")
        self.spinBox_prio_hs.setMinimum(1)
        self.spinBox_prio_hs.setMaximum(100)
        self.spinBox_prio_hs.setObjectName("spinBox_prio_hs")
        self.gridLayout_2.addWidget(self.spinBox_prio_hs, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.spinBox_prio_ns = QtGui.QSpinBox(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_prio_ns.sizePolicy().hasHeightForWidth())
        self.spinBox_prio_ns.setSizePolicy(sizePolicy)
        self.spinBox_prio_ns.setStyleSheet("QSpinBox { background-color: #F2DEDE; }")
        self.spinBox_prio_ns.setMinimum(1)
        self.spinBox_prio_ns.setMaximum(100)
        self.spinBox_prio_ns.setObjectName("spinBox_prio_ns")
        self.gridLayout_2.addWidget(self.spinBox_prio_ns, 2, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.spinBox_prio_wh = QtGui.QSpinBox(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_prio_wh.sizePolicy().hasHeightForWidth())
        self.spinBox_prio_wh.setSizePolicy(sizePolicy)
        self.spinBox_prio_wh.setStyleSheet("QSpinBox { background-color: #D2E2F2; }")
        self.spinBox_prio_wh.setMinimum(1)
        self.spinBox_prio_wh.setMaximum(100)
        self.spinBox_prio_wh.setProperty("value", 1)
        self.spinBox_prio_wh.setObjectName("spinBox_prio_wh")
        self.gridLayout_2.addWidget(self.spinBox_prio_wh, 2, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.spinBox_prio_ls = QtGui.QSpinBox(self.groupBox_security)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_prio_ls.sizePolicy().hasHeightForWidth())
        self.spinBox_prio_ls.setSizePolicy(sizePolicy)
        self.spinBox_prio_ls.setStyleSheet("QSpinBox { background-color: #FCF8E3; }")
        self.spinBox_prio_ls.setMinimum(1)
        self.spinBox_prio_ls.setMaximum(100)
        self.spinBox_prio_ls.setObjectName("spinBox_prio_ls")
        self.gridLayout_2.addWidget(self.spinBox_prio_ls, 1, 3, 1, 1)
        self.checkBox_security_enabled = QtGui.QCheckBox(self.groupBox_security)
        self.checkBox_security_enabled.setObjectName("checkBox_security_enabled")
        self.gridLayout_2.addWidget(self.checkBox_security_enabled, 0, 0, 1, 5)
        self.verticalLayout_3.addWidget(self.groupBox_security)
        self.groupBox_avoidance = QtGui.QGroupBox(self.groupBox__options)
        self.groupBox_avoidance.setObjectName("groupBox_avoidance")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_avoidance)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_avoid_enabled = QtGui.QCheckBox(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_avoid_enabled.sizePolicy().hasHeightForWidth())
        self.checkBox_avoid_enabled.setSizePolicy(sizePolicy)
        self.checkBox_avoid_enabled.setObjectName("checkBox_avoid_enabled")
        self.horizontalLayout_5.addWidget(self.checkBox_avoid_enabled)
        self.label_avoid_status = QtGui.QLabel(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_avoid_status.sizePolicy().hasHeightForWidth())
        self.label_avoid_status.setSizePolicy(sizePolicy)
        self.label_avoid_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_avoid_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_avoid_status.setObjectName("label_avoid_status")
        self.horizontalLayout_5.addWidget(self.label_avoid_status)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_avoid_name = QtGui.QLineEdit(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_avoid_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_avoid_name.setSizePolicy(sizePolicy)
        self.lineEdit_avoid_name.setMaxLength(32)
        self.lineEdit_avoid_name.setObjectName("lineEdit_avoid_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_avoid_name)
        self.pushButton_avoid_add = QtGui.QPushButton(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_avoid_add.sizePolicy().hasHeightForWidth())
        self.pushButton_avoid_add.setSizePolicy(sizePolicy)
        self.pushButton_avoid_add.setMinimumSize(QtCore.QSize(32, 0))
        self.pushButton_avoid_add.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_avoid_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_avoid_add.setObjectName("pushButton_avoid_add")
        self.horizontalLayout_2.addWidget(self.pushButton_avoid_add)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.groupBox_avoidance)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.listWidget_avoid = QtGui.QListWidget(self.groupBox_avoidance)
        self.listWidget_avoid.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_avoid.setObjectName("listWidget_avoid")
        self.verticalLayout_4.addWidget(self.listWidget_avoid)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_avoid_delete = QtGui.QPushButton(self.groupBox_avoidance)
        self.pushButton_avoid_delete.setObjectName("pushButton_avoid_delete")
        self.horizontalLayout_3.addWidget(self.pushButton_avoid_delete)
        self.pushButton_avoid_clear = QtGui.QPushButton(self.groupBox_avoidance)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_avoid_clear.setIcon(icon5)
        self.pushButton_avoid_clear.setObjectName("pushButton_avoid_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_avoid_clear)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_avoidance)
        self.pushButton_reset = QtGui.QPushButton(self.groupBox__options)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.verticalLayout_3.addWidget(self.pushButton_reset)
        self.horizontalLayout.addWidget(self.groupBox__options)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Route planner", None, QtGui.QApplication.UnicodeUTF8))
        self.label_destination.setText(QtGui.QApplication.translate("MainWindow", "Destination:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_source.setText(QtGui.QApplication.translate("MainWindow", "Source:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_player_location.setText(QtGui.QApplication.translate("MainWindow", "Player location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_find_path.setText(QtGui.QApplication.translate("MainWindow", "Find path", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status.setText(QtGui.QApplication.translate("MainWindow", "Path status", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_set_dest.setText(QtGui.QApplication.translate("MainWindow", "Set in-game destination", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "FC, please help!", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_short_format.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "For quick copy-pasting of info", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox__options.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_trip_get.setText(QtGui.QApplication.translate("MainWindow", "Get Tripwire Chain", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_trip_config.setText(QtGui.QApplication.translate("MainWindow", "Tripwire", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crest_config.setText(QtGui.QApplication.translate("MainWindow", "CREST", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_eve_login.setText(QtGui.QApplication.translate("MainWindow", "Log in with EvE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bridge.setText(QtGui.QApplication.translate("MainWindow", "Get Bridge Network", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bridge_conf.setText(QtGui.QApplication.translate("MainWindow", "Bridge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_trip_status.setText(QtGui.QApplication.translate("MainWindow", "Not connected to Tripwire, yet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_evescout_status.setText(QtGui.QApplication.translate("MainWindow", "Eve-Scout", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_restrictions.setTitle(QtGui.QApplication.translate("MainWindow", "Restrictions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Wormhole size at least:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_size.setItemText(0, QtGui.QApplication.translate("MainWindow", "Small [All]", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_size.setItemText(1, QtGui.QApplication.translate("MainWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_size.setItemText(2, QtGui.QApplication.translate("MainWindow", "Large", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_size.setItemText(3, QtGui.QApplication.translate("MainWindow", "X-Large", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_size.setItemText(4, QtGui.QApplication.translate("MainWindow", "[Ignore wormholes]", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_eol.setText(QtGui.QApplication.translate("MainWindow", "Ignore end of life wormholes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_masscrit.setText(QtGui.QApplication.translate("MainWindow", "Ignore critical mass wormholes", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_ignore_old.setText(QtGui.QApplication.translate("MainWindow", "Ignore wormholes updated more than", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "hours ago", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_security.setTitle(QtGui.QApplication.translate("MainWindow", "Security prioritization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "NS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/farshield/shortcircuit/blob/master/README.md#security-prioritization\"><span style=\" text-decoration: underline; color:#0000ff;\">[?]</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "HS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "LS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "WH:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_security_enabled.setText(QtGui.QApplication.translate("MainWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_avoidance.setTitle(QtGui.QApplication.translate("MainWindow", "Avoidance list", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_avoid_enabled.setText(QtGui.QApplication.translate("MainWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_avoid_status.setText(QtGui.QApplication.translate("MainWindow", "Addition status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "System:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_add.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_delete.setText(QtGui.QApplication.translate("MainWindow", "Delete selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear list", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset chain", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
