from PyQt4 import QtGui, QtTest # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

import gui # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer
import time

class ExampleApp(QtGui.QMainWindow, gui.Ui_MainWindow):  # This class is to interact with the GUI
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        #########  Binds GUI widgets with functions  #####
        self.connectbutton.clicked.connect(self.pushbutton) # Call function "pushbutton" when pressed
        self.motor_up.clicked.connect(self.motorup) # Call function motorup when pressed
        self.motor_down.clicked.connect(self.motordown) # Call function motorup when pressed
        self.motor_speed_slider.valueChanged.connect(self.slider) # Call function slider
        self.auto_manual_check.stateChanged.connect(self.checkbox) # Call function checkbox
        self.Kp_box.valueChanged.connect(self.kp_entry)
        self.Ki_box.valueChanged.connect(self.ki_entry)
        self.Kd_box.valueChanged.connect(self.kd_entry)


        ######### Functions to run when GUI event is encountered

    def pushbutton(self): # stuff to do if connect button is pressed
        self.connectlabel.setText("Connected")
        QtTest.QTest.qWait(2000)        
        self.connectlabel.setText("Disconnected")

    def slider(self): # Stuff to do when slider is changed
        print(self.motor_speed_slider.value()) # Print to monitor

    def motorup(self): # Run if motor up is clicked
        print("motor up")

    def motordown(self): # Run if motor down is clicked
        print("motor down")

    def checkbox(self): # Run if checkbox is changed
        if self.auto_manual_check.isChecked():
            print("is checked")
        else:
            print("unchecked")

    def kp_entry(self): # Run if kp is changed
        print(self.Kp_box.value())

    def ki_entry(self): # Run if ki is changed
        print(self.Ki_box.value())

    def kd_entry(self):# Run if kd is changed
        print(self.Kd_box.value())



def main():  # Function to run the main GUI
    
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
