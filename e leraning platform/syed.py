from PyQt5 import QtCore , QtGui , QtWidgets import seaborn as sns
import matplotlib.pyplot as plt 
class Ui_MainWindow(object):    
      def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") 
        MainWindow.resize(839, 678)         
        font=QtGui.QFont()         
        font.setUnderline(False)         
        MainWindow.setFont(font) 
        MainWindow.setContextMenuPolicy.QtCore.Qt.DefaultContextMenu         
        self.centralwidget.QtWidgets.QWidget(MainWindow)         
        self.centralwidget.setObjectName("centralwidget")         
        self.label.QtWidgets.QLabel(self.centralwidget)         
        self.label.setGeometry.QtCore.QRect(150, 0, 671, 121)         
        font = QtGui.QFont()         
        font.setBold(True)         
        font.setUnderline(False)         
        self.label.setFont(font) 
        self.label.setAutoFillBackground(True) 
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);")        
        self.label.setText("") 
        self.label.setPixmap.QtGui.QPixmap("../images/mergeimg.jpg")       
        self.label.setScaledContents(True)         
        self.label.setWordWrap(False)         
        self.label.setObjectName("label") 
        self.frame . QtWidgets.QFrame(self.centralwidget)         
        self.frame.setGeometry.QtCore.QRect(0, 0, 151, 641) 
        self.frame.setStyleSheet("background-color: rgb(0, 1, 86);\n" "") 
        self.frame.setFrameShape.QtWidgets.QFrame.StyledPanel        
        self.frame.setFrameShadow.QtWidgets.QFrame.Raised         
        self.frame.setObjectName("frame")         
        self.label_2.QtWidgets.QLabel(self.frame) 
        self.label_2.setGeometry.QtCore.QRect(40, 10, 71, 61)
        self.label_2.setStyleSheet("")         
        self.label_2.setText("") 
        self.label_2.setPixmap.QtGui.QPixmap("../images/logo2.png")         
        self.label_2.setScaledContents(True)         
        self.label_2.setObjectName("label_2")         
        self.label_3.QtWidgets.QLabel(self.frame) 
        self.label_3.setGeometry.QtCore.QRect(40, 70, 81, 21)         
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 700 10pt \"Segoe UI\";") 
        self.label_3.setObjectName("label_3") 
        self.layoutWidget . QtWidgets.QWidget(self.centralwidget)         
        self.layoutWidget.setGeometry.QtCore.QRect(10, 180, 131, 220);        
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget) 
        self.verticalLayout.setContentsMargins(0, 0, 0, 0) 
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(35, 50))         
        font = QtGui.QFont()
        font.setBold(True)         
        font.setUnderline(False)         
        self.pushButton.setFont(font) 
        self.pushButton.setAutoFillBackground(False) 
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n" "color: rgb(255, 255, 255);") 
        self.pushButton.setObjectName("pushButton")       
        self.verticalLayout.addWidget(self.pushButton) 
        self.pushButton_3 =QtWidgets.QPushButton 
        (self.layoutWidget ,font.setBold(True)         
        font.setUnderline(False)         
        self.pushButton_4.setFont(font) 
        self.pushButton_4.setAutoFillBackground(False) 
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 0);\n" "color: rgb(255, 255, 255);") 
        self.pushButton_4.setObjectName("pushButton_4")         
        self.verticalLayout.addWidget(self.pushButton_4)         
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)         
        self.frame_2.setGeometry(QtCore.QRect(150, 120, 671, 521))         
        self.frame_2.setStyleSheet("background-color: rgb(0, 93, 93);\n" "")[11:17 PM, 2/12/2024] SYED: self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)         
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)         
        self.frame_2.setObjectName("frame_2")         
        self.templabel = QtWidgets.QLabel(self.frame_2) 
        self.templabel.setGeometry(QtCore.QRect(210, 10, 251, 51))         
        self.templabel.setStyleSheet("color: rgb(255, 255, 255);\n" "font: 700 10pt \"Segoe UI\";") 
        self.templabel.setObjectName("templabel")         
        self.frame_3 = QtWidgets.QFrame(self.frame_2)         
        self.frame_3.setGeometry(QtCore.QRect(10, 70, 651, 51)) 
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")         
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)         
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)         
        self.frame_3.setObjectName("frame_3")         
        self.label_5 = QtWidgets.QLabel(self.frame_3)         
        self.label_5.setGeometry(QtCore.QRect(20, 10, 61, 21))         
        self.label_5.setObjectName("label_5")          
        self.statecombobox = QtWidgets.QComboBox(self.frame_3)         
        self.statecombobox.setGeometry(QtCore.QRect(90, 10, 131, 21))         
        self.statecombobox.setObjectName("statecombobox")         
        #------------- Here I have put the skeleton of the state         for i in range (len(state_list)): 
        self.statecombobox.addItem("") 
        self.showdata = QtWidgets.QPushButton(self.frame_3)         
        self.showdata.setGeometry(QtCore.QRect(480, 10, 151, 31)) 
        self.showdata.setStyleSheet("background-color: rgb(0, 130, 0);\n" "color: rgb(255, 255, 255);") 
        self.showdata.setObjectName("showdata") 
        self.districtcombobox = QtWidgets.QComboBox(self.frame_3)     
        self.districtcombobox.setGeometry(QtCore.QRect(320, 10, 131, 22))     
        self.districtcombobox.setObjectName("districtcombobox")         
        for i in range (len(district_list)): 
                self.districtcombobox.addItem("") 
                # --------------Here you have put the district's skeleton  
         
        self.label_6 = QtWidgets.QLabel(self.frame_3)       
        self.label_6.setGeometry(QtCore.QRect(240, 10, 71, 21))    
        self.label_6.setObjectName("label_6") 
        self.label_4 = QtWidgets.QLabel(self.frame_2)[11:18 PM, 2/12/2024] SYED:
        self.label_4.setObjectName("label_4") 
        self.piechartcrop = QtWidgets.QLabel(self.frame_2) 
        self.piechartcrop.setGeometry(QtCore.QRect(10, 190, 301, 231))        
        self.piechartcrop.setText("") 
        self.piechartcrop.setScaledContents(True)        
        self.piechartcrop.setWordWrap(False) 
        self.piechartcrop.setObjectName("piechartcrop")       
        self.piechartcategory = QtWidgets.QLabel(self.frame_2)
