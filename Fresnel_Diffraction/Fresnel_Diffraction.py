##################################################################################################################################
#####IMPORTANT - IF RUNNING IN AN IPYTHON CONSOLE, THE COMMAND "%gui qt5" MUST FIRST BE RUN, OR THE KERNEL WILL ENDLESSLY DIE#####
##################################################################################################################################

import sys
import matplotlib

# Ensure using PyQt5 backend
#must be imported before matplotlib.backends and matplotlib.pyplot

matplotlib.use('QT5Agg') #this /should/ do something, but judging by the angry console messages...

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas

import numpy as np
from scipy import integrate as integrate #ADDING THIS FIXES THINGS AND I HAVE NO IDEA WHY, sp.integrate.simps does not work but this does despite referencing the same thing in the same package???
from mpl_toolkits.axes_grid1 import make_axes_locatable






class Ui_MainWindow(object): #Class that contains all UI objects
    def setupUi(self, MainWindow):
        
        ####Define main window framework and tab structure####
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 490)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.PartATab = QtWidgets.QWidget()
        self.PartATab.setObjectName("PartATab")
               
        
        ##########Creating various labels used throughout the GUI##########
        
        
        font = QtGui.QFont() #defining label font type and size
        font.setPointSize(12)
        
        self.label = QtWidgets.QLabel(self.PartATab)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.PartATab)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 71, 21))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.PartATab)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 46, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.PartATab)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 101, 20))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(self.PartATab)
        self.label_5.setGeometry(QtCore.QRect(180, 80, 46, 21))      
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.PartATab)
        self.label_6.setGeometry(QtCore.QRect(180, 50, 71, 21))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(self.PartATab)
        self.label_7.setGeometry(QtCore.QRect(30, 270, 111, 16))
        self.label_7.setObjectName("label_7")
        
        self.label_8 = QtWidgets.QLabel(self.PartATab)
        self.label_8.setGeometry(QtCore.QRect(210, 270, 61, 16))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.PartATab)
        self.label_9.setGeometry(QtCore.QRect(380, 430, 371, 20))
        self.label_9.setObjectName("label_9")
        
        self.label_10 = QtWidgets.QLabel(self.PartATab)
        self.label_10.setGeometry(QtCore.QRect(30, 340, 121, 16))
        self.label_10.setObjectName("label_10")
        
        
        ##############Creating various spinboxes for user data entry#############
        
        #Default values are set to values defined in the exercise script, for ease of testing code changes
        
        self.IntegralNSpinBox = QtWidgets.QSpinBox(self.PartATab)
        self.IntegralNSpinBox.setEnabled(True)
        self.IntegralNSpinBox.setGeometry(QtCore.QRect(120, 50, 51, 22))
        self.IntegralNSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.IntegralNSpinBox.setAccelerated(False)
        self.IntegralNSpinBox.setMaximum(1000)
        self.IntegralNSpinBox.setSingleStep(2)
        self.IntegralNSpinBox.setObjectName("IntegralNSpinBox")
        self.IntegralNSpinBox.setValue(100)
        
        self.ScreenDistanceMainSpinBox = QtWidgets.QDoubleSpinBox(self.PartATab)
        self.ScreenDistanceMainSpinBox.setGeometry(QtCore.QRect(120, 20, 51, 22))
        self.ScreenDistanceMainSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.ScreenDistanceMainSpinBox.setDecimals(2)
        self.ScreenDistanceMainSpinBox.setMaximum(9.99)
        self.ScreenDistanceMainSpinBox.setObjectName("ScreenDistanceMainSpinBox")
        self.ScreenDistanceMainSpinBox.setValue(2)
        
        
        self.ScreenDistancePowerSpinBox = QtWidgets.QSpinBox(self.PartATab)
        self.ScreenDistancePowerSpinBox.setGeometry(QtCore.QRect(200, 21, 41, 21))
        self.ScreenDistancePowerSpinBox.setWrapping(True)
        self.ScreenDistancePowerSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.ScreenDistancePowerSpinBox.setMinimum(-99)
        self.ScreenDistancePowerSpinBox.setObjectName("ScreenDistancePowerSpinBox")
        self.ScreenDistancePowerSpinBox.setValue(-2)
        

        
        self.WavelengthMainSpinBox = QtWidgets.QDoubleSpinBox(self.PartATab)
        self.WavelengthMainSpinBox.setGeometry(QtCore.QRect(120, 80, 51, 21))
        self.WavelengthMainSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.WavelengthMainSpinBox.setMaximum(9.99)
        self.WavelengthMainSpinBox.setObjectName("WavelengthMainSpinBox")
        self.WavelengthMainSpinBox.setValue(1)
        
        self.WavelengthPowerSpinBox = QtWidgets.QSpinBox(self.PartATab)
        self.WavelengthPowerSpinBox.setGeometry(QtCore.QRect(200, 80, 41, 21))
        self.WavelengthPowerSpinBox.setWrapping(True)
        self.WavelengthPowerSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.WavelengthPowerSpinBox.setMinimum(-99)
        self.WavelengthPowerSpinBox.setObjectName("WavelengthPowerSpinBox")
        self.WavelengthPowerSpinBox.setValue(-6)
        
        self.IterationNSpinBox = QtWidgets.QSpinBox(self.PartATab)
        self.IterationNSpinBox.setGeometry(QtCore.QRect(40, 360, 42, 22))
        self.IterationNSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.IterationNSpinBox.setMaximum(10000000) #Set as an arbitrary large maximum unless you want the possibility of leaving the program running for weeks on end...
        self.IterationNSpinBox.setObjectName("IterationNSpinBox")
        self.IterationNSpinBox.setValue(100)
        
        

        
        #Defining radio buttons in GUI for dynamic input selection#
        
        self.RadioHomebrew = QtWidgets.QRadioButton(self.PartATab)
        self.RadioHomebrew.setGeometry(QtCore.QRect(40, 130, 191, 21))
        self.RadioHomebrew.setChecked(True) #ensures that a button is checked on startup to prevent breaking functions later in code
        self.RadioHomebrew.setObjectName("RadioHomebrew")
        self.FunctionButtonGroup = QtWidgets.QButtonGroup(MainWindow) #Creates a new button group for the function selection, means the RadioHomebrew and RadioInbuilt buttons are exclusive, and only one of the two can be selected
        self.FunctionButtonGroup.setObjectName("FunctionButtonGroup")
        self.FunctionButtonGroup.addButton(self.RadioHomebrew) 
        
        self.RadioInbuilt = QtWidgets.QRadioButton(self.PartATab)
        self.RadioInbuilt.setGeometry(QtCore.QRect(40, 160, 181, 17))
        self.RadioInbuilt.setAutoExclusive(True)
        self.RadioInbuilt.setObjectName("RadioInbuilt")
        self.FunctionButtonGroup.addButton(self.RadioInbuilt) #adds the new button to the fuction button group
        
        self.RadioOne = QtWidgets.QRadioButton(self.PartATab)
        self.RadioOne.setGeometry(QtCore.QRect(40, 200, 101, 17))
        self.RadioOne.setObjectName("RadioOne")
        self.RadioOne.setChecked(True) #as above
        self.DimensionButtonGroup = QtWidgets.QButtonGroup(MainWindow) # as above, but for the selection of 1D or 2D Apertures
        self.DimensionButtonGroup.setObjectName("DimensionButtonGroup")
        self.DimensionButtonGroup.addButton(self.RadioOne)
        
        self.RadioTwo = QtWidgets.QRadioButton(self.PartATab)
        self.RadioTwo.setGeometry(QtCore.QRect(40, 230, 111, 17))
        self.RadioTwo.setObjectName("RadioTwo")
        self.DimensionButtonGroup.addButton(self.RadioTwo) #adds the new button to the dimension button group
        
        
        #####################################################
        
        ####Defining a QWidget used to contain matplotlib figures when they are added to the main GUI####
        
        self.MatplotlibWidget = QtWidgets.QWidget(self.PartATab)
        self.MatplotlibWidget.setGeometry(QtCore.QRect(350, 0, 420, 340))
        self.MatplotlibWidget.setObjectName("MatplotlibWidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MatplotlibWidget.sizePolicy().hasHeightForWidth())
        self.MatplotlibWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MatplotlibWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
             
        self.OkButton = QtWidgets.QPushButton(self.PartATab)
        self.OkButton.setGeometry(QtCore.QRect(360, 390, 75, 23))
        self.OkButton.setObjectName("OkButton")
        self.CancelButton = QtWidgets.QPushButton(self.PartATab)
        self.CancelButton.setGeometry(QtCore.QRect(460, 390, 75, 23))
        self.CancelButton.setObjectName("CancelButton")
        


        

        #######Experimenting with LineEdits over spinboxes as a means of data entry###########
        
        #ImhFormattedNumbersOnly does not seem to result in the expected input restrictions - should restrict data entry to digits, decimal points and minus signs only.
        #Bug: ImhFormattedNumbersOnly does not have any effect on LineEdit data entry - all characters appear to be allowed
        #Further testing indicates that no value will be parsed if it is not a valid number, which is nice. No fatal errors here!
              
        
        self.X_ApertureEntry = QtWidgets.QLineEdit(self.PartATab)
        self.X_ApertureEntry.setGeometry(QtCore.QRect(40, 290, 71, 20))
        self.X_ApertureEntry.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.X_ApertureEntry.setObjectName("X_ApertureEntry")
        self.X_ApertureEntry.setText("1E-5")
        
        self.Y_ApertureEntry = QtWidgets.QLineEdit(self.PartATab)
        self.Y_ApertureEntry.setGeometry(QtCore.QRect(40, 310, 71, 20))
        self.Y_ApertureEntry.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.Y_ApertureEntry.setObjectName("Y_ApertureEntry")
        self.Y_ApertureEntry.setText("1E-5")
        
        self.X_AxisSize = QtWidgets.QLineEdit(self.PartATab)
        self.X_AxisSize.setGeometry(QtCore.QRect(180, 290, 113, 20))
        self.X_AxisSize.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.X_AxisSize.setObjectName("X_AxisSize")
        self.X_AxisSize.setText("0.005")
        
        self.Y_AxisSize = QtWidgets.QLineEdit(self.PartATab)
        self.Y_AxisSize.setGeometry(QtCore.QRect(180, 310, 113, 20))
        self.Y_AxisSize.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.Y_AxisSize.setObjectName("Y_AxisSize")
        self.Y_AxisSize.setText("0.005")

        

        
        self.tabWidget.addTab(self.PartATab, "")
        
        ####Various cosmetic things for MainWindow####

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.OkButton.clicked.connect(self.MainOutput) #Executes the MainOutput function in Main() when the OK pushbutton is pressed.
                                                        #Couldn't make the cancel button work properly due to program lockup, it is now a placebo. Click it as much as you want :) 
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        #####Setting the text for labels initialised earlier in the code#####
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Fresnel Diffraction - Josiah Farrelly"))
        self.OkButton.setText(_translate("MainWindow", "Ok"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.IterationNSpinBox.setToolTip(_translate("MainWindow", "The number of loops per Aperture."))
        self.label.setText(_translate("MainWindow", "Screen Distance (m):"))
        self.label_2.setText(_translate("MainWindow", "Integration N:"))
        self.label_3.setText(_translate("MainWindow", "E"))
        self.label_4.setText(_translate("MainWindow", "Wavelength (m):"))
        self.label_5.setText(_translate("MainWindow", "E"))
        self.RadioHomebrew.setText(_translate("MainWindow", "Homebrew Simpson\'s Rule Function"))
        self.RadioInbuilt.setText(_translate("MainWindow", "Scipy Simpson\'s Rule Function"))
        self.RadioOne.setText(_translate("MainWindow", "1D Line Grating"))
        self.RadioTwo.setText(_translate("MainWindow", "2D Plane Grating"))
        self.label_6.setText(_translate("MainWindow", "(Per aperture)"))
        self.X_ApertureEntry.setPlaceholderText(_translate("MainWindow", "Horizontal"))
        self.Y_ApertureEntry.setPlaceholderText(_translate("MainWindow", "Vertical"))
        self.label_7.setText(_translate("MainWindow", "Aperture Size (metres)"))
        self.X_AxisSize.setPlaceholderText(_translate("MainWindow", "X Value"))
        self.Y_AxisSize.setPlaceholderText(_translate("MainWindow", "Y Value"))
        self.label_8.setText(_translate("MainWindow", "Axis\' Range"))
        self.label_9.setText(_translate("MainWindow", "Note: X and Y values will be taken in both positive and negative directions"))
        self.label_10.setText(_translate("MainWindow", "Number of graph points"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PartATab), _translate("MainWindow", ""))
        
        
        ####### Executing functions for user entered values and plotting graphs
            
        
    
class Main(QtWidgets.QMainWindow, Ui_MainWindow): #Class that contains main program logic for output
    
    
    def __init__(self, ): #sets up the UI immeditately on Main() call
        super(Main, self).__init__()
        self.setupUi(self)
 
    def addmpl(self, fig): #used to add graphs to the UI
        self.canvas = Canvas(fig)
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
    
    def rmmpl(self,): #used to remove graphs from the UI
        self.verticalLayout.removeWidget(self.canvas)
        self.canvas.close()
        
        
        
        
    def MainOutput(self): #Main logic
        
        
        
        ####Define used constants and important variables####
        
        permittivity_of_free_space = (8.85418782 * (10 ** -12))
        speed_of_light = 299792458
        fig = Figure() #blank figure for later graphing

        
        ####Pull values from appropriate input points in GUI####
        
        if self.IntegralNSpinBox.value() % 2 != 0: #Somewhat hacky method of ensuring that IntegralN for simpsons rule can never be an odd number
            self.IntegralNSpinBox.setValue(self.IntegralNSpinBox.value() - 1)
        
        
        WaveLength = self.WavelengthMainSpinBox.value() * (10 ** self.WavelengthPowerSpinBox.value())
        ScreenDistance = self.ScreenDistanceMainSpinBox.value() * (10 ** self.ScreenDistancePowerSpinBox.value())
        NumPoints = self.IterationNSpinBox.value()
        IntegralN = self.IntegralNSpinBox.value()
        
        #Need to add validation here -> never mind, program does it for me. A
        
        XApertureUpper = float(self.X_ApertureEntry.text()) / 2 #Setting the size of horizontal Aperture width such that 0 is the central point
        XApertureLower = - XApertureUpper
        
        
        YApertureUpper = float(self.Y_ApertureEntry.text()) / 2 #As above
        YApertureLower = -YApertureUpper
        
        XAxisSize = float(self.X_AxisSize.text())  
        YAxisSize = float(self.Y_AxisSize.text())
                                 
        ####Introduce various derived values####
        
        WaveNumber = 2 * np.pi / WaveLength
        multiplier = (WaveNumber)/ (2 * np.pi * ScreenDistance)
        
        
        y_vals = np.linspace(-YAxisSize,YAxisSize,NumPoints)
        y_Fresnel = np.zeros(NumPoints)
        
        x_vals = np.linspace(-XAxisSize,XAxisSize,NumPoints)
        x_Fresnel = np.zeros(NumPoints)
        
        OneD_Intensity = np.zeros(NumPoints)
        TwoD_Intensity = np.zeros((NumPoints,NumPoints))
        
        def SimpsonsRule(lower, upper, wav_Num, x_Coord, integral_N, screen_Distance): #Function containing both home-made and inbuilt scipy simpson's rule functions, which are executed according to which radiobutton is selected
            
            ####Reset values at the beginning of function call to prevent repetition errors####
            
            simpsons_Integral = 0
            simpsons_Even = 0
            simpsons_Odd = 0
            
            
            
            def e_Integral(x_Dash): #Creating a simple internal function for the function to be integrated via Simpson's rule, as it will be used multiple times.
                
                e_Integrand = ((1j*wav_Num) / (2  * screen_Distance)) * (x_Coord - x_Dash)**2 #where x_Dash is the integration subject
                return np.exp(e_Integrand)
            
            
            ####An attempt at determining the error in the simpsons rule. Could not implement without massively slowing down the rest of the program####
            
            '''def simpsonsError(x_Dash):
                
                def FourthDerivative(): #horrific fourth derivative of e_Integral with respect to x prime
                    return abs(e_Integral(x_Dash) * (((-3 * wav_Num **2)/screen_Distance**2) - ((61 * (wav_Num**3) * (x_Coord-x_Dash)**2)/screen_Distance**3) + (((wav_Num**4) * (x_Coord-x_Dash)**4)/screen_Distance**4)))
            
                max_x = scipy.optimize.fmin(lambda x: -FourthDerivative()) #should return the absolute value of the maximum value of the fourth derivative
                Error = (((upper-lower)**5)/(180*integral_N**4))*max_x'''
            
            if self.RadioHomebrew.isChecked(): #Home-made simpson's rule code for part A            
                
                delta_X = (upper - lower) / integral_N #generating the step value for Simpson's rule
        
    
                for i in range(2, integral_N, 2): #Even N portion of Simpson's rule, loops up to, but not including, integral_N
        
                    x_iteration = lower + i * delta_X
                    function_x = e_Integral(x_iteration)
                    simpsons_Even += 2*function_x
        
                for i in range(1, integral_N, 2): #Odd N portion of Simpson's rule
                    
                    x_iteration = lower + i * delta_X
                    function_x = e_Integral(x_iteration)
                    simpsons_Odd += 4*function_x
        
                simpsons_Integral = (e_Integral(upper) + e_Integral(lower) + simpsons_Odd + simpsons_Even) * delta_X / 3 #The full evaluated integral
    
            
            elif self.RadioInbuilt.isChecked(): #Don't go above N ~~ 200 for this, unless you want to wait about a week for your graph. Time to completion scales by IntegralN ^2 * IterationN ^2. It gets ridiculous.
                
                Aperture_spacing = np.linspace(lower,upper,integral_N)
                Aperture_value = np.zeros(integral_N,dtype = "c16") #ensures array is able to take complex numbers. May not be needed, but better safe than sorry.
                
                
                for i in range(integral_N):
                    
                   Aperture_value[i] = e_Integral(Aperture_spacing[i])

                simpsons_Integral = integrate.simps(Aperture_value,Aperture_spacing)

                
            else:
                print("RadioButton Broken") #Used for debugging
    
            return simpsons_Integral
        
        
    
            
        if self.RadioOne.isChecked():
            
            for i in range(NumPoints):
    
                E_Field = multiplier * SimpsonsRule(XApertureLower,XApertureUpper, WaveNumber, x_vals[i], IntegralN, ScreenDistance)
                Intensity = abs(E_Field * E_Field.conjugate())  * permittivity_of_free_space * speed_of_light
                OneD_Intensity[i] = Intensity
               

            
            self.rmmpl()
            ax1f1 = fig.add_subplot(111)
            ax1f1.set_title("1D Fresnel Diffraction for λ = " + str(WaveLength) + ", z = " + str(ScreenDistance)) 
            ax1f1.set_xlabel("Horizontal Position") #Bug: if program executed outside of an ipython console with %gui qt5, this label gets half cut off. No detrimental effects otherwise.
            ax1f1.set_ylabel("Relative Intensity")
            
            OneD_Intensity = (OneD_Intensity-OneD_Intensity.min())/abs(OneD_Intensity.max() - OneD_Intensity.min()) #Normalising intensities
            
            ax1f1.plot(x_vals,OneD_Intensity)
            
        
        elif self.RadioTwo.isChecked(): #performs simpsons rule over a 2D plane defined by the user

            #hideously inefficient - should be completely redone using vectorisation. O(N^4)

            for i in range(NumPoints):
                
                x_Fresnel[i] = SimpsonsRule(XApertureLower, XApertureUpper, WaveNumber, x_vals[i], IntegralN, ScreenDistance)
                
                for j in range(NumPoints):
                    
                    y_Fresnel[j] = SimpsonsRule(YApertureLower, YApertureUpper, WaveNumber, y_vals[j], IntegralN, ScreenDistance)
                    
                    E_Field = multiplier * x_Fresnel[i] * y_Fresnel[j]
                    TwoD_Intensity[i,j]  = abs(E_Field * E_Field.conjugate()) * permittivity_of_free_space * speed_of_light
            
            TwoD_Intensity = (TwoD_Intensity-TwoD_Intensity.min())/abs(TwoD_Intensity.max() - TwoD_Intensity.min()) #as above, normalising intensity values on a scale of 0 to 1
            
            self.rmmpl() #remove previous plot
            ax1f1 = fig.add_subplot(111)
            im = ax1f1.imshow(TwoD_Intensity,cmap = "GnBu", extent=[-XAxisSize, XAxisSize, -YAxisSize, YAxisSize],interpolation = "bilinear") #plot the diffraction pattern, [...] sets axis range
            
            divider = make_axes_locatable(ax1f1)
            cax = divider.append_axes("right", size="5%", pad=0.1) #adds a colourmap legend to the right of the plot
            fig.colorbar(im, cax=cax)
            
            ###Setting titles and axis labels###
               
            ax1f1.set_title("2D Fresnel Diffraction for λ = " + str(WaveLength) + ", z = " + str(ScreenDistance))            
            ax1f1.set_xlabel("Horizontal Position")
            ax1f1.set_ylabel("Vertical Position")
       

        self.addmpl(fig) #add and draw created graphs
        main.show()
        
        
        
if __name__ == "__main__": #this is what runs if the python script is executed directly (as opposed to being imported)
    
    
    ####Initialise blank graph to fill out space###
    
    fig = Figure()
    ax1f1 = fig.add_subplot(111)
    ax1f1.plot(0)
    
    
    if not QtWidgets.QApplication.instance(): #prevents a segmentation fault that would occur from running a QApplication within Spyder or a similar Python IDE that itself relies on PyQt to run.
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
        
    main = Main() #intialise main class
    main.addmpl(fig)
    main.show()
        
    sys.exit(app.exec_()) #ensure app exits properly when closed
    
    


