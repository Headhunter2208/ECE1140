# Form implementation generated from reading ui file 'Track_Configuration.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TrackConfig(object):
    def setupUi(self, TrackConfig):
        TrackConfig.setObjectName("TrackConfig")
        TrackConfig.resize(658, 689)
        self.centralwidget = QtWidgets.QWidget(parent=TrackConfig)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 621, 577))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ladderlogic = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.ladderlogic.setStyleSheet("font: 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 170);")
        self.ladderlogic.setObjectName("ladderlogic")
        self.horizontalLayout_10.addWidget(self.ladderlogic)
        self.functionblocklogic = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.functionblocklogic.setStyleSheet("font: 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 170);")
        self.functionblocklogic.setObjectName("functionblocklogic")
        self.horizontalLayout_10.addWidget(self.functionblocklogic)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pencil.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(41, 31))
        self.label_6.setStyleSheet("font: 700 16pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("parallel.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(41, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("halfcircle.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("slash.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plcdisplay = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.plcdisplay.setText("")
        self.plcdisplay.setPixmap(QtGui.QPixmap("ladderlogic.png"))
        self.plcdisplay.setObjectName("plcdisplay")
        self.verticalLayout.addWidget(self.plcdisplay)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 590, 621, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uploadplc = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.uploadplc.setObjectName("uploadplc")
        self.horizontalLayout_2.addWidget(self.uploadplc)
        self.label_7 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.cancel = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.save = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_4)
        self.save.setObjectName("save")
        self.horizontalLayout_2.addWidget(self.save)
        TrackConfig.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=TrackConfig)
        self.statusbar.setObjectName("statusbar")
        TrackConfig.setStatusBar(self.statusbar)

        self.retranslateUi(TrackConfig)
        self.uploadplc.clicked.connect(TrackConfig.show) # type: ignore
        self.cancel.clicked.connect(TrackConfig.close) # type: ignore
        self.save.clicked.connect(TrackConfig.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TrackConfig)

    def retranslateUi(self, TrackConfig):
        _translate = QtCore.QCoreApplication.translate
        TrackConfig.setWindowTitle(_translate("TrackConfig", "MainWindow"))
        self.ladderlogic.setText(_translate("TrackConfig", "Ladder Logic"))
        self.functionblocklogic.setText(_translate("TrackConfig", "Function Block Logic"))
        self.label_6.setText(_translate("TrackConfig", "T"))
        self.uploadplc.setText(_translate("TrackConfig", "Upload PLC"))
        self.label_7.setText(_translate("TrackConfig", "                                                               "))
        self.cancel.setText(_translate("TrackConfig", "Cancel"))
        self.save.setText(_translate("TrackConfig", "Save"))