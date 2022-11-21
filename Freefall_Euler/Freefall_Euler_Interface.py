

import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
    
        ####Defining entry fields. QDoubleSpinBox is incredibly handy, as it comes with built in validation as default####

        self.HeightEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.HeightEntry.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.HeightEntry.setObjectName("HeightEntry")
        self.HeightEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.HeightEntry.setMaximum(10000000)
        self.HeightEntry.setValue(1000)
        
        self.TimeEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.TimeEntry.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.TimeEntry.setObjectName("TimeEntry")
        self.TimeEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TimeEntry.setMaximum(10000000)
        self.TimeEntry.setValue(0.1)
        
        self.DensityEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.DensityEntry.setGeometry(QtCore.QRect(110, 110, 113, 20))
        self.DensityEntry.setObjectName("DensityEntry")
        self.DensityEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DensityEntry.setMaximum(10000000)
        self.DensityEntry.setValue(1.2)
        
        self.CrossSectionEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.CrossSectionEntry.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.CrossSectionEntry.setObjectName("CrossSectionEntry")
        self.CrossSectionEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.CrossSectionEntry.setMaximum(10000000)
        self.CrossSectionEntry.setValue(0.7)
        
        self.DragEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.DragEntry.setGeometry(QtCore.QRect(110, 170, 113, 20))
        self.DragEntry.setObjectName("DragEntry")
        self.DragEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.DragEntry.setMaximum(10000000)
        self.DragEntry.setValue(1.3)
        
        self.MassEntry = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.MassEntry.setGeometry(QtCore.QRect(110, 200, 113, 20))
        self.MassEntry.setObjectName("MassEntry")
        self.MassEntry.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.MassEntry.setMaximum(10000000)
        self.MassEntry.setValue(108) 
        
        ####Selection checkboxes for the various iteration algorithms####

        self.VariableDensityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.VariableDensityCheckBox.setGeometry(QtCore.QRect(260, 130, 111, 17))
        self.VariableDensityCheckBox.setObjectName("VariableDensityCheckBox")
        
        self.EulerCheckBox = QtWidgets.QRadioButton(self.centralwidget)
        self.EulerCheckBox.setGeometry(QtCore.QRect(260, 50, 70, 17))
        self.EulerCheckBox.setObjectName("EulerCheckBox")
        self.EulerCheckBox.setChecked(True)
        
        self.ModifiedCheckBox = QtWidgets.QRadioButton(self.centralwidget)
        self.ModifiedCheckBox.setGeometry(QtCore.QRect(260, 70, 91, 17))
        self.ModifiedCheckBox.setObjectName("ModifiedCheckBox")
        
        self.AnalyticalCheckBox = QtWidgets.QRadioButton(self.centralwidget)
        self.AnalyticalCheckBox.setGeometry(QtCore.QRect(260, 90, 121, 17))
        self.AnalyticalCheckBox.setObjectName("AnalyticalCheckBox")
        
        ####The go button####
        
        self.StartPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartPushButton.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.StartPushButton.setObjectName("StartPushButton")
        
        self.ClearPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearPushButton.setGeometry(QtCore.QRect(250, 310, 75, 23))
        self.ClearPushButton.setObjectName("ClearPushButton")
        
        ####Output Fields####
        
        self.MaxVelocityOutput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.MaxVelocityOutput.setGeometry(QtCore.QRect(270, 440, 113, 20))
        self.MaxVelocityOutput.setReadOnly(True)
        self.MaxVelocityOutput.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.MaxVelocityOutput.setObjectName("MaxVelocityOutput")
        self.MaxVelocityOutput.setMinimum(-999999999) #allowing negatives
        
        self.TotalTimeOutput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.TotalTimeOutput.setGeometry(QtCore.QRect(270, 410, 113, 20))
        self.TotalTimeOutput.setReadOnly(True)
        self.TotalTimeOutput.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.TotalTimeOutput.setObjectName("TotalTimeOutput")
        self.TotalTimeOutput.setMaximum(999999999)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #####Defining label widgets####
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 200, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 410, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 440, 91, 20))
        self.label_10.setObjectName("label_10")
                
        self.HeightWidget = QtWidgets.QWidget(self.centralwidget)
        self.HeightWidget.setGeometry(QtCore.QRect(400, 5, 395, 460))
        self.HeightWidget.setObjectName("HeightWidget")
        self.VelocityWidget = QtWidgets.QWidget(self.centralwidget)
        self.VelocityWidget.setGeometry(QtCore.QRect(430, 250, 341, 231))
        self.VelocityWidget.setObjectName("VelocityWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.HeightWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.StartPushButton.clicked.connect(self.MainOutput)
        self.ClearPushButton.clicked.connect(self.Clear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        
        ####Setting label text####
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EulerCheckBox.setText(_translate("MainWindow", "Euler"))
        self.ModifiedCheckBox.setText(_translate("MainWindow", "Modified Euler"))
        self.AnalyticalCheckBox.setText(_translate("MainWindow", "Analytical Prediction"))
        self.label.setText(_translate("MainWindow", "Algorithm Type"))
        self.label_2.setText(_translate("MainWindow", "Variables and Intial Conditions"))
        self.label_3.setText(_translate("MainWindow", "Starting Height (m)"))
        self.label_4.setText(_translate("MainWindow", "Time Step (s)"))
        self.label_5.setText(_translate("MainWindow", "Air Density "))
        self.label_6.setText(_translate("MainWindow", "Cross Section"))
        self.label_7.setText(_translate("MainWindow", "Drag Coefficient"))
        self.label_8.setText(_translate("MainWindow", "Object Mass (kg)"))
        self.StartPushButton.setText(_translate("MainWindow", "Plot"))
        self.ClearPushButton.setText(_translate("MainWindow", "Clear"))
        self.VariableDensityCheckBox.setText(_translate("MainWindow", "Variable Air Density"))
        self.label_9.setText(_translate("MainWindow", "Time Elapsed"))
        self.label_10.setText(_translate("MainWindow", "Maximum Velocity"))

class Main(QtWidgets.QMainWindow, Ui_MainWindow): #Class that contains main program logic for output
    
    
    def __init__(self, ): #sets up the UI immeditately on Main() call
        super(Main, self).__init__()
        self.setupUi(self)
 
    def addmpl(self, fig, fig2): #used to add graphs to the UI
        self.canvas = Canvas(fig)
        self.canvas2 = Canvas(fig2)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.canvas2)
        self.canvas.draw()
        self.canvas2.draw()
    
    def rmmpl(self,): #used to remove graphs from the UI
        self.verticalLayout.removeWidget(self.canvas)
        self.verticalLayout.removeWidget(self.canvas2)
        self.canvas.close()
        self.canvas2.close()

    
    def MainOutput(self): #Main logic loop

        #### Pulling constants from respective fields within UI####

        gravity = 9.81
        
        drag_coefficient = self.DragEntry.value()
        air_density = self.DensityEntry.value()
        cross_section = self.CrossSectionEntry.value()
        mass = self.MassEntry.value()
        time_step = self.TimeEntry.value()
        initial_height = self.HeightEntry.value()
        
        
        #### Initialising lists for data entry ####
        
        time_axis = [0]
        height_axis = [initial_height]
        velocity_axis = [0]
        
        height_axis_modified = [initial_height]
        velocity_axis_modified = [0]
        
        height_axis_analytical = [initial_height]
        velocity_axis_analytical = [0]
        
        velocity_predicted = [0]
        
        time_index = 0
         
        resistance_constant = 0.5 * (drag_coefficient * air_density * cross_section)
        
        
        
        #### Defining various functions for the iteration of Euler's method ####
            
        def velocity_iteration(velocity, resistance, step):
            return velocity - step * (gravity + (resistance/mass)*(np.abs(velocity)*velocity))
        
        def height_iteration(height, velocity, step):
            return height + step * velocity
        
        def density_eq(height):
            return air_density * np.exp(-height/7640)
                
        
        current_height = initial_height #tracking variable for height
        
        while current_height > 0: #loop runs so long as the height is above 0 - ie. the object has not hit the ground yet.

                time_index += 1 #simple index reference for the number of time steps generated by the while loop
                time_axis.append(time_index * time_step) #generating the value on the timeaxis for loop repetition
                
                if self.EulerCheckBox.isChecked() is True:
                    if self.VariableDensityCheckBox.isChecked() is True:
                        resistance_constant = 0.5 * (drag_coefficient * density_eq(height_axis[time_index-1]) * cross_section) 
                        
                    height_axis.append(height_iteration(height_axis[time_index-1], velocity_axis[time_index-1], time_step))
                    velocity_axis.append(velocity_iteration(velocity_axis[time_index-1], resistance_constant, time_step))
            
                    current_height = height_axis[time_index]
                    
                elif self.ModifiedCheckBox.isChecked() is True:
                    
                    if self.VariableDensityCheckBox.isChecked() is True:
                        resistance_constant = 0.5 * (drag_coefficient * density_eq(height_axis_modified[time_index-1]) * cross_section)
                    
                        
                    velocity_predicted.append(velocity_iteration(velocity_predicted[time_index-1], resistance_constant, time_step))   
                    
                    modified_iteration = (velocity_iteration(velocity_axis_modified[time_index-1], resistance_constant, time_step/2)
                                            + velocity_iteration(velocity_predicted[time_index], resistance_constant, time_step/2)
                                            - velocity_predicted[time_index])
                    
                    velocity_axis_modified.append(modified_iteration)
                    
                    height_axis_modified.append(height_iteration(height_axis_modified[time_index-1], velocity_predicted[time_index] + velocity_axis_modified[time_index-1], time_step/2))
                    
                    current_height = height_axis_modified[time_index]
                    
                elif self.AnalyticalCheckBox.isChecked() is True:
                    if self.VariableDensityCheckBox.isChecked() is True:
                        resistance_constant = 0.5 * (drag_coefficient * density_eq(height_axis_analytical[time_index-1]) * cross_section)
                                        
                    velocity_axis_analytical.append(- np.sqrt((mass* gravity) /resistance_constant) * np.tanh(np.sqrt(resistance_constant * gravity / mass) * time_axis[time_index]))
                    height_axis_analytical.append(initial_height -  (mass /(2 * resistance_constant)) * np.log((np.cosh(np.sqrt((resistance_constant * gravity) / mass) * time_axis[time_index]))**2))
                    
                    current_height = height_axis_analytical[time_index]

                else:
                    break #prevents infinite recursion and crashing due if no options are selected

       
        
        #### Graph plotting logic ####
        self.rmmpl()
        HeightPlot = fig.add_subplot(111)
        VelocityPlot = fig2.add_subplot(111)
        
        HeightPlot.set_ylabel("Height above sea level (m)")
        HeightPlot.set_xlabel("Time Elapsed (s)")
        VelocityPlot.set_ylabel("Velocity (ms^-1)")
        VelocityPlot.set_xlabel("Time Elapsed (s)")
        
        if self.EulerCheckBox.isChecked() is True:
            V_max = min(velocity_axis)
            HeightPlot.plot(time_axis,height_axis)
            VelocityPlot.plot(time_axis,velocity_axis)
                
        elif self.ModifiedCheckBox.isChecked() is True:
            V_max = min(velocity_axis_modified)
            HeightPlot.plot(time_axis,height_axis_modified)
            VelocityPlot.plot(time_axis,velocity_axis_modified)
               
                
        elif self.AnalyticalCheckBox.isChecked() is True:
            V_max = min(velocity_axis_analytical)
            HeightPlot.plot(time_axis,height_axis_analytical)
            VelocityPlot.plot(time_axis,velocity_axis_analytical)          
        else:
            self.rmmpl()
        

        self.TotalTimeOutput.setValue(time_index * time_step)
        self.MaxVelocityOutput.setValue(V_max)

        
        self.addmpl(fig, fig2) #add and draw created graphs
        main.show()
    
    def Clear(self): #clearing the graphs of all
        self.rmmpl()
        HeightPlot.cla()
        VelocityPlot.cla()
        
        
        HeightPlot.plot([])
        VelocityPlot.plot([])



if __name__ == "__main__": #this is what runs if the python script is executed directly (as opposed to being imported)
    
    
    ####Initialise blank graph to fill out space###
    
    fig = Figure()
    HeightPlot = fig.add_subplot(111)
    HeightPlot.plot([])
    
    fig2 = Figure()
    VelocityPlot = fig2.add_subplot(111)
    VelocityPlot.plot([])
    
    if not QtWidgets.QApplication.instance(): #prevents a segmentation fault that would occur from running a QApplication within Spyder or a similar Python IDE that itself relies on PyQt to run.
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
        
    main = Main() #intialise main class
    main.addmpl(fig, fig2)
    main.show()
        
    sys.exit(app.exec_()) #ensure app exits properly when closed
    