# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/robot/Robotics_0_1/mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(398, 338)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.Kd_box = QtGui.QDoubleSpinBox(self.centralWidget)
        self.Kd_box.setGeometry(QtCore.QRect(255, 221, 66, 23))
        self.Kd_box.setMaximum(1000.0)
        self.Kd_box.setObjectName(_fromUtf8("Kd_box"))
        self.Kp_box = QtGui.QDoubleSpinBox(self.centralWidget)
        self.Kp_box.setGeometry(QtCore.QRect(111, 221, 66, 23))
        self.Kp_box.setMaximum(1000.0)
        self.Kp_box.setObjectName(_fromUtf8("Kp_box"))
        self.Kp_label = QtGui.QLabel(self.centralWidget)
        self.Kp_label.setGeometry(QtCore.QRect(120, 200, 31, 16))
        self.Kp_label.setObjectName(_fromUtf8("Kp_label"))
        self.Ki_label = QtGui.QLabel(self.centralWidget)
        self.Ki_label.setGeometry(QtCore.QRect(200, 200, 21, 16))
        self.Ki_label.setObjectName(_fromUtf8("Ki_label"))
        self.Kd_label = QtGui.QLabel(self.centralWidget)
        self.Kd_label.setGeometry(QtCore.QRect(270, 200, 21, 16))
        self.Kd_label.setObjectName(_fromUtf8("Kd_label"))
        self.auto_manual_check = QtGui.QCheckBox(self.centralWidget)
        self.auto_manual_check.setGeometry(QtCore.QRect(120, 70, 101, 20))
        self.auto_manual_check.setChecked(True)
        self.auto_manual_check.setObjectName(_fromUtf8("auto_manual_check"))
        self.motor_speed_slider = QtGui.QSlider(self.centralWidget)
        self.motor_speed_slider.setGeometry(QtCore.QRect(120, 160, 160, 16))
        self.motor_speed_slider.setMaximum(100)
        self.motor_speed_slider.setPageStep(1)
        self.motor_speed_slider.setProperty("value", 10)
        self.motor_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.motor_speed_slider.setObjectName(_fromUtf8("motor_speed_slider"))
        self.motor_up = QtGui.QPushButton(self.centralWidget)
        self.motor_up.setGeometry(QtCore.QRect(110, 100, 80, 22))
        self.motor_up.setObjectName(_fromUtf8("motor_up"))
        self.motor_down = QtGui.QPushButton(self.centralWidget)
        self.motor_down.setGeometry(QtCore.QRect(220, 100, 80, 22))
        self.motor_down.setObjectName(_fromUtf8("motor_down"))
        self.motorspeedlabel = QtGui.QLabel(self.centralWidget)
        self.motorspeedlabel.setGeometry(QtCore.QRect(140, 140, 121, 16))
        self.motorspeedlabel.setObjectName(_fromUtf8("motorspeedlabel"))
        self.fasterlabel = QtGui.QLabel(self.centralWidget)
        self.fasterlabel.setGeometry(QtCore.QRect(300, 160, 51, 16))
        self.fasterlabel.setObjectName(_fromUtf8("fasterlabel"))
        self.slowerlabel = QtGui.QLabel(self.centralWidget)
        self.slowerlabel.setGeometry(QtCore.QRect(60, 160, 51, 20))
        self.slowerlabel.setObjectName(_fromUtf8("slowerlabel"))
        self.connectbutton = QtGui.QPushButton(self.centralWidget)
        self.connectbutton.setGeometry(QtCore.QRect(56, 31, 141, 22))
        self.connectbutton.setObjectName(_fromUtf8("connectbutton"))
        self.connectlabel = QtGui.QLabel(self.centralWidget)
        self.connectlabel.setGeometry(QtCore.QRect(204, 31, 101, 16))
        self.connectlabel.setObjectName(_fromUtf8("connectlabel"))
        self.Ki_box = QtGui.QDoubleSpinBox(self.centralWidget)
        self.Ki_box.setGeometry(QtCore.QRect(183, 221, 66, 23))
        self.Ki_box.setMaximum(1000.0)
        self.Ki_box.setObjectName(_fromUtf8("Ki_box"))
        self.Kd_box.raise_()
        self.Kp_box.raise_()
        self.Ki_box.raise_()
        self.Kp_label.raise_()
        self.Ki_label.raise_()
        self.Kd_label.raise_()
        self.auto_manual_check.raise_()
        self.motor_speed_slider.raise_()
        self.motor_up.raise_()
        self.motor_down.raise_()
        self.motorspeedlabel.raise_()
        self.fasterlabel.raise_()
        self.slowerlabel.raise_()
        self.connectbutton.raise_()
        self.Ki_box.raise_()
        self.connectlabel.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 398, 19))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Catching Robot GUI 2017", None))
        self.Kp_label.setText(_translate("MainWindow", "Kp", None))
        self.Ki_label.setText(_translate("MainWindow", "Ki", None))
        self.Kd_label.setText(_translate("MainWindow", "Kd", None))
        self.auto_manual_check.setText(_translate("MainWindow", "Manual", None))
        self.motor_up.setText(_translate("MainWindow", "Up", None))
        self.motor_down.setText(_translate("MainWindow", "Down", None))
        self.motorspeedlabel.setText(_translate("MainWindow", "Adjust Motor Speed", None))
        self.fasterlabel.setText(_translate("MainWindow", "Faster", None))
        self.slowerlabel.setText(_translate("MainWindow", "Slower", None))
        self.connectbutton.setText(_translate("MainWindow", "Connect To Robot", None))
        self.connectlabel.setText(_translate("MainWindow", "Disconnected", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

