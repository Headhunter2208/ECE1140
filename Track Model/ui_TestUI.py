# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(414, 530)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.switchLabel = QLabel(self.centralwidget)
        self.switchLabel.setObjectName(u"switchLabel")
        self.switchLabel.setGeometry(QRect(180, 10, 58, 16))
        self.SwitchBlock = QLabel(self.centralwidget)
        self.SwitchBlock.setObjectName(u"SwitchBlock")
        self.SwitchBlock.setGeometry(QRect(120, 60, 58, 16))
        self.SwitchConn = QLabel(self.centralwidget)
        self.SwitchConn.setObjectName(u"SwitchConn")
        self.SwitchConn.setGeometry(QRect(270, 60, 81, 20))
        self.divider1 = QFrame(self.centralwidget)
        self.divider1.setObjectName(u"divider1")
        self.divider1.setGeometry(QRect(0, 130, 411, 16))
        self.divider1.setFrameShape(QFrame.HLine)
        self.divider1.setFrameShadow(QFrame.Sunken)
        self.RRXing = QLabel(self.centralwidget)
        self.RRXing.setObjectName(u"RRXing")
        self.RRXing.setGeometry(QRect(150, 150, 121, 16))
        self.RRRedLine = QLabel(self.centralwidget)
        self.RRRedLine.setObjectName(u"RRRedLine")
        self.RRRedLine.setGeometry(QRect(60, 180, 121, 16))
        self.RRGreenLine = QLabel(self.centralwidget)
        self.RRGreenLine.setObjectName(u"RRGreenLine")
        self.RRGreenLine.setGeometry(QRect(300, 180, 121, 16))
        self.RedXing = QCheckBox(self.centralwidget)
        self.RedXing.setObjectName(u"RedXing")
        self.RedXing.setGeometry(QRect(50, 210, 85, 20))
        self.GreenXing = QCheckBox(self.centralwidget)
        self.GreenXing.setObjectName(u"GreenXing")
        self.GreenXing.setGeometry(QRect(300, 210, 85, 20))
        self.divider2 = QFrame(self.centralwidget)
        self.divider2.setObjectName(u"divider2")
        self.divider2.setGeometry(QRect(0, 250, 411, 16))
        self.divider2.setFrameShape(QFrame.HLine)
        self.divider2.setFrameShadow(QFrame.Sunken)
        self.OccHeader = QLabel(self.centralwidget)
        self.OccHeader.setObjectName(u"OccHeader")
        self.OccHeader.setGeometry(QRect(160, 270, 121, 16))
        self.OccBlock = QLabel(self.centralwidget)
        self.OccBlock.setObjectName(u"OccBlock")
        self.OccBlock.setGeometry(QRect(130, 300, 58, 16))
        self.SetTo = QLabel(self.centralwidget)
        self.SetTo.setObjectName(u"SetTo")
        self.SetTo.setGeometry(QRect(300, 300, 81, 20))
        self.OccLine = QLabel(self.centralwidget)
        self.OccLine.setObjectName(u"OccLine")
        self.OccLine.setGeometry(QRect(40, 300, 58, 16))
        self.divider3 = QFrame(self.centralwidget)
        self.divider3.setObjectName(u"divider3")
        self.divider3.setGeometry(QRect(0, 370, 411, 16))
        self.divider3.setFrameShape(QFrame.HLine)
        self.divider3.setFrameShadow(QFrame.Sunken)
        self.divider4 = QFrame(self.centralwidget)
        self.divider4.setObjectName(u"divider4")
        self.divider4.setGeometry(QRect(163, 380, 20, 141))
        self.divider4.setFrameShape(QFrame.VLine)
        self.divider4.setFrameShadow(QFrame.Sunken)
        self.TrackHeaters = QLabel(self.centralwidget)
        self.TrackHeaters.setObjectName(u"TrackHeaters")
        self.TrackHeaters.setGeometry(QRect(40, 390, 121, 16))
        self.InduceFault = QLabel(self.centralwidget)
        self.InduceFault.setObjectName(u"InduceFault")
        self.InduceFault.setGeometry(QRect(260, 390, 121, 16))
        self.HeaterStatus = QLabel(self.centralwidget)
        self.HeaterStatus.setObjectName(u"HeaterStatus")
        self.HeaterStatus.setGeometry(QRect(10, 470, 141, 16))
        self.DateTime = QLabel(self.centralwidget)
        self.DateTime.setObjectName(u"DateTime")
        self.DateTime.setGeometry(QRect(10, 500, 141, 16))
        self.tempEntry = QLineEdit(self.centralwidget)
        self.tempEntry.setObjectName(u"tempEntry")
        self.tempEntry.setGeometry(QRect(10, 440, 125, 21))
        self.setOccupied = QPushButton(self.centralwidget)
        self.setOccupied.setObjectName(u"setOccupied")
        self.setOccupied.setGeometry(QRect(250, 320, 71, 32))
        self.setVacant = QPushButton(self.centralwidget)
        self.setVacant.setObjectName(u"setVacant")
        self.setVacant.setGeometry(QRect(330, 320, 71, 32))
        self.SwitchBlockDropDown = QComboBox(self.centralwidget)
        self.SwitchBlockDropDown.setObjectName(u"SwitchBlockDropDown")
        self.SwitchBlockDropDown.setGeometry(QRect(100, 90, 71, 32))
        self.SwitchSec_2 = QLabel(self.centralwidget)
        self.SwitchSec_2.setObjectName(u"SwitchSec_2")
        self.SwitchSec_2.setGeometry(QRect(20, 60, 81, 20))
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(0, 90, 91, 32))
        self.EnterTemp = QPushButton(self.centralwidget)
        self.EnterTemp.setObjectName(u"EnterTemp")
        self.EnterTemp.setGeometry(QRect(20, 410, 100, 31))
        self.OccLineSel = QComboBox(self.centralwidget)
        self.OccLineSel.addItem("")
        self.OccLineSel.addItem("")
        self.OccLineSel.addItem("")
        self.OccLineSel.setObjectName(u"OccLineSel")
        self.OccLineSel.setGeometry(QRect(0, 320, 91, 32))
        self.OccBlockSel = QComboBox(self.centralwidget)
        self.OccBlockSel.setObjectName(u"OccBlockSel")
        self.OccBlockSel.setGeometry(QRect(110, 320, 71, 32))
        self.Connection = QLabel(self.centralwidget)
        self.Connection.setObjectName(u"Connection")
        self.Connection.setGeometry(QRect(240, 90, 121, 20))
        self.Connection.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.switchLabel.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.SwitchBlock.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.SwitchConn.setText(QCoreApplication.translate("MainWindow", u"Connection", None))
        self.RRXing.setText(QCoreApplication.translate("MainWindow", u"Railroad Crossings", None))
        self.RRRedLine.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.RRGreenLine.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedXing.setText(QCoreApplication.translate("MainWindow", u"E-19", None))
        self.GreenXing.setText(QCoreApplication.translate("MainWindow", u"I-47", None))
        self.OccHeader.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.OccBlock.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.SetTo.setText(QCoreApplication.translate("MainWindow", u"Set To:", None))
        self.OccLine.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.TrackHeaters.setText(QCoreApplication.translate("MainWindow", u"Track Heaters", None))
        self.InduceFault.setText(QCoreApplication.translate("MainWindow", u"Induce Fault", None))
        self.HeaterStatus.setText(QCoreApplication.translate("MainWindow", u"Heater Status: ON", None))
        self.DateTime.setText(QCoreApplication.translate("MainWindow", u"Date/Time", None))
        self.setOccupied.setText(QCoreApplication.translate("MainWindow", u"Occupied", None))
        self.setVacant.setText(QCoreApplication.translate("MainWindow", u"Vacant", None))
        self.SwitchSec_2.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.EnterTemp.setText(QCoreApplication.translate("MainWindow", u"Enter Temp", None))
        self.OccLineSel.setItemText(0, QCoreApplication.translate("MainWindow", u"Red", None))
        self.OccLineSel.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.OccLineSel.setItemText(2, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.Connection.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

