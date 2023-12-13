# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designwWnhCD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UpperPCGUI(object):
    def setupUi(self, UpperPCGUI):
        if not UpperPCGUI.objectName():
            UpperPCGUI.setObjectName(u"UpperPCGUI")
        UpperPCGUI.resize(900, 631)
        UpperPCGUI.setMinimumSize(QSize(900, 0))
        self.centralwidget = QWidget(UpperPCGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 20))
        self.tabWidget.setSizeIncrement(QSize(0, 20))
        self.tabWidget.setStyleSheet(u"color=rgb(0, 170, 255)")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.Main = QWidget()
        self.Main.setObjectName(u"Main")
        self.gridLayout_2 = QGridLayout(self.Main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 8, 0, 1, 1)

        self.line1 = QFrame(self.Main)
        self.line1.setObjectName(u"line1")
        self.line1.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        self.line1.setMinimumSize(QSize(5, 5))
        self.line1.setSizeIncrement(QSize(0, 5))
        self.line1.setBaseSize(QSize(0, 5))
        self.line1.setStyleSheet(u"color:#00aaff;")
        self.line1.setLineWidth(5)
        self.line1.setMidLineWidth(5)
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line1, 7, 0, 1, 1)

        self.line0 = QFrame(self.Main)
        self.line0.setObjectName(u"line0")
        self.line0.setStyleSheet(u"color:#00aaff;")
        self.line0.setFrameShape(QFrame.HLine)
        self.line0.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line0, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Pressure_label = QLabel(self.Main)
        self.Pressure_label.setObjectName(u"Pressure_label")
        self.Pressure_label.setLayoutDirection(Qt.LeftToRight)
        self.Pressure_label.setTextFormat(Qt.AutoText)
        self.Pressure_label.setScaledContents(False)
        self.Pressure_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.Pressure_label)

        self.Pressure_value = QLCDNumber(self.Main)
        self.Pressure_value.setObjectName(u"Pressure_value")
        self.Pressure_value.setSmallDecimalPoint(False)

        self.horizontalLayout.addWidget(self.Pressure_value)

        self.Pressure_units = QLabel(self.Main)
        self.Pressure_units.setObjectName(u"Pressure_units")

        self.horizontalLayout.addWidget(self.Pressure_units)

        self.Temp_label = QLabel(self.Main)
        self.Temp_label.setObjectName(u"Temp_label")
        self.Temp_label.setTextFormat(Qt.RichText)
        self.Temp_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.Temp_label)

        self.Temp_value = QLCDNumber(self.Main)
        self.Temp_value.setObjectName(u"Temp_value")

        self.horizontalLayout.addWidget(self.Temp_value)

        self.Temp_units = QLabel(self.Main)
        self.Temp_units.setObjectName(u"Temp_units")

        self.horizontalLayout.addWidget(self.Temp_units)

        self.Depth_label = QLabel(self.Main)
        self.Depth_label.setObjectName(u"Depth_label")
        self.Depth_label.setTextFormat(Qt.RichText)
        self.Depth_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Depth_label.setWordWrap(False)
        self.Depth_label.setMargin(1)

        self.horizontalLayout.addWidget(self.Depth_label)

        self.Depth_value = QLCDNumber(self.Main)
        self.Depth_value.setObjectName(u"Depth_value")

        self.horizontalLayout.addWidget(self.Depth_value)

        self.Depth_units = QLabel(self.Main)
        self.Depth_units.setObjectName(u"Depth_units")

        self.horizontalLayout.addWidget(self.Depth_units)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 15, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 9, 0, 1, 1)

        self.Sensors0_label = QLabel(self.Main)
        self.Sensors0_label.setObjectName(u"Sensors0_label")

        self.gridLayout_2.addWidget(self.Sensors0_label, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)

        self.tabWidget.addTab(self.Main, "")
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.gridLayout = QGridLayout(self.Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.Settings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.record_start = QPushButton(self.Settings)
        self.record_start.setObjectName(u"record_start")

        self.horizontalLayout_4.addWidget(self.record_start)

        self.record_stop = QPushButton(self.Settings)
        self.record_stop.setObjectName(u"record_stop")

        self.horizontalLayout_4.addWidget(self.record_stop)

        self.record_path = QLabel(self.Settings)
        self.record_path.setObjectName(u"record_path")

        self.horizontalLayout_4.addWidget(self.record_path)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 2, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Serialconn = QRadioButton(self.Settings)
        self.Serialconn.setObjectName(u"Serialconn")
        self.Serialconn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.Serialconn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.Settings)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.serial_port_box = QComboBox(self.Settings)
        self.serial_port_box.setObjectName(u"serial_port_box")

        self.horizontalLayout_6.addWidget(self.serial_port_box)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_2 = QLabel(self.Settings)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.serial_baudrate_box = QComboBox(self.Settings)
        self.serial_baudrate_box.setObjectName(u"serial_baudrate_box")

        self.horizontalLayout_6.addWidget(self.serial_baudrate_box)

        self.serial_update = QPushButton(self.Settings)
        self.serial_update.setObjectName(u"serial_update")

        self.horizontalLayout_6.addWidget(self.serial_update)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.line = QFrame(self.Settings)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color:#00aaff;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.line_2 = QFrame(self.Settings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color:#00aaff;\n"
