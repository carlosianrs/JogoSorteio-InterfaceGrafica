from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jogo(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 505)
        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 241, 41))
        self.label.setStyleSheet("font: 75 17pt \"Verdana\";")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 110, 271, 20))
        self.label_5.setStyleSheet("color: rgb(0, 170, 255);\n"
"font: 75 8pt \"Tusker Grotesk 8700 Bold\";")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 180, 161, 51))
        self.label_4.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 230, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 400, 181, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 10pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 270, 171, 20))
        self.label_2.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(211, 211, 211);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 310, 211, 20))
        self.label_3.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(211, 211, 211);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 350, 211, 20))
        self.label_6.setStyleSheet("font: 10pt \"Verdana\";\n"
"background-color: rgb(211, 211, 211);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_5.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jogo de Adivinhação"))
        self.label.setText(_translate("Dialog", "Jogo de Adivinhação"))
        self.label_5.setText(_translate("Dialog", "______________________________________"))
        self.label_4.setText(_translate("Dialog", "Qual o seu palpite?"))
        self.pushButton.setText(_translate("Dialog", "Enviar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_jogo()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
