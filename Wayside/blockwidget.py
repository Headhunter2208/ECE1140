# Form implementation generated from reading ui file 'blockwidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 415)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 455, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.aicon = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.aicon.setMaximumSize(QtCore.QSize(50, 50))
        self.aicon.setText("")
        self.aicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.aicon.setScaledContents(True)
        self.aicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.aicon.setObjectName("aicon")
        self.gridLayout.addWidget(self.aicon, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_8.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.bicon = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.bicon.setMaximumSize(QtCore.QSize(50, 50))
        self.bicon.setText("")
        self.bicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.bicon.setObjectName("bicon")
        self.gridLayout.addWidget(self.bicon, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.cicon = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cicon.setMaximumSize(QtCore.QSize(50, 50))
        self.cicon.setText("")
        self.cicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cicon.setObjectName("cicon")
        self.gridLayout.addWidget(self.cicon, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.sectionname = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.sectionname.setStyleSheet("font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectionname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sectionname.setObjectName("sectionname")
        self.gridLayout.addWidget(self.sectionname, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_9.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.dicon = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.dicon.setMaximumSize(QtCore.QSize(50, 50))
        self.dicon.setText("")
        self.dicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.dicon.setScaledContents(True)
        self.dicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dicon.setObjectName("dicon")
        self.gridLayout.addWidget(self.dicon, 4, 1, 1, 1)
        self.eicon = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.eicon.setMaximumSize(QtCore.QSize(50, 50))
        self.eicon.setText("")
        self.eicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.eicon.setScaledContents(True)
        self.eicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.eicon.setObjectName("eicon")
        self.gridLayout.addWidget(self.eicon, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "4"))
        self.label_6.setText(_translate("Form", "2"))
        self.label_2.setText(_translate("Form", "Occupation"))
        self.sectionname.setText(_translate("Form", "Section A"))
        self.label_3.setText(_translate("Form", "Switch"))
        self.label_4.setText(_translate("Form", "Crossing"))
        self.label_7.setText(_translate("Form", "3"))
        self.label_5.setText(_translate("Form", "1"))
        self.label_9.setText(_translate("Form", "5"))
