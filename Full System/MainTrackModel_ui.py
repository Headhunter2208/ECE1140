# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainTrackModel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RedLineScrollArea = QScrollArea(self.centralwidget)
        self.RedLineScrollArea.setObjectName(u"RedLineScrollArea")
        self.RedLineScrollArea.setGeometry(QRect(0, 120, 411, 481))
        self.RedLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.RedLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels = QWidget()
        self.RedLineLabels.setObjectName(u"RedLineLabels")
        self.RedLineLabels.setGeometry(QRect(0, 0, 409, 479))
        self.RedLineScrollArea.setWidget(self.RedLineLabels)
        self.RedLineLabel = QLabel(self.centralwidget)
        self.RedLineLabel.setObjectName(u"RedLineLabel")
        self.RedLineLabel.setGeometry(QRect(110, 20, 191, 51))
        self.RedLineLabel.setStyleSheet(u"font-size: 20pt")
        self.RedLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineLabel = QLabel(self.centralwidget)
        self.GreenLineLabel.setObjectName(u"GreenLineLabel")
        self.GreenLineLabel.setGeometry(QRect(550, 20, 191, 51))
        self.GreenLineLabel.setStyleSheet(u"font-size: 20pt")
        self.GreenLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineScrollArea = QScrollArea(self.centralwidget)
        self.GreenLineScrollArea.setObjectName(u"GreenLineScrollArea")
        self.GreenLineScrollArea.setGeometry(QRect(440, 120, 411, 481))
        self.GreenLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.GreenLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels_2 = QWidget()
        self.RedLineLabels_2.setObjectName(u"RedLineLabels_2")
        self.RedLineLabels_2.setGeometry(QRect(0, 0, 409, 479))
        self.GreenLineScrollArea.setWidget(self.RedLineLabels_2)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 60, 401, 51))
        self.RedLineHeadersLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.RedLineHeadersLayout.setObjectName(u"RedLineHeadersLayout")
        self.RedLineHeadersLayout.setContentsMargins(0, 0, 0, 0)
        self.RedSection = QLabel(self.horizontalLayoutWidget)
        self.RedSection.setObjectName(u"RedSection")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RedSection.sizePolicy().hasHeightForWidth())
        self.RedSection.setSizePolicy(sizePolicy)
        self.RedSection.setMinimumSize(QSize(75, 0))
        self.RedSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedSection)

        self.RedTrainCount = QLabel(self.horizontalLayoutWidget)
        self.RedTrainCount.setObjectName(u"RedTrainCount")
        sizePolicy.setHeightForWidth(self.RedTrainCount.sizePolicy().hasHeightForWidth())
        self.RedTrainCount.setSizePolicy(sizePolicy)
        self.RedTrainCount.setMinimumSize(QSize(75, 0))
        self.RedTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedTrainCount)

        self.RedOcc = QLabel(self.horizontalLayoutWidget)
        self.RedOcc.setObjectName(u"RedOcc")
        sizePolicy.setHeightForWidth(self.RedOcc.sizePolicy().hasHeightForWidth())
        self.RedOcc.setSizePolicy(sizePolicy)
        self.RedOcc.setMinimumSize(QSize(150, 0))
        self.RedOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedOcc)

        self.RedInfo = QLabel(self.horizontalLayoutWidget)
        self.RedInfo.setObjectName(u"RedInfo")
        sizePolicy.setHeightForWidth(self.RedInfo.sizePolicy().hasHeightForWidth())
        self.RedInfo.setSizePolicy(sizePolicy)
        self.RedInfo.setMinimumSize(QSize(50, 0))
        self.RedInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedInfo)

        self.Spacer1 = QFrame(self.centralwidget)
        self.Spacer1.setObjectName(u"Spacer1")
        self.Spacer1.setGeometry(QRect(420, 0, 16, 601))
        self.Spacer1.setFrameShape(QFrame.VLine)
        self.Spacer1.setFrameShadow(QFrame.Sunken)
        self.Spacer2 = QFrame(self.centralwidget)
        self.Spacer2.setObjectName(u"Spacer2")
        self.Spacer2.setGeometry(QRect(860, 0, 16, 601))
        self.Spacer2.setFrameShape(QFrame.VLine)
        self.Spacer2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(440, 60, 411, 51))
        self.RedLineHeadersLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.RedLineHeadersLayout_2.setObjectName(u"RedLineHeadersLayout_2")
        self.RedLineHeadersLayout_2.setContentsMargins(0, 0, 0, 0)
        self.GreenSection = QLabel(self.horizontalLayoutWidget_3)
        self.GreenSection.setObjectName(u"GreenSection")
        sizePolicy.setHeightForWidth(self.GreenSection.sizePolicy().hasHeightForWidth())
        self.GreenSection.setSizePolicy(sizePolicy)
        self.GreenSection.setMinimumSize(QSize(75, 0))
        self.GreenSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenSection)

        self.GreenTrainCount = QLabel(self.horizontalLayoutWidget_3)
        self.GreenTrainCount.setObjectName(u"GreenTrainCount")
        sizePolicy.setHeightForWidth(self.GreenTrainCount.sizePolicy().hasHeightForWidth())
        self.GreenTrainCount.setSizePolicy(sizePolicy)
        self.GreenTrainCount.setMinimumSize(QSize(75, 0))
        self.GreenTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenTrainCount)

        self.GreenOcc = QLabel(self.horizontalLayoutWidget_3)
        self.GreenOcc.setObjectName(u"GreenOcc")
        sizePolicy.setHeightForWidth(self.GreenOcc.sizePolicy().hasHeightForWidth())
        self.GreenOcc.setSizePolicy(sizePolicy)
        self.GreenOcc.setMinimumSize(QSize(150, 0))
        self.GreenOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenOcc)

        self.GreenInfo = QLabel(self.horizontalLayoutWidget_3)
        self.GreenInfo.setObjectName(u"GreenInfo")
        sizePolicy.setHeightForWidth(self.GreenInfo.sizePolicy().hasHeightForWidth())
        self.GreenInfo.setSizePolicy(sizePolicy)
        self.GreenInfo.setMinimumSize(QSize(50, 0))
        self.GreenInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenInfo)

        self.GeneralInfoLabel = QLabel(self.centralwidget)
        self.GeneralInfoLabel.setObjectName(u"GeneralInfoLabel")
        self.GeneralInfoLabel.setGeometry(QRect(920, 0, 191, 51))
        self.GeneralInfoLabel.setStyleSheet(u"font-size: 20pt")
        self.GeneralInfoLabel.setAlignment(Qt.AlignCenter)
        self.DateTimeLabel = QLabel(self.centralwidget)
        self.DateTimeLabel.setObjectName(u"DateTimeLabel")
        self.DateTimeLabel.setGeometry(QRect(880, 60, 71, 20))
        self.GreenLineGenInfo = QLabel(self.centralwidget)
        self.GreenLineGenInfo.setObjectName(u"GreenLineGenInfo")
        self.GreenLineGenInfo.setGeometry(QRect(1020, 90, 120, 50))
        self.GreenLineGenInfo.setStyleSheet(u"font-size: 20pt;\n"
"background-color: #00b321;\n"
"font-weight: bold")
        self.GreenLineGenInfo.setAlignment(Qt.AlignCenter)
        self.RedLineGenInfo = QLabel(self.centralwidget)
        self.RedLineGenInfo.setObjectName(u"RedLineGenInfo")
        self.RedLineGenInfo.setGeometry(QRect(880, 90, 120, 50))
        self.RedLineGenInfo.setStyleSheet(u"font-size: 20pt;\n"
"background-color: #FF0000;\n"
"font-weight: bold")
        self.RedLineGenInfo.setAlignment(Qt.AlignCenter)
        self.GeneralInfoSpacer = QFrame(self.centralwidget)
        self.GeneralInfoSpacer.setObjectName(u"GeneralInfoSpacer")
        self.GeneralInfoSpacer.setGeometry(QRect(1000, 90, 20, 471))
        self.GeneralInfoSpacer.setFrameShape(QFrame.VLine)
        self.GeneralInfoSpacer.setFrameShadow(QFrame.Sunken)
        self.TotalTrainCountLabel = QLabel(self.centralwidget)
        self.TotalTrainCountLabel.setObjectName(u"TotalTrainCountLabel")
        self.TotalTrainCountLabel.setGeometry(QRect(920, 380, 191, 21))
        self.TotalTrainCountLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.TotalTrainCountLabel.setAlignment(Qt.AlignCenter)
        self.RedTrainCt = QLabel(self.centralwidget)
        self.RedTrainCt.setObjectName(u"RedTrainCt")
        self.RedTrainCt.setGeometry(QRect(910, 410, 58, 16))
        self.RedTrainCt.setAlignment(Qt.AlignCenter)
        self.GreenTrainCt = QLabel(self.centralwidget)
        self.GreenTrainCt.setObjectName(u"GreenTrainCt")
        self.GreenTrainCt.setGeometry(QRect(1050, 410, 58, 16))
        self.GreenTrainCt.setAlignment(Qt.AlignCenter)
        self.RRXingLabel = QLabel(self.centralwidget)
        self.RRXingLabel.setObjectName(u"RRXingLabel")
        self.RRXingLabel.setGeometry(QRect(920, 430, 191, 21))
        self.RRXingLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.RRXingLabel.setAlignment(Qt.AlignCenter)
        self.I47 = QLabel(self.centralwidget)
        self.I47.setObjectName(u"I47")
        self.I47.setGeometry(QRect(880, 470, 31, 16))
        self.E19 = QLabel(self.centralwidget)
        self.E19.setObjectName(u"E19")
        self.E19.setGeometry(QRect(1020, 470, 31, 16))
        self.I47Status = QLabel(self.centralwidget)
        self.I47Status.setObjectName(u"I47Status")
        self.I47Status.setGeometry(QRect(917, 470, 81, 20))
        self.I47Status.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.I47Status.setAlignment(Qt.AlignCenter)
        self.E19Status = QLabel(self.centralwidget)
        self.E19Status.setObjectName(u"E19Status")
        self.E19Status.setGeometry(QRect(1060, 470, 81, 20))
        self.E19Status.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.E19Status.setAlignment(Qt.AlignCenter)
        self.UploadTrack = QPushButton(self.centralwidget)
        self.UploadTrack.setObjectName(u"UploadTrack")
        self.UploadTrack.setGeometry(QRect(880, 620, 261, 32))
        self.TrackHeatersLabel = QLabel(self.centralwidget)
        self.TrackHeatersLabel.setObjectName(u"TrackHeatersLabel")
        self.TrackHeatersLabel.setGeometry(QRect(920, 500, 191, 21))
        self.TrackHeatersLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.TrackHeatersLabel.setAlignment(Qt.AlignCenter)
        self.FaultsLabel = QLabel(self.centralwidget)
        self.FaultsLabel.setObjectName(u"FaultsLabel")
        self.FaultsLabel.setGeometry(QRect(920, 560, 191, 21))
        self.FaultsLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.FaultsLabel.setAlignment(Qt.AlignCenter)
        self.CurrentTempLabel = QLabel(self.centralwidget)
        self.CurrentTempLabel.setObjectName(u"CurrentTempLabel")
        self.CurrentTempLabel.setGeometry(QRect(880, 530, 121, 20))
        self.HeaterStatus = QLabel(self.centralwidget)
        self.HeaterStatus.setObjectName(u"HeaterStatus")
        self.HeaterStatus.setGeometry(QRect(1040, 530, 81, 20))
        self.HeaterStatus.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.HeaterStatus.setAlignment(Qt.AlignCenter)
        self.FaultSpacer1 = QFrame(self.centralwidget)
        self.FaultSpacer1.setObjectName(u"FaultSpacer1")
        self.FaultSpacer1.setGeometry(QRect(910, 580, 20, 41))
        self.FaultSpacer1.setFrameShape(QFrame.VLine)
        self.FaultSpacer1.setFrameShadow(QFrame.Sunken)
        self.FaultSpacer2 = QFrame(self.centralwidget)
        self.FaultSpacer2.setObjectName(u"FaultSpacer2")
        self.FaultSpacer2.setGeometry(QRect(1000, 580, 20, 41))
        self.FaultSpacer2.setFrameShape(QFrame.VLine)
        self.FaultSpacer2.setFrameShadow(QFrame.Sunken)
        self.PowerFaultLabel = QLabel(self.centralwidget)
        self.PowerFaultLabel.setObjectName(u"PowerFaultLabel")
        self.PowerFaultLabel.setGeometry(QRect(870, 590, 41, 20))
        self.PowerFaultLabel.setAlignment(Qt.AlignCenter)
        self.BrokenRailLabel = QLabel(self.centralwidget)
        self.BrokenRailLabel.setObjectName(u"BrokenRailLabel")
        self.BrokenRailLabel.setGeometry(QRect(920, 590, 91, 20))
        self.BrokenRailLabel.setAlignment(Qt.AlignCenter)
        self.BrokenCircuitLabel = QLabel(self.centralwidget)
        self.BrokenCircuitLabel.setObjectName(u"BrokenCircuitLabel")
        self.BrokenCircuitLabel.setGeometry(QRect(1010, 590, 101, 20))
        self.BrokenCircuitLabel.setAlignment(Qt.AlignCenter)
        self.FaultWindowButton = QPushButton(self.centralwidget)
        self.FaultWindowButton.setObjectName(u"FaultWindowButton")
        self.FaultWindowButton.setGeometry(QRect(1110, 590, 41, 32))
        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(957, 60, 181, 20))
        self.tempEntry = QLineEdit(self.centralwidget)
        self.tempEntry.setObjectName(u"tempEntry")
        self.tempEntry.setGeometry(QRect(10, 630, 113, 21))
        self.tempLabel = QLabel(self.centralwidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(10, 610, 131, 16))
        self.tempGo = QPushButton(self.centralwidget)
        self.tempGo.setObjectName(u"tempGo")
        self.tempGo.setGeometry(QRect(130, 620, 71, 32))
        self.Spacer3 = QFrame(self.centralwidget)
        self.Spacer3.setObjectName(u"Spacer3")
        self.Spacer3.setGeometry(QRect(210, 600, 3, 61))
        self.Spacer3.setFrameShape(QFrame.VLine)
        self.Spacer3.setFrameShadow(QFrame.Sunken)
        self.brokenRailButton = QPushButton(self.centralwidget)
        self.brokenRailButton.setObjectName(u"brokenRailButton")
        self.brokenRailButton.setGeometry(QRect(620, 620, 91, 32))
        self.powerFailure = QPushButton(self.centralwidget)
        self.powerFailure.setObjectName(u"powerFailure")
        self.powerFailure.setGeometry(QRect(400, 620, 101, 32))
        self.circuitFailure = QPushButton(self.centralwidget)
        self.circuitFailure.setObjectName(u"circuitFailure")
        self.circuitFailure.setGeometry(QRect(510, 620, 101, 32))
        self.brokenRailLineLabel = QLabel(self.centralwidget)
        self.brokenRailLineLabel.setObjectName(u"brokenRailLineLabel")
        self.brokenRailLineLabel.setGeometry(QRect(250, 610, 31, 20))
        self.brokenRailBlockLabel = QLabel(self.centralwidget)
        self.brokenRailBlockLabel.setObjectName(u"brokenRailBlockLabel")
        self.brokenRailBlockLabel.setGeometry(QRect(330, 610, 58, 16))
        self.brokenRailLineSelect = QComboBox(self.centralwidget)
        self.brokenRailLineSelect.setObjectName(u"brokenRailLineSelect")
        self.brokenRailLineSelect.setGeometry(QRect(220, 630, 91, 32))
        self.brokenRailBlockSelect = QComboBox(self.centralwidget)
        self.brokenRailBlockSelect.setObjectName(u"brokenRailBlockSelect")
        self.brokenRailBlockSelect.setGeometry(QRect(310, 630, 71, 32))
        self.fixButton = QPushButton(self.centralwidget)
        self.fixButton.setObjectName(u"fixButton")
        self.fixButton.setGeometry(QRect(770, 620, 91, 32))
        self.SwitchHeading = QLabel(self.centralwidget)
        self.SwitchHeading.setObjectName(u"SwitchHeading")
        self.SwitchHeading.setGeometry(QRect(920, 150, 191, 21))
        self.SwitchHeading.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.SwitchHeading.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(890, 180, 21, 20))
        self.R1 = QLabel(self.centralwidget)
        self.R1.setObjectName(u"R1")
        self.R1.setGeometry(QRect(930, 180, 21, 20))
        self.R1.setStyleSheet(u"color: orange")
        self.R15 = QLabel(self.centralwidget)
        self.R15.setObjectName(u"R15")
        self.R15.setGeometry(QRect(960, 180, 21, 20))
        self.R76 = QLabel(self.centralwidget)
        self.R76.setObjectName(u"R76")
        self.R76.setGeometry(QRect(960, 210, 21, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(890, 210, 21, 20))
        self.R28 = QLabel(self.centralwidget)
        self.R28.setObjectName(u"R28")
        self.R28.setGeometry(QRect(930, 210, 21, 20))
        self.R28.setStyleSheet(u"color: orange")
        self.R72 = QLabel(self.centralwidget)
        self.R72.setObjectName(u"R72")
        self.R72.setGeometry(QRect(960, 240, 21, 20))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(890, 240, 21, 20))
        self.R32 = QLabel(self.centralwidget)
        self.R32.setObjectName(u"R32")
        self.R32.setGeometry(QRect(930, 240, 21, 20))
        self.R32.setStyleSheet(u"color: orange")
        self.R71 = QLabel(self.centralwidget)
        self.R71.setObjectName(u"R71")
        self.R71.setGeometry(QRect(960, 270, 21, 20))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(890, 270, 21, 20))
        self.R39 = QLabel(self.centralwidget)
        self.R39.setObjectName(u"R39")
        self.R39.setGeometry(QRect(930, 270, 21, 20))
        self.R39.setStyleSheet(u"color: orange")
        self.R67 = QLabel(self.centralwidget)
        self.R67.setObjectName(u"R67")
        self.R67.setGeometry(QRect(960, 300, 21, 20))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(890, 300, 21, 20))
        self.R43 = QLabel(self.centralwidget)
        self.R43.setObjectName(u"R43")
        self.R43.setGeometry(QRect(930, 300, 21, 20))
        self.R43.setStyleSheet(u"color: orange")
        self.R66 = QLabel(self.centralwidget)
        self.R66.setObjectName(u"R66")
        self.R66.setGeometry(QRect(960, 330, 21, 20))
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(890, 330, 21, 20))
        self.R53 = QLabel(self.centralwidget)
        self.R53.setObjectName(u"R53")
        self.R53.setGeometry(QRect(930, 330, 21, 20))
        self.R53.setStyleSheet(u"color: orange")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(1030, 270, 21, 20))
        self.G12 = QLabel(self.centralwidget)
        self.G12.setObjectName(u"G12")
        self.G12.setGeometry(QRect(1100, 180, 21, 20))
        self.GYard57 = QLabel(self.centralwidget)
        self.GYard57.setObjectName(u"GYard57")
        self.GYard57.setGeometry(QRect(1060, 300, 31, 20))
        self.GYard57.setStyleSheet(u"color: orange")
        self.G100 = QLabel(self.centralwidget)
        self.G100.setObjectName(u"G100")
        self.G100.setGeometry(QRect(1100, 270, 21, 20))
        self.G76 = QLabel(self.centralwidget)
        self.G76.setObjectName(u"G76")
        self.G76.setGeometry(QRect(1070, 240, 21, 20))
        self.G76.setStyleSheet(u"color: orange")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(1030, 300, 21, 20))
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(1030, 180, 21, 20))
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(1030, 240, 21, 20))
        self.G30 = QLabel(self.centralwidget)
        self.G30.setObjectName(u"G30")
        self.G30.setGeometry(QRect(1070, 210, 21, 20))
        self.G30.setStyleSheet(u"color: orange")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(1030, 210, 21, 20))
        self.G1 = QLabel(self.centralwidget)
        self.G1.setObjectName(u"G1")
        self.G1.setGeometry(QRect(1070, 180, 21, 20))
        self.G1.setStyleSheet(u"color: orange")
        self.G86 = QLabel(self.centralwidget)
        self.G86.setObjectName(u"G86")
        self.G86.setGeometry(QRect(1070, 270, 21, 20))
        self.G86.setStyleSheet(u"color: orange")
        self.G150 = QLabel(self.centralwidget)
        self.G150.setObjectName(u"G150")
        self.G150.setGeometry(QRect(1100, 210, 21, 20))
        self.G58 = QLabel(self.centralwidget)
        self.G58.setObjectName(u"G58")
        self.G58.setGeometry(QRect(1100, 300, 21, 20))
        self.G101 = QLabel(self.centralwidget)
        self.G101.setObjectName(u"G101")
        self.G101.setGeometry(QRect(1100, 240, 21, 20))
        self.G62 = QLabel(self.centralwidget)
        self.G62.setObjectName(u"G62")
        self.G62.setGeometry(QRect(1100, 330, 21, 20))
        self.GYard63 = QLabel(self.centralwidget)
        self.GYard63.setObjectName(u"GYard63")
        self.GYard63.setGeometry(QRect(1060, 330, 31, 20))
        self.GYard63.setStyleSheet(u"color: orange")
        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(1030, 330, 21, 20))
        self.RedYard = QLabel(self.centralwidget)
        self.RedYard.setObjectName(u"RedYard")
        self.RedYard.setGeometry(QRect(920, 350, 31, 20))
        self.RedYard.setStyleSheet(u"color: orange")
        self.R10 = QLabel(self.centralwidget)
        self.R10.setObjectName(u"R10")
        self.R10.setGeometry(QRect(960, 350, 21, 20))
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(890, 350, 21, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.GeneralInfoSpacer.raise_()
        self.RedLineScrollArea.raise_()
        self.RedLineLabel.raise_()
        self.GreenLineLabel.raise_()
        self.GreenLineScrollArea.raise_()
        self.horizontalLayoutWidget.raise_()
        self.Spacer1.raise_()
        self.Spacer2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.GeneralInfoLabel.raise_()
        self.DateTimeLabel.raise_()
        self.GreenLineGenInfo.raise_()
        self.RedLineGenInfo.raise_()
        self.TotalTrainCountLabel.raise_()
        self.RedTrainCt.raise_()
        self.GreenTrainCt.raise_()
        self.RRXingLabel.raise_()
        self.I47.raise_()
        self.E19.raise_()
        self.I47Status.raise_()
        self.E19Status.raise_()
        self.UploadTrack.raise_()
        self.TrackHeatersLabel.raise_()
        self.FaultsLabel.raise_()
        self.CurrentTempLabel.raise_()
        self.HeaterStatus.raise_()
        self.FaultSpacer1.raise_()
        self.FaultSpacer2.raise_()
        self.PowerFaultLabel.raise_()
        self.BrokenRailLabel.raise_()
        self.BrokenCircuitLabel.raise_()
        self.FaultWindowButton.raise_()
        self.time.raise_()
        self.tempEntry.raise_()
        self.tempLabel.raise_()
        self.tempGo.raise_()
        self.Spacer3.raise_()
        self.brokenRailButton.raise_()
        self.powerFailure.raise_()
        self.circuitFailure.raise_()
        self.brokenRailLineLabel.raise_()
        self.brokenRailBlockLabel.raise_()
        self.brokenRailLineSelect.raise_()
        self.brokenRailBlockSelect.raise_()
        self.fixButton.raise_()
        self.SwitchHeading.raise_()
        self.label.raise_()
        self.R1.raise_()
        self.R15.raise_()
        self.R76.raise_()
        self.label_5.raise_()
        self.R28.raise_()
        self.R72.raise_()
        self.label_8.raise_()
        self.R32.raise_()
        self.R71.raise_()
        self.label_11.raise_()
        self.R39.raise_()
        self.R67.raise_()
        self.label_14.raise_()
        self.R43.raise_()
        self.R66.raise_()
        self.label_17.raise_()
        self.R53.raise_()
        self.label_19.raise_()
        self.G12.raise_()
        self.GYard57.raise_()
        self.G100.raise_()
        self.G76.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.G30.raise_()
        self.label_29.raise_()
        self.G1.raise_()
        self.G86.raise_()
        self.G150.raise_()
        self.G58.raise_()
        self.G101.raise_()
        self.G62.raise_()
        self.GYard63.raise_()
        self.label_39.raise_()
        self.RedYard.raise_()
        self.R10.raise_()
        self.label_30.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RedLineLabel.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.GreenLineLabel.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.RedTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.RedOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.RedInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.GreenSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.GreenTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.GreenOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.GreenInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.GeneralInfoLabel.setText(QCoreApplication.translate("MainWindow", u"General Info", None))
        self.DateTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Date/Time:", None))
        self.GreenLineGenInfo.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedLineGenInfo.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.TotalTrainCountLabel.setText(QCoreApplication.translate("MainWindow", u"Total Trains Active", None))
        self.RedTrainCt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GreenTrainCt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RRXingLabel.setText(QCoreApplication.translate("MainWindow", u"RR Crossings", None))
        self.I47.setText(QCoreApplication.translate("MainWindow", u"I-47:", None))
        self.E19.setText(QCoreApplication.translate("MainWindow", u"E-19", None))
        self.I47Status.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.E19Status.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.UploadTrack.setText(QCoreApplication.translate("MainWindow", u"Upload Track Layout", None))
        self.TrackHeatersLabel.setText(QCoreApplication.translate("MainWindow", u"Track Heaters", None))
        self.FaultsLabel.setText(QCoreApplication.translate("MainWindow", u"Faults", None))
        self.CurrentTempLabel.setText(QCoreApplication.translate("MainWindow", u"Current Temp:", None))
        self.HeaterStatus.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.PowerFaultLabel.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.BrokenRailLabel.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.BrokenCircuitLabel.setText(QCoreApplication.translate("MainWindow", u"Broken Circuit", None))
        self.FaultWindowButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.time.setText("")
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Temperature:", None))
        self.tempGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.brokenRailButton.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.powerFailure.setText(QCoreApplication.translate("MainWindow", u"Power Failure", None))
        self.circuitFailure.setText(QCoreApplication.translate("MainWindow", u"Circuit Failure", None))
        self.brokenRailLineLabel.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.brokenRailBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.fixButton.setText(QCoreApplication.translate("MainWindow", u"Fix All Faults", None))
        self.SwitchHeading.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.R1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.R15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.R76.setText(QCoreApplication.translate("MainWindow", u"76", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.R28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.R72.setText(QCoreApplication.translate("MainWindow", u"72", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.R32.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.R71.setText(QCoreApplication.translate("MainWindow", u"71", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.R39.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.R67.setText(QCoreApplication.translate("MainWindow", u"67", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.R43.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.R66.setText(QCoreApplication.translate("MainWindow", u"66", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"52", None))
        self.R53.setText(QCoreApplication.translate("MainWindow", u"53", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"85", None))
        self.G12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.GYard57.setText(QCoreApplication.translate("MainWindow", u"Yard", None))
        self.G100.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.G76.setText(QCoreApplication.translate("MainWindow", u"76", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"77", None))
        self.G30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.G1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.G86.setText(QCoreApplication.translate("MainWindow", u"86", None))
        self.G150.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.G58.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.G101.setText(QCoreApplication.translate("MainWindow", u"101", None))
        self.G62.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.GYard63.setText(QCoreApplication.translate("MainWindow", u"Yard", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.RedYard.setText(QCoreApplication.translate("MainWindow", u"Yard", None))
        self.R10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"9", None))
    # retranslateUi