"")
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 1)

        self.label_5 = QLabel(self.Settings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.UDPconn = QRadioButton(self.Settings)
        self.UDPconn.setObjectName(u"UDPconn")

        self.horizontalLayout_5.addWidget(self.UDPconn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.Settings)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.UDP_IP_box = QComboBox(self.Settings)
        self.UDP_IP_box.setObjectName(u"UDP_IP_box")

        self.horizontalLayout_5.addWidget(self.UDP_IP_box)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_4 = QLabel(self.Settings)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.UDP_port_box = QComboBox(self.Settings)
        self.UDP_port_box.setObjectName(u"UDP_port_box")

        self.horizontalLayout_5.addWidget(self.UDP_port_box)

        self.UDP_update = QPushButton(self.Settings)
        self.UDP_update.setObjectName(u"UDP_update")

        self.horizontalLayout_5.addWidget(self.UDP_update)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 7, 0, 1, 1)

        self.tabWidget.addTab(self.Settings, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        UpperPCGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpperPCGUI)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(UpperPCGUI)
    # setupUi

    def retranslateUi(self, UpperPCGUI):
        UpperPCGUI.setWindowTitle(QCoreApplication.translate("UpperPCGUI", u"UpperPCGUI", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("UpperPCGUI", u"<span style=\" font-size:18pt; font-weight:600; color:#00aaff;\">", None))
#endif // QT_CONFIG(tooltip)
        self.Pressure_label.setText(QCoreApplication.translate("UpperPCGUI", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; color:#00aaff;\">Pressure</span></p></body></html>", None))
        self.Pressure_units.setText(QCoreApplication.translate("UpperPCGUI", u"<html><head/><body><p align=\"left\"><span style=\" font-size:16pt; font-weight:600; color:#00aaff;\">mbar</span></p></body></html>", None))
        self.Temp_label.setText(QCoreApplication.translate("UpperPCGUI", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; color:#00aaff;\">Temp</span></p></body></html>", None))
        self.Temp_units.setText(QCoreApplication.translate("UpperPCGUI", u"\n"
"<html><head/><body><p align=\"left\"><span style=\" font-size:16pt; font-weight:600; color:#00aaff;\">C</span></p></body></html>", None))
        self.Depth_label.setText(QCoreApplication.translate("UpperPCGUI", u"<html><head/><body><p align=\"right\"><span style=\" font-size:18pt; font-weight:600; color:#00aaff;\">Depth</span></p></body></html>", None))
        self.Depth_units.setText(QCoreApplication.translate("UpperPCGUI", u"\n"
"<html><head/><body><p align=\"left\"><span style=\" font-size:16pt; font-weight:600; color:#00aaff;\">m</span></p></body></html>", None))
        self.Sensors0_label.setText(QCoreApplication.translate("UpperPCGUI", u"<html><head/><body><p align=\"left\"><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">Sensor 0</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), QCoreApplication.translate("UpperPCGUI", u"Main", None))
        self.label_6.setText(QCoreApplication.translate("UpperPCGUI", u"\n"
"<html><head/><body><p align=\"left\"><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">Settings serial port </span></p></body></html>", None))
        self.record_start.setText(QCoreApplication.translate("UpperPCGUI", u"Start", None))
        self.record_stop.setText(QCoreApplication.translate("UpperPCGUI", u"Stop", None))
        self.record_path.setText(QCoreApplication.translate("UpperPCGUI", u"Name: ", None))
        self.Serialconn.setText(QCoreApplication.translate("UpperPCGUI", u"Serial connection", None))
        self.label.setText(QCoreApplication.translate("UpperPCGUI", u" Port", None))
        self.label_2.setText(QCoreApplication.translate("UpperPCGUI", u"Baudrate", None))
        self.serial_update.setText(QCoreApplication.translate("UpperPCGUI", u"Update", None))
        self.label_5.setText(QCoreApplication.translate("UpperPCGUI", u"\n"
"<html><head/><body><p align=\"left\"><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">Recording data</span></p></body></html>", None))
        self.UDPconn.setText(QCoreApplication.translate("UpperPCGUI", u"UDP connection  ", None))
        self.label_3.setText(QCoreApplication.translate("UpperPCGUI", u"IP address", None))
        self.label_4.setText(QCoreApplication.translate("UpperPCGUI", u"Port", None))
        self.UDP_update.setText(QCoreApplication.translate("UpperPCGUI", u"Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), QCoreApplication.translate("UpperPCGUI", u"Settings", None))
    # retranslateUi

