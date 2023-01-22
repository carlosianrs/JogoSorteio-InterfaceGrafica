from ctypes import pointer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from random import randint
import os, sys

from jogo import Ui_jogo
from tentativas import Ui_tentativas
from jogar import Ui_jogar

class jogar(QDialog):
    def __init__(self,*args,**argvs):
        super(jogar,self).__init__(*args,**argvs)
        self.ui = Ui_jogar()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.comecar)

    def comecar(self):
        self.window = tentativas()
        self.window.show()

class tentativas(QDialog):
    def __init__(self,*args,**argvs):
        super(tentativas,self).__init__(*args,**argvs)
        self.ui = Ui_tentativas()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.tentar)

    def tentar(self):
        global dado_lido
        global pont
        pont = 0
        dado_lido = int(self.ui.lineEdit.text())
        print(dado_lido)
        if dado_lido <= 0:
            QMessageBox.information(QMessageBox(),"Alerta","O número mínimo de jogadas é 1")
        else:
            QMessageBox.information(QMessageBox(),"Boa sorte","Você terá: "+ str(dado_lido) + " tentativas")
            self.window = jogo()
            self.window.show()

class jogo(QDialog):
    def __init__(self,*args,**argvs):
        super(jogo,self).__init__(*args,**argvs)
        self.ui = Ui_jogo()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sortear)

    def sortear(self):
        global cal
        global dado_lido
        global calc
        global pont
        cal = dado_lido
        dado_lido = cal - 1
        num = int(self.ui.lineEdit.text())
        self.ui.lineEdit.setText("")
        numeros = randint(1, 10)
        if num > 10:
            QMessageBox.information(QMessageBox(),"Alerta","O valor está entre 1 e 10")
            self.ui.label_2.setText("Tentativas: "+ str(dado_lido))
            self.ui.label_3.setText("Você errou")
            self.ui.label_6.setText("O número sorteado foi: "+ str(numeros))
        elif num <= 0:
            QMessageBox.information(QMessageBox(),"Alerta","O valor está entre 1 e 10")
            self.ui.label_2.setText("Tentativas: "+ str(dado_lido))
            self.ui.label_3.setText("Você errou")
            self.ui.label_6.setText("O número sorteado foi: "+ str(numeros))
        else:
            if num != numeros:
                if pont > 0:
                    calc = pont
                    pont = calc - 1
                    self.ui.label_2.setText("Tentativas: "+ str(dado_lido))
                    self.ui.label_3.setText("Errou, perdeu 1 ponto")
                    self.ui.label_6.setText("O número sorteado foi: "+ str(numeros))
                    if dado_lido == 0:
                        QMessageBox.information(QMessageBox(),"Obrigado por jogar","Sua pontuação foi: "+ str(pont))
                        self.close()
                else:
                    self.ui.label_2.setText("Tentativas: "+ str(dado_lido))
                    self.ui.label_3.setText("Você errou")
                    self.ui.label_6.setText("O número sorteado foi: "+ str(numeros))
                    if dado_lido == 0:
                        QMessageBox.information(QMessageBox(),"Obrigado por jogar","Sua pontuação foi: "+ str(pont))
                        self.close()
            else:
                calc = pont
                pont = calc + 3
                self.ui.label_2.setText("Tentativas: "+ str(dado_lido))
                self.ui.label_3.setText("Acertou, você ganhou 3 pontos"+ str(pont))
                self.ui.label_6.setText("O número sorteado foi: "+ str(numeros))
                if dado_lido == 0:
                    QMessageBox.information(QMessageBox(),"Obrigado por jogar","Sua pontuação foi: "+ str(pont))
                    self.close()
        
app = QApplication(sys.argv)
if (QDialog.Accepted == True): 
    window = jogar()
    window.show()
sys.exit(app.exec_())