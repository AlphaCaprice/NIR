# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forma3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1300, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 850))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 921, 671))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setMouseTracking(False)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setMidLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1010, 20, 281, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(950, 50, 41, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 80, 41, 22))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(950, 110, 41, 22))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(950, 140, 41, 22))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(950, 170, 41, 22))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(1010, 50, 281, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(1010, 80, 281, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1010, 110, 281, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1010, 140, 281, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(1010, 170, 281, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1010, 200, 281, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(1010, 230, 281, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(1010, 260, 281, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(1010, 290, 281, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(1010, 320, 281, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(1010, 350, 281, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(1010, 380, 281, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_17.setGeometry(QtCore.QRect(1010, 410, 281, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_18.setGeometry(QtCore.QRect(1010, 440, 281, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_19.setGeometry(QtCore.QRect(1010, 470, 281, 22))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_20.setGeometry(QtCore.QRect(1010, 500, 281, 22))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setEnabled(False)
        self.lineEdit_21.setGeometry(QtCore.QRect(950, 230, 41, 22))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setEnabled(False)
        self.lineEdit_22.setGeometry(QtCore.QRect(950, 260, 41, 22))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setEnabled(False)
        self.lineEdit_23.setGeometry(QtCore.QRect(950, 290, 41, 22))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_24.setEnabled(False)
        self.lineEdit_24.setGeometry(QtCore.QRect(950, 320, 41, 22))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_25.setEnabled(False)
        self.lineEdit_25.setGeometry(QtCore.QRect(950, 350, 41, 22))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_26.setEnabled(False)
        self.lineEdit_26.setGeometry(QtCore.QRect(950, 380, 41, 22))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_27.setEnabled(False)
        self.lineEdit_27.setGeometry(QtCore.QRect(950, 410, 41, 22))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_28.setEnabled(False)
        self.lineEdit_28.setGeometry(QtCore.QRect(950, 440, 41, 22))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_29.setEnabled(False)
        self.lineEdit_29.setGeometry(QtCore.QRect(950, 470, 41, 22))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_30.setEnabled(False)
        self.lineEdit_30.setGeometry(QtCore.QRect(950, 500, 41, 22))
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1040, 675, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.answersNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.answersNumber.setGeometry(QtCore.QRect(1240, 600, 51, 22))
        self.answersNumber.setObjectName("answersNumber")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 600, 291, 16))
        self.label_2.setObjectName("label_2")
        self.midSymbol = QtWidgets.QLineEdit(self.centralwidget)
        self.midSymbol.setGeometry(QtCore.QRect(1240, 640, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.midSymbol.setFont(font)
        self.midSymbol.setObjectName("midSymbol")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(950, 640, 291, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(950, 560, 201, 16))
        self.label_6.setObjectName("label_6")
        self.amountOfAnswers = QtWidgets.QComboBox(self.centralwidget)
        self.amountOfAnswers.setEnabled(True)
        self.amountOfAnswers.setGeometry(QtCore.QRect(1242, 560, 51, 22))
        self.amountOfAnswers.setAcceptDrops(False)
        self.amountOfAnswers.setEditable(False)
        self.amountOfAnswers.setObjectName("amountOfAnswers")
        self.amountOfAnswers.addItem("")
        self.amountOfAnswers.addItem("")
        self.amountOfAnswers.addItem("")
        self.amountOfAnswers.addItem("")
        self.amountOfAnswers.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Задача"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Левая часть</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "1)"))
        self.lineEdit_2.setText(_translate("MainWindow", "2)"))
        self.lineEdit_3.setText(_translate("MainWindow", "3)"))
        self.lineEdit_4.setText(_translate("MainWindow", "4)"))
        self.lineEdit_5.setText(_translate("MainWindow", "5)"))
        self.lineEdit_6.setText(_translate("MainWindow", "f_1"))
        self.lineEdit_7.setText(_translate("MainWindow", "f_2"))
        self.lineEdit_8.setText(_translate("MainWindow", "f_3"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Правая часть</p></body></html>"))
        self.lineEdit_11.setText(_translate("MainWindow", "\\oplus"))
        self.lineEdit_12.setText(_translate("MainWindow", "\\downarrow"))
        self.lineEdit_13.setText(_translate("MainWindow", "\\land"))
        self.lineEdit_14.setText(_translate("MainWindow", "\\equiv"))
        self.lineEdit_15.setText(_translate("MainWindow", "\\lor "))
        self.lineEdit_21.setText(_translate("MainWindow", "1)"))
        self.lineEdit_22.setText(_translate("MainWindow", "2)"))
        self.lineEdit_23.setText(_translate("MainWindow", "3)"))
        self.lineEdit_24.setText(_translate("MainWindow", "4)"))
        self.lineEdit_25.setText(_translate("MainWindow", "5)"))
        self.lineEdit_26.setText(_translate("MainWindow", "6)"))
        self.lineEdit_27.setText(_translate("MainWindow", "7)"))
        self.lineEdit_28.setText(_translate("MainWindow", "8)"))
        self.lineEdit_29.setText(_translate("MainWindow", "9)"))
        self.lineEdit_30.setText(_translate("MainWindow", "10)"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Нажмите, чтобы сгенерировать задачу"))
        self.pushButton.setText(_translate("MainWindow", "Создать задачу"))
        self.answersNumber.setText(_translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "Количество показываемых ответов:"))
        self.midSymbol.setToolTip(_translate("MainWindow", "<html><head/><body><p>Символ, который будет вставлен между частями ответов (например, -, . , :)</p></body></html>"))
        self.midSymbol.setText(_translate("MainWindow", "-"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>Символ, который будет вставлен между частями ответов (например, -, . , :)</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Соединяющий символ:"))
        self.label_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>Позволяет создавать пары ответов, тройки и т.д.</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Ответов в одном:"))
        self.amountOfAnswers.setToolTip(_translate("MainWindow", "<html><head/><body><p>Позволяет создавать пары ответов, тройки и т.д.</p></body></html>"))
        self.amountOfAnswers.setItemText(0, _translate("MainWindow", "1"))
        self.amountOfAnswers.setItemText(1, _translate("MainWindow", "2"))
        self.amountOfAnswers.setItemText(2, _translate("MainWindow", "3"))
        self.amountOfAnswers.setItemText(3, _translate("MainWindow", "4"))
        self.amountOfAnswers.setItemText(4, _translate("MainWindow", "5"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

