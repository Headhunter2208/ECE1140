import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Track import Track
import time
from Clock import Clock
from signals import signals

class TrainController(QObject):  

    def __init__(self):
        super().__init__()

        # connect signals
        signals.trainControllerUpdateCurrSpeed.connect(self.updateCurrSpeed)

        self.Ki = 1000
        self.Kp = 1000

        self.UkPrev = 0
        self.EkPrev = 0
        self.T = 1
        self.commandedPower = 0
        self.currentSpeed = 0
        self.train = None

    def updateCurrSpeed(self, train, currSpeed):
        print('current speed updated')
        self.currentSpeed = currSpeed
        self.train = train

    def sendPower(self):
        if self.train.actSpeed == 0:
            self.commandedPower = 120000
        else:
            # velocity error calcuation
            self.ek = self.train.commandedSpeed - self.train.actSpeed

            # calculate uk
            self.uk = self.UkPrev + ((self.T/2) * (self.ek + self.EkPrev))

            self.commandedPower = (self.Kp * self.ek) + (self.Ki * self.uk)

            self.UkPrev = self.uk
            self.EkPrev = self.ek

        if self.commandedPower > 120000:
            self.commandedPower = 120000

        signals.trainModelGetPower.emit(self.train, self.commandedPower)