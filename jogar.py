from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jogar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 465)
        Dialog.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 271, 41))
        self.label_2.setStyleSheet("color: rgb(0, 170, 255);\n"
"font: 75 8pt \"Tusker Grotesk 8700 Bold\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 80, 241, 41))
        self.label.setStyleSheet("font: 75 17pt \"Verdana\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 170, 221, 31))
        self.label_3.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 220, 301, 41))
        self.label_4.setStyleSheet("font: 12pt \"Verdana\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 300, 171, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 10pt \"Verdana\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jogo de Adivinhação"))
        self.label_2.setText(_translate("Dialog", "______________________________________"))
        self.label.setText(_translate("Dialog", "Jogo de Adivinhação"))
        self.label_3.setText(_translate("Dialog", "Vou pensar em um número"))
        self.label_4.setText(_translate("Dialog", "Quero ver se você consegue acertar"))
        self.pushButton.setText(_translate("Dialog", "Jogar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_jogar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
