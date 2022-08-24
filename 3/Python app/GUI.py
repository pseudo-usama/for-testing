from importlib.resources import path
from shelve import Shelf
from typing_extensions import Self
import warnings
from PIL import Image,ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.preprocessing import image

from PyQt5 import Qtcore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from win32com.client import Dispatch


def speak(str1):
   speak=Dispatch(("SApI.SpVoice"))
   speak.Speak(str1)
class ui_MainWindow(object):
      def setupui(self,Mainwindow,QtCore):
          Mainwindow.setObjectName("MainWindow")
          Mainwindow.resize(695,609)
          self.centralwidget=QtWidgets.QWidget(Mainwindow)
          self.centralWidget.setObjectName("centralwidget")
          self.fram = QtWidgets.QFrame(self.centralwidget)
          self.frame.setGeometry(QtCore.QRect(0,0,701,611))
          self.fram.setStyleSheet("background-color:#035874;")
          self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
          self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
          self.frame.setObjectName("frame")
          self.label = QtWidgets.QLabel(self.fram)
          self.label.setGeometry(Qtcore.QRect(80,-60,541,561))
          self.label.setText("")
          self.gif=QMovie("picture.gif")
          self.label.setMovie(self.gif)
          self.gif.start()
          self.label.setobjectName("label")
          self.label_2 = QtWidgets.QLabel(self.frame)
          self.label_2.setGeometry(Qtcore.QRect(80,430,591,41))
          font = QtGui.QFont()
          font.setPointSize(24)
          font.setBold(True)
          font.setWeight(75)
          self.label_2.setFont(font)
          self.label_2.setObjectName("label_2")
          self.pushButton = QtWidgets.QpushButton(self.frame)
          self.pushButton.setGeometry(Qtcore.QRect(30,530,201,31))
          font = QtGui.QFont()
          font.setPointSize(12)
          font.setBold(True)
          font.setWeight(75)
          icon = QtGui.QIcon()
          icon.addPixmap(QtGui.Qpixmap("patient.png"),QtGui.QIcon.Normal,QtGui.QIcon.off)
          Mainwindow.setWindowIcon(icon)
          self.pushButton.setFont(font)
          self.pushButton.setStyleSheet("QpushButton{\n"
   "border-radius:10px;\n"
   "background-color:#DF582c;\n"
   "\n"
   "}\n"
  "QpushButton:hover {\n"
  "background-color:#7D93E0;\n"
  "}")
class ui_MainWindow(object):
      def setupui(self,Mainwindow,QtCore):
       self.pushButton.setObjectName("pushButton")
       self.pushButton_2=QtWidgets.QpushButton(self.frame)
       self.pushButton_2.setGeometry(QtCore.QRect(450,530,201,31))
       font = QtGui.QFont()
       font.setPointSize(12)
       font.setBold(True)
       font.setWeight(75)
       self.pushButton_2.setFont(font)
       self.pushButton_2.setStyleSheet("QpushButton{\n"
     "border-radius:10px;\n"
     "background-color:#DF582c;\n"
   "\n"
   "}\n"
  "QpushButton:hover {\n"
  "background-color:#7D93E0;\n"
  "}")
class ui_MainWindow(object):
      def setupui(self,MainWindow,QtCore):
       self.pushButton_2.setObjectName("pushButton_2")
       MainWindow.setCentralWidget(self.centralwidget)

       self.retranslateUi(MainWindow)
       QtCore.QMetaObject.connectSlotsByName(MainWindow)
       self.pushButton.clicked.connect(self.upload_image)
       self.pushButton_2.clicked.connect(self.predict_result)

      def retranslateUi(self,MainWindow,QtCore,_translate):
        _translate = QtCore.QCoreApplications.translate
        MainWindow.setWindowTitle(_translate("Mainwindow","PNEUMONIA Detection Apps"))
        self.label.setToolTip(_translate("C:\\Users\\Shaniii\\Desktop\\New folder (2)\\Lungs X_ray"))
        self.label_2.setText(_translate("MainWindow","chest X_ray PNEUMONIA"))
        self.pushButton.setText(_translate("Mainwindow","upload Image"))
        self.pushButton_2.setText(_translate("MainWindow","Prediction"))
      def upload_image(self):
       filename=QFileDialog.getOpenFileName()
       path=filename[0]
       path=str(path)
       print(path)
      model=load_model('chest_xray.h5')
      img_file=image.load_img(path,target_size=(224,224))
      x=image.img_to_arry(img_file)
      x=np.expand_dims(x,axis=0)
      img_data=preprocess_input(x)
      classes=model.predict(img_data)
      global result
      result=classes

def predict_result(self):
     print(result)
if result[0][0]>0.5:
      print("Result is Normal")
      speak("Result is Normal")
else:
  print("Affected By PNEUMONIA")
  speak("Affected By PNEUMONIA")
 
 
if __name__ == "__main__":
   import sys
   app=QtWidgets.QApplication(sys.argv)
   MainWindow= QtWidgets.QMainWindow()
   ui= ui_MainWindow()
   ui.setupui(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())