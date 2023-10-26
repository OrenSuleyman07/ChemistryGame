# -*- coding: utf-8 -*-

from random import randrange
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QKeySequence
import keyboard

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.setEnabled(True)
        # set size
        mainWindow.resize(400, 400)
        mainWindow.setFixedSize(400,400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        # set icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ChemistryIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)

        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet('background-color: #202020;')
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)
        self.actionprecipitation_colors = QtWidgets.QAction(mainWindow)
        self.actionprecipitation_colors.setObjectName("actionprecipitation_colors")

        self.createElements()

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.addFunctions()

    def createElements(self):
        #creating main buttons
        self.btn_OGE = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OGE.setEnabled(True)
        self.btn_OGE.setGeometry(QtCore.QRect(70, 150, 120, 51))
        self.btn_OGE.setObjectName("btn_OGE")
        self.btn_EGE = QtWidgets.QPushButton(self.centralwidget)
        self.btn_EGE.setEnabled(True)
        self.btn_EGE.setGeometry(QtCore.QRect(210, 150, 120, 51))
        self.btn_EGE.setObjectName("btn_EGE")
        self.btn_All = QtWidgets.QPushButton(self.centralwidget)
        self.btn_All.setEnabled(True)
        self.btn_All.setGeometry(QtCore.QRect(120, 220, 160, 51))
        self.btn_All.setObjectName("btn_All")
        #creating back button
        self.btn_Back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Back.setEnabled(True)
        self.btn_Back.setGeometry(QtCore.QRect(20, 350, 101, 31))
        self.btn_Back.setObjectName("btn_Back")
        self.btn_Back.hide()
        #creating game menu
        self.requestLine = QtWidgets.QLineEdit(self.centralwidget)
        self.requestLine.setGeometry(QtCore.QRect(10, 130, 261, 30))
        self.requestLine.setObjectName("requestLine")
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setGeometry(QtCore.QRect(280, 130, 111, 30))
        self.btn_go.setObjectName("btn_go")
        self.gameLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameLabel.setGeometry(QtCore.QRect(125, 60, 150, 50))
        self.gameLabel.setObjectName("gameLabel")
        self.correctAnswerLabel = QtWidgets.QLabel(self.centralwidget)
        self.correctAnswerLabel.setGeometry(QtCore.QRect(10, 130, 381, 30))
        self.correctAnswerLabel.setObjectName("correctAnswerLabel")
        self.solaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.solaceLabel.setGeometry(QtCore.QRect(10, 180, 381, 30))
        self.solaceLabel.setObjectName("solaceLabel")
        self.btn_retry = QtWidgets.QPushButton(self.centralwidget)
        self.btn_retry.setGeometry(QtCore.QRect(145, 230, 111, 30))
        self.btn_retry.setObjectName("btn_retry")
        self.requestLine.hide()
        self.btn_go.hide()
        self.gameLabel.hide()
        self.correctAnswerLabel.hide()
        self.solaceLabel.hide()
        self.btn_retry.hide()
        #style
        #QtGui.QFontDatabase.addApplicationFont('OldSoviet.otf')
        stylesheetForButtons = """
            QPushButton{
                background-color: #3B3B3B;
                border: none;
                border: 1px solid #303030;
                border-top: 1px solid #353535;
                border-radius: 7px;
                color: #E1E1E1;
                font-size: 15px;
            }
            QPushButton::hover{background-color: #323232;color: #C8C8C8;}
            """
        stylesheetForLabelsAndLines = """
            background-color: #3B3B3B;
            border: 1px solid #303030;
            border-radius: 10px;
            color: #E1E1E1;
            font-size: 15px;
            padding: 5px;
            """
        self.btn_OGE.setStyleSheet(stylesheetForButtons)
        self.btn_EGE.setStyleSheet(stylesheetForButtons)
        self.btn_All.setStyleSheet(stylesheetForButtons)
        self.btn_Back.setStyleSheet("""
            QPushButton{
                background-color: #604040;
                border: none;
                border: 1px solid #5A3C3C;
                border-top: 1px solid #644343;
                border-radius: 5px;
                color: #E1E1E1;
                font-size: 15px;
                padding-right: 10px;
            }
            QPushButton::hover{background-color: #553939;color: #C8C8C8;}
        """)
        self.requestLine.setStyleSheet(stylesheetForLabelsAndLines)
        self.btn_go.setStyleSheet(stylesheetForButtons)       
        self.gameLabel.setStyleSheet(stylesheetForLabelsAndLines + 'font-size: 20px;')
        self.correctAnswerLabel.setStyleSheet(stylesheetForLabelsAndLines)
        self.solaceLabel.setStyleSheet(stylesheetForLabelsAndLines)
        self.btn_retry.setStyleSheet(stylesheetForButtons)
        #create shortcuts
        # self.shortcut_open = QtWidgets.QShortcut(QKeySequence('ENTER', self))
        # self.pushButtonGood.clicked.connect(self.setFocus())

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ChemistryGames"))
        mainWindow.setWhatsThis(_translate("mainWindow", "<html><head/><body><p>It\'s Game</p></body></html>"))
        self.btn_OGE.setText(_translate("mainWindow", "ОГЭ"))
        self.btn_EGE.setText(_translate("mainWindow", "ЕГЭ"))
        self.btn_All.setText(_translate("mainWindow", "Весь список"))
        self.btn_Back.setText(_translate("mainWindow", "< Назад"))
        self.btn_go.setText(_translate("mainWindow", "Погнали!"))
        self.btn_retry.setText(_translate("mainWindow", "Ещё раз!?"))
        # self.gameLabel.setText(_translate("mainWindow", ""))
        self.actionprecipitation_colors.setText(_translate("mainWindow", "precipitation_colors"))

    def addFunctions(self):
        self.btn_All.clicked.connect(lambda: self.MainProtocol(self.btn_All.objectName()))
        self.btn_OGE.clicked.connect(lambda: self.MainProtocol(self.btn_OGE.objectName()))
        self.btn_EGE.clicked.connect(lambda: self.MainProtocol(self.btn_EGE.objectName()))
        self.btn_Back.clicked.connect(self.BackToMainMenu)
        self.btn_go.clicked.connect(self.checkRequest)
        self.btn_retry.clicked.connect(self.retry)

    def BackToMainMenu(self):
        # keyboard.remove_hotkey('enter')
        self.btn_Back.hide()
        self.gameLabel.hide()
        self.btn_All.show()
        self.btn_OGE.show()
        self.btn_EGE.show()
        if not self.requestLine.isHidden():
            self.requestLine.hide()
            self.btn_go.hide()
        if not self.solaceLabel.isHidden():
            self.solaceLabel.hide()
            self.btn_retry.hide()
            self.correctAnswerLabel.hide()
        

    def MainProtocol(self, protocol_variant):
        self.last_protocol_variant = protocol_variant
        # keyboard.add_hotkey('enter', self.checkRequest)
        #hiding buttons
        self.btn_All.hide()
        self.btn_OGE.hide()
        self.btn_EGE.hide()

        #showing back button and game menu
        self.requestLine.setFocus(True)
        self.requestLine.setEnabled(True)
        self.btn_go.setEnabled(True)
        self.requestLine.clear()
        self.btn_Back.show()
        self.requestLine.show()
        self.btn_go.show()
        self.gameLabel.show()
        
        #creating protocol_file_list
        if protocol_variant == 'btn_All':
            with open('FullProtocol.txt', 'rt', encoding="utf-8") as f:
                protocol_file = f.read()
                self.protocol_file_list = protocol_file.split('\n')
        elif protocol_variant == 'btn_OGE':
            with open('OGEProtocol.txt', 'rt', encoding="utf-8") as f:
                protocol_file = f.read()
                self.protocol_file_list = protocol_file.split('\n')
        elif protocol_variant == 'btn_EGE':
            with open('EGEProtocol.txt', 'rt', encoding="utf-8") as f:
                protocol_file = f.read()
                self.protocol_file_list = protocol_file.split('\n')
        #collect and print precipitation
        self.index = randrange(0, len(self.protocol_file_list)-1, 2)
        self.gameLabel.setText(self.protocol_file_list[self.index])

    def checkRequest(self):
        # keyboard.remove_hotkey('enter')
        self.requestLine.setFocus(False)
        if self.requestLine.text().lower() == self.protocol_file_list[self.index + 1].lower():
            self.solaceLabel.setText('Всё верно! Молодец!')
            self.requestLine.setEnabled(False)
            self.btn_go.setEnabled(False)
        else:
            self.solaceLabel.setText('Почти верно. Не переживай, ты ещё учишься!')    
            self.correctAnswerLabel.setText('Правильный ответ: ' + self.protocol_file_list[self.index + 1]) 
            self.correctAnswerLabel.show()
            self.requestLine.hide()
            self.btn_go.hide()
        self.solaceLabel.show()
        self.btn_retry.show()
        # keyboard.add_hotkey('enter', self.retry)
    
    def retry(self):
        # keyboard.remove_hotkey('enter')
        self.solaceLabel.hide()
        self.btn_retry.hide()
        self.correctAnswerLabel.hide()
        # self.requestLine.clear()
        # self.requestLine.setEnabled(True)
        # self.btn_go.setEnabled(True)
        self.MainProtocol(self.last_protocol_variant)
        # keyboard.add_hotkey('enter', self.checkRequest)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())