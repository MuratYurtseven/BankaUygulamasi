# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sifremiUnuttum.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sifremiUnuttumSC(object):
    def setupUi(self, sifremiUnuttumSC):
        sifremiUnuttumSC.setObjectName("sifremiUnuttumSC")
        sifremiUnuttumSC.resize(424, 550)
        self.pbGeri = QtWidgets.QPushButton(sifremiUnuttumSC)
        self.pbGeri.setGeometry(QtCore.QRect(170, 350, 100, 32))
        self.pbGeri.setObjectName("pbGeri")
        self.pbYenile = QtWidgets.QPushButton(sifremiUnuttumSC)
        self.pbYenile.setGeometry(QtCore.QRect(140, 300, 161, 32))
        self.pbYenile.setObjectName("pbYenile")
        self.labelSifreDurum = QtWidgets.QLabel(sifremiUnuttumSC)
        self.labelSifreDurum.setGeometry(QtCore.QRect(190, 270, 151, 20))
        self.labelSifreDurum.setText("")
        self.labelSifreDurum.setObjectName("labelSifreDurum")
        self.layoutWidget = QtWidgets.QWidget(sifremiUnuttumSC)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 90, 111, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.layoutWidget1 = QtWidgets.QWidget(sifremiUnuttumSC)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 90, 171, 121))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lneSYadi = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lneSYadi.setObjectName("lneSYadi")
        self.verticalLayout_2.addWidget(self.lneSYadi)
        self.lneSYtc = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lneSYtc.setObjectName("lneSYtc")
        self.verticalLayout_2.addWidget(self.lneSYtc)
        self.lneSYyenisifre = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lneSYyenisifre.setObjectName("lneSYyenisifre")
        self.verticalLayout_2.addWidget(self.lneSYyenisifre)
        self.lneSYyenisifre2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lneSYyenisifre2.setObjectName("lneSYyenisifre2")
        self.verticalLayout_2.addWidget(self.lneSYyenisifre2)

        self.retranslateUi(sifremiUnuttumSC)
        QtCore.QMetaObject.connectSlotsByName(sifremiUnuttumSC)

    def retranslateUi(self, sifremiUnuttumSC):
        _translate = QtCore.QCoreApplication.translate
        sifremiUnuttumSC.setWindowTitle(_translate("sifremiUnuttumSC", "Form"))
        self.pbGeri.setText(_translate("sifremiUnuttumSC", "Geri"))
        self.pbYenile.setText(_translate("sifremiUnuttumSC", "Yenile"))
        self.label.setText(_translate("sifremiUnuttumSC", "Kullanici Adi"))
        self.label_2.setText(_translate("sifremiUnuttumSC", "Kullanici TC"))
        self.label_3.setText(_translate("sifremiUnuttumSC", "Yeni Şifre"))
        self.label_4.setText(_translate("sifremiUnuttumSC", "Yeni Şifre"))
