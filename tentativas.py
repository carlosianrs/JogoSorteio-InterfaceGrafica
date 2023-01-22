from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tentativas(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 463)
        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 80, 281, 41))
        self.label.setStyleSheet("font: 75 17pt \"Verdana\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 110, 271, 20))
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);\n"
"font: 75 8pt \"Tusker Grotesk 8700 Bold\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 271, 51))
        self.label_3.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 240, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 370, 181, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 10pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jogo de Adivinhação"))
        self.label.setText(_translate("Dialog", "Seja-bem-vindo ao jogo"))
        self.label_2.setText(_translate("Dialog", "______________________________________"))
        self.label_3.setText(_translate("Dialog", "Quantas vezes você quer jogar?"))
        self.pushButton.setText(_translate("Dialog", "Começar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_tentativas()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