[11:19 PM, 2/12/2024] SYED: self.piechartcategory.setGeometry(QtCore.QRect(350, 190, 301, 231))         font = QtGui.QFont()         font.setPointSize(12)         font.setBold(False) 
        self.piechartcategory.setFont(font) 
        self.piechartcategory.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))         self.piechartcategory.setAutoFillBackground(False)         self.piechartcategory.setText("") 
        self.piechartcategory.setScaledContents(True) 
        self.piechartcategory.setObjectName("piechartcategory") 
         
        self.frame_4 = QtWidgets.QFrame(self.frame_2) 
        self.frame_4.setGeometry(QtCore.QRect(10, 430, 651, 51)) 
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")         
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)         
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)         
        self.frame_4.setObjectName("frame_4")         
        self.label_9 = QtWidgets.QLabel(self.frame_4)        
        self.label_9.setGeometry(QtCore.QRect(30, 20, 91, 16))         
        self.label_9.setObjectName("label_9")         
        self.label_10 = QtWidgets.QLabel(self.frame_4)         
        self.label_10.setGeometry(QtCore.QRect(250, 20, 71, 16))         
        self.label_10.setObjectName("label_10")         
        self.label_11 = QtWidgets.QLabel(self.frame_4)         
        self.label_11.setGeometry(QtCore.QRect(450, 20, 71, 16))         
        self.label_11.setObjectName("label_11") 
        self.suggestedcrop = QtWidgets.QLabel(self.frame_4) 
        self.suggestedcrop.setGeometry(QtCore.QRect(130, 20, 111, 16))         
        self.suggestedcrop.setObjectName("suggestedcrop")         
        self.alternate1 = QtWidgets.QLabel(self.frame_4) 
        self.alternate1.setGeometry(QtCore.QRect(330, 20, 111, 16))         
        self.alternate1.setObjectName("alternate1")         
        self.alternate2 = QtWidgets.QLabel(self.frame_4) 
        self.alternate2.setGeometry(QtCore.QRect(530, 20, 111, 16))         
        self.alternate2.setAutoFillBackground(False)         
        self.alternate2.setObjectName("alternate2")         
        self.cropwiselabel = QtWidgets.QLabel(self.frame_2) 
        self.cropwiselabel.setGeometry(QtCore.QRect(50, 150, 231, 21))         
        self.cropwiselabel.setStyleSheet("color: rgb(255, 255, 255);")         
        self.cropwiselabel.setObjectName("cropwiselabel")         
        self.categorywiselabel = QtWidgets.QLabel(self.frame_2) 
        self.categorywiselabel.setGeometry(QtCore.QRect(360, 150, 301, 21))         
        self.categorywiselabel.setStyleSheet("color: rgb(255, 255, 255);")         
        self.categorywiselabel.setObjectName("categorywiselabel")         
        self.frame.raise_()
        [11:20 PM, 2/12/2024] SYED: self.layoutWidget.raise_()         
        self.frame_2.raise_() 
        MainWindow.setCentralWidget(self.centralwidget)         
        self.statusbar = QtWidgets.QStatusBar(MainWindow)        
          self.statusbar.setObjectName("statusbar")   MainWindow.setStatusBar(self.statusbar)
        [11:22 PM, 2/12/2024] SYED: self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
        def retranslateUi(self, MainWindow): 
        _translate = QtCore.QCoreApplication.translate 
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))         
        self.label_3.setText(_translate("MainWindow", "AGRI"))         
        self.pushButton.setText(_translate("MainWindow", ""))         
        self.pushButton_3.setText(_translate("MainWindow", ""))         
        self.pushButton_2.setText(_translate("MainWindow", ""))         
        self.pushButton_4.setText(_translate("MainWindow", ""))         
        self.templabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Crop Production </span></p></body></html>")) 
        self.label_5.setText(_translate("MainWindow", "Select State"))         
        self.showdata.setText(_translate("MainWindow", "Show Data"))         
        self.label_6.setText(_translate("MainWindow", "Select District"))         
        self.label_4.setText(_translate("MainWindow", "TextLabel"))         
        self.label_9.setText(_translate("MainWindow", "Suggested Crop :"))         
        self.label_10.setText(_translate("MainWindow", "Alternate 1 :"))         
        self.label_11.setText(_translate("MainWindow", "Alternate 2 :"))         
        self.suggestedcrop.setText(_translate("MainWindow", 
"...................................")) 
        self.alternate1.setText(_translate("MainWindow", 
"....................................")) 
        self.alternate2.setText(_translate("MainWindow", 
"...................................")) 
        self.cropwiselabel.setText(_translate("MainWindow", 
"<html><head/><body><p><br/></p></body></html>")) 
        self.categorywiselabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))  
#-----------------------------------------------------------Your work starts from here----------------------- 
                 for i in range (len(state_list)): 
                self.statecombobox.setItemText(i, _translate("MainWindow", state_list[i])) 
                #Here I have entered the state data 
              for i in range (len(district_list)): 
                self.districtcombobox.setItemText(i, _translate("MainWindow", district_list[i])) 
                #Here I have entered the data of the district
[11:22 PM, 2/12/2024] SYED: def func(self): 
        state=self.statecombobox.currentText()          dist=self.districtcombobox.currentText()         self.find(state,dist)     def find(self,state,dist): 
            self.cropwiselabel.setText("Crop Wise Production Status")