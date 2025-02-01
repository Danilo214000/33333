from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 160, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius:10px;
            border: 4px outset #006400;
        }
        """)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 75, 160, 590))
        self.listView.setObjectName("listView")

        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 10, 281, 341))
        self.widget.setObjectName("widget")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 10, 110, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius:10px;
            border: 2px solid #006400;
        }
        """)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 60, 110, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)

        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 110, 110, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 160, 110, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 210, 110, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(770, 260, 110, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(770, 310, 110, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("""
        QPushButton {        
            background-color: #90EE90;
            color: black;
            border-radius: 10px;
            border: 2px solid #006400;
        }
        """)




        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(765, 350, 120, 20))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 390, 35, 10))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(725, 375, 180, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(775, 395, 180, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Фотографії"))
        self.pushButton_2.setText(_translate("MainWindow", "Вліва"))
        self.pushButton_3.setText(_translate("MainWindow", "Вправа"))
        self.pushButton_4.setText(_translate("MainWindow", "Дрекало"))
        self.pushButton_5.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_6.setText(_translate("MainWindow", "Ч/Б"))
        self.pushButton_7.setText(_translate("MainWindow", "Колір"))
        self.pushButton_8.setText(_translate("MainWindow", "Размітіє"))
        self.label.setText(_translate("MainWindow", "ФатаЖопа3000"))
        self.label_3.setText(_translate("MainWindow", "Нету лучше мужчины!"))
        self.label_4.setText(_translate("MainWindow", "Чем Фурри!"))


