#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:38:02 2023

@author: murat
"""


import sys 

import random

from datetime import datetime

import requests

from bs4 import BeautifulSoup

import time

from PyQt5.QtWidgets import *

from login import *

from KullanıcıData import *

from Ykayit import *

from sifremiUnuttum import *

from menu import *

from paraYatir import *

from paraCekme import *

from paraGonder import *

from dovizIslemleri import *


kullanici = KullaniciIslemler()

app = QApplication(sys.argv)

pencere = QMainWindow()

ui = Ui_KullaniciGirisEkrani()

ui.setupUi(pencere)

pencere.show()


Form = QtWidgets.QWidget()
yui = Ui_KayitEkrani()
yui.setupUi(Form)

sifreSorun = QtWidgets.QWidget()
sui = Ui_sifremiUnuttumSC()
sui.setupUi(sifreSorun)

menu = QtWidgets.QWidget()
mui = Ui_anaMenu()
mui.setupUi(menu)

yatir = QtWidgets.QWidget()
pyui = Ui_paraYatir()
pyui.setupUi(yatir)

cekme = QtWidgets.QWidget()
cyui = Ui_paraCekme()
cyui.setupUi(cekme)

gonder = QtWidgets.QWidget()
gyui = Ui_paraGonder()
gyui.setupUi(gonder)

donustur = QtWidgets.QWidget()
dyui = Ui_paraDonustur()
dyui.setupUi(donustur)

def giris(menuScreen,firstScreen):
    
    kullaniciAdi = ui.lneKullaniAd.text()
    kullaniciSifre = ui.lneKullaniciSifre.text()
    
    if kullanici.kullaniciGiris(kullaniciAdi, kullaniciSifre):
        
       ui.statusBar.showMessage("Başarılı Giriş",3000)
       firstScreen.hide()
       
       for i in kullanici.kullaniciBilgileri(kullaniciAdi):
           
           an = datetime.now()
           
           mui.labelKullaniciAdi.setText(i[0])
           mui.labelKullaniciSoyadi.setText(i[1])
           mui.labelIban.setText(str(i[3]))
           mui.labelTLnakit.setText(str(i[4]))      
           mui.labelDolarnakit.setText(str(i[5]))
           mui.labelTarih.setText(datetime.strftime(an, '%d %B %Y'))
       
       
       
       menuScreen.show()
       pencere.hide()

    else:
       ui.statusBar.showMessage("Başarısız Giriş",3000)
    
    
    

   
def Kayıt():
  
    yKullaniciAdi = yui.lneYKadi.text()
    yKullaniciSoyadi = yui.lneYKsoyadi.text()
    yKullaniciSifre = yui.lneYKsifre.text()
    IBAN = random.randint(0, 100000)
    yKullanicitlBakiye = float(yui.lneYKtlbakiye.text())
    yKullaniciDollarBakiye = float(yui.lneYKdovizbakiye.text())
    yKullaniciTC  = yui.lneYKtc.text()
    
    
    
    yeniKullanici = Kullanici(yKullaniciAdi,yKullaniciSoyadi ,yKullaniciSifre, IBAN,yKullanicitlBakiye, yKullaniciDollarBakiye,yKullaniciTC)
    
    kullanici.kullaniciKayit(yeniKullanici)

    yui.labelDurum.setText("Kayıt Başarılı")
  
def geri(secondScreen,firstScreen):

    
    secondScreen.hide()
    firstScreen.show()



def yeniSifre():
   
    
    yeniSifreKullaniciAdi = sui.lneSYadi.text()
    yeniSifreKullaniciTC = sui.lneSYtc.text()
    yeniSifreKullaniciSifre = sui.lneSYyenisifre.text()
    yeniSifreKullaniciSifre2 = sui.lneSYyenisifre2.text()
    if yeniSifreKullaniciSifre == yeniSifreKullaniciSifre2:
        
        kullanici.sifreYenile(yeniSifreKullaniciTC, yeniSifreKullaniciSifre)
        
        sui.labelSifreDurum.setText("Başarılı")
        
    else:
        sui.labelSifreDurum.setText("Başarısız")
        
def menuyeGeri(secondScreen,firstScreen):
    
    for i in kullanici.kullaniciBilgileri(mui.labelKullaniciAdi.text()):
        
        mui.labelKullaniciAdi.setText(i[0])
        mui.labelKullaniciSoyadi.setText(i[1])
        mui.labelIban.setText(i[3])
        mui.labelTLnakit.setText(str(i[4]))
        mui.labelDolarnakit.setText(str(i[5]))
    
    secondScreen.hide()
    firstScreen.show()


def paraYatirEkrani(yatirScreen,menuScreen):
    
    menuScreen.hide()
    yatirScreen.show()

def screen(openScreen,closeScreen):
    
    openScreen.show()
    closeScreen.hide()
    
def paraYatir():
    
    
    paraTuru = pyui.cmParaTuru.currentText()
    paraMiktari = float(pyui.lnParaMiktari.text())
    ilkTL = float(mui.labelTLnakit.text())
    ilkDoviz = float(mui.labelDolarnakit.text())
    tc = pyui.lnTC.text()
    
    kullanici.paraYatirf(ilkTL, ilkDoviz, paraTuru, paraMiktari, tc)
    pyui.labelDurum.setText("Başarılı")

def paraCek():
    paraTuru = cyui.cmParaTuru.currentText()
    paraMiktari = float(cyui.lnParaMiktari.text())
    ilkTL = float(mui.labelTLnakit.text())
    ilkDoviz = float(mui.labelDolarnakit.text())
    tc = cyui.lnTC.text()
    
    cyui.labelDurum.setText(kullanici.paraCekf(ilkTL, ilkDoviz, paraTuru, paraMiktari, tc))

def GonderPara():
    
    paraTuru = gyui.cmParaTuru.currentText()
    paraMiktari = float(gyui.lnParaMiktari.text())
    ilkTL = float(mui.labelTLnakit.text())
    ilkDoviz = float(mui.labelDolarnakit.text())
    tc = gyui.lnTC.text()
    gidecekIban = gyui.lnGIBAN.text()
    
    gyui.labelDurum.setText(kullanici.paraGonderf(ilkTL, ilkDoviz, paraTuru, paraMiktari, tc, gidecekIban))

def paraDonusturEkran(openScreen,closeScreen):
    
    openScreen.show()
    closeScreen.hide()
    dyui.lcdNumber.setStyleSheet("background-color : green")

    url = "https://www.google.com/finance/quote/USD-TRY"
                
    sayfa = requests.get(url)
                    
    htmlSayfa = BeautifulSoup(sayfa.content,"html.parser")
                    
    dolar = htmlSayfa.find("div",{"class" :"YMlKec fxKbKc"}).getText()
            
    roundDolar = round(float(dolar.replace(",",".")),2)
            
    dyui.lcdNumber.display(str(roundDolar))
            
def dovizHesapla():
    
    tercih1 = dyui.cmParaTuru.currentText()
    tercih2 =dyui.cmParaTuruCevir.currentText()
    if tercih1 == tercih2:
        dyui.labelDurum.setText("Başarısız")
        time.sleep(1.5)
    elif tercih1 == "Dolar":
        url = "https://www.google.com/finance/quote/USD-TRY"
                
        sayfa = requests.get(url)
                
        htmlSayfa = BeautifulSoup(sayfa.content,"html.parser")
                
        dolar = htmlSayfa.find("div",{"class" :"YMlKec fxKbKc"}).getText()
        
        roundDolar = round(float(dolar.replace(",",".")),2)
        
        dyui.lcdNumber.display(str(roundDolar))
        
        gPara = float(dyui.lnParaMiktari.text())
        
        sonuc = gPara * roundDolar
        
        dyui.labelSonuc.setText(str(round(sonuc,2)))
    
    elif tercih1 == "Tl":
        url = "https://www.google.com/finance/quote/USD-TRY"
                
        sayfa = requests.get(url)
                
        htmlSayfa = BeautifulSoup(sayfa.content,"html.parser")
                
        dolar = htmlSayfa.find("div",{"class" :"YMlKec fxKbKc"}).getText()
        
        roundDolar = round(float(dolar.replace(",",".")),2)
        
        Tl = 1/ roundDolar

        
        dyui.lcdNumber.display(str(roundDolar))
        
        gPara = float(dyui.lnParaMiktari.text())
        
        sonuc = gPara * Tl
        
        dyui.labelSonuc.setText(str(round(sonuc,2)))

def dovizDonustur():
    tc = dyui.lnTC.text()
    tercih1 = dyui.cmParaTuru.currentText()
    tercih2 =dyui.cmParaTuruCevir.currentText()
    if tercih1 == tercih2:
        dyui.labelDurum.setText("Başarısız")
        time.sleep(1.5)
    elif tercih1 == "Dolar":
        url = "https://www.google.com/finance/quote/USD-TRY"
                
        sayfa = requests.get(url)
                
        htmlSayfa = BeautifulSoup(sayfa.content,"html.parser")
                
        dolar = htmlSayfa.find("div",{"class" :"YMlKec fxKbKc"}).getText()
        
        roundDolar = round(float(dolar.replace(",",".")),2)
        
        dyui.lcdNumber.display(str(roundDolar))
        
        gPara = float(dyui.lnParaMiktari.text())
        
        sonuc = gPara * roundDolar
        
        dyui.labelSonuc.setText(str(sonuc))
              
        dyui.labelDurum.setText(kullanici.doviIslemi(tercih1, gPara, sonuc, tc))
    
    elif tercih1 == "Tl":
        url = "https://www.google.com/finance/quote/USD-TRY"
                
        sayfa = requests.get(url)
                
        htmlSayfa = BeautifulSoup(sayfa.content,"html.parser")
                
        dolar = htmlSayfa.find("div",{"class" :"YMlKec fxKbKc"}).getText()
        
        roundDolar = round(float(dolar.replace(",",".")),2)
        
        Tl = 1/ roundDolar

        
        dyui.lcdNumber.display(str(roundDolar))
        
        gPara = float(dyui.lnParaMiktari.text())
        
        sonuc = gPara * Tl
        
        dyui.labelSonuc.setText(str(sonuc))
        
        dyui.labelDurum.setText(kullanici.doviIslemi(tercih1, gPara, sonuc, tc))
       
    
    
    

#buttonlar
ui.pbGiris.clicked.connect(lambda : giris(menu,pencere))
ui.pbYeniKayt.clicked.connect(lambda : screen(Form,pencere))
ui.pbSorunSifre.clicked.connect(lambda : screen(sifreSorun,pencere))
yui.pbKayit.clicked.connect(Kayıt)
yui.pbGeri.clicked.connect(lambda : geri(Form,pencere))
sui.pbYenile.clicked.connect(yeniSifre)
sui.pbGeri.clicked.connect(lambda : geri(sifreSorun,pencere))
mui.pbGeri.clicked.connect(lambda :screen(pencere, menu))
mui.pbParaYatir.clicked.connect(lambda : screen(yatir,menu))
pyui.pbGeri.clicked.connect(lambda : menuyeGeri(yatir, menu))
pyui.pbParaYatir.clicked.connect(paraYatir)
mui.pbParaCek.clicked.connect(lambda : screen(cekme,menu))
cyui.pbParaCek.clicked.connect(paraCek)
cyui.pbGeri.clicked.connect(lambda : menuyeGeri(cekme, menu))
mui.pbParaGonder.clicked.connect(lambda : screen(gonder, menu))
gyui.pbGeri.clicked.connect(lambda : menuyeGeri(gonder, menu))
gyui.pbParaGonder.clicked.connect(GonderPara)
mui.pbDovizIslemi.clicked.connect(lambda : paraDonusturEkran(donustur, menu))
dyui.pbHesapla.clicked.connect(dovizHesapla)
dyui.pbGeri.clicked.connect(lambda : menuyeGeri(donustur, menu))
dyui.pbParaDonustur.clicked.connect(dovizDonustur)




sys.exit(app.exec_())
