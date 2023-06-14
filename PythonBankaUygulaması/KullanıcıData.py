#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:55:47 2023

@author: murat
"""



import sqlite3



class Kullanici():
    
    
    def __init__(self,kullaniciAdi,kullaniciSoyadi,kullaniciSifre,kullaniciIBAN,kullaniciBakiye,kullaniciDoviz,kullaniciTC):
        
        self.kullaniciAdi = kullaniciAdi
        self.kullaniciSoyadi = kullaniciSoyadi
        self.kullaniciSifre = kullaniciSifre
        self.kullaniciIBAN = kullaniciIBAN
        self.kullaniciBakiye = kullaniciBakiye
        self.kullaniciDoviz = kullaniciDoviz
        self.kullaniciTC = kullaniciTC
        
    
class KullaniciIslemler():
    
    def __init__(self):
        
        self.createConn()

    def createConn(self):
        
        self.conn = sqlite3.connect("Kullanicilar.db")
        self.cursor = self.conn.cursor()
        query = "Create table if not exists kullanicilar (KullanıcıAdı TEXT,KullanıcıSoyadı TEXT,KullanıcıŞifre TEXT,KullanıcıIBAN TEXT,KullanıcıBakiye FLOAT,KullanıcıDöviz FLOAT,KullanıcıTC TEXT)"
        
        self.cursor.execute(query)
        self.conn.commit()
        
    def disconn(self):
        
        self.conn.close()
    
    def kullaniciKayit(self,kullanici):
        

        query = "Insert into kullanicilar Values (?,?,?,?,?,?,?)"
        
        self.cursor.execute(query,(kullanici.kullaniciAdi,kullanici.kullaniciSoyadi,kullanici.kullaniciSifre,kullanici.kullaniciIBAN,kullanici.kullaniciBakiye,kullanici.kullaniciDoviz,kullanici.kullaniciTC))
        
        self.conn.commit()
        
    def kullaniciGiris(self,ad,sifre):
        
        query = "Select * from kullanicilar"
        self.cursor.execute(query)
        kullaniciListe = self.cursor.fetchall()
        
        durum = 0
        for i in kullaniciListe:
            
            if(ad == i[0] and i[2] == sifre):
                durum += 1

                return True
        if durum == 0:
            return False
    
    def sifreYenile(self,tc,yeniSifre):
        
        query = "Update kullanicilar set KullanıcıŞifre = ? where KullanıcıTC = ?"
        
        self.cursor.execute(query,(yeniSifre,tc))
        self.conn.commit()

    def kullaniciBilgileri(self,ad):
        
        query = "Select * from kullanicilar"
        self.cursor.execute(query)
        kullaniciListe = self.cursor.fetchall()
        sonucListe = list()
        for i in kullaniciListe:
            
            if(ad == i[0]):
                for x in range(0,7):
                    sonucListe.append(i[x])
                returnListe=list()
                returnListe.append(sonucListe)
                return returnListe

    def paraYatirf(self,ilkTl,ilkDolar,tur,miktar,tc):
        
        if tur == "Dolar":
            
            ilkDolar += miktar
            
            query = "Update kullanicilar set KullanıcıDöviz = ? where kullanıcıTC = ?"
            
            self.cursor.execute(query,(ilkDolar,tc))
            self.conn.commit()
        
        elif tur == "Tl":
            
            ilkTl += miktar
            
            query = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıTC = ?"
            
            self.cursor.execute(query,(ilkTl,tc))
            self.conn.commit()
            

    def paraCekf(self,ilkTl,ilkDolar,tur,miktar,tc):
        
        if tur == "Dolar":
            
            if miktar>ilkDolar:
                return "Başarısız"
            else:
                ilkDolar -= miktar
                
                query = "Update kullanicilar set KullanıcıDöviz = ? where kullanıcıTC = ?"
                
                self.cursor.execute(query,(ilkDolar,tc))
                self.conn.commit()
                return "Başarılı"
        
        elif tur == "Tl":
            
            if miktar>ilkTl:
                return "Başarısız"
            else:
                
                ilkTl -= miktar
            
                query = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıTC = ?"
                
                self.cursor.execute(query,(ilkTl,tc))
                self.conn.commit()
                return "Başarılı"
        

    def paraGonderf(self,ilkTl,ilkDolar,tur,miktar,tc,iban):
        
        if tur == "Dolar":
            
            if miktar>ilkDolar:
                return "Başarısız"
            else:
                ilkDolar -= miktar
                
                query = "Update kullanicilar set KullanıcıDöviz = ? where kullanıcıTC = ?"
                
                self.cursor.execute(query,(ilkDolar,tc))
                self.conn.commit()
                
                query2 = "Select * from kullanicilar"
                self.cursor.execute(query2)
                liste=self.cursor.fetchall()
                durum = 0
                for i in liste:
                    if i[3] == iban:
                        durum += 1
                        gDolar = i[5] + miktar
                        
                        query3 = "Update kullanicilar set kullanıcıDöviz = ? where kullanıcıIBAN = ?"
                        self.cursor.execute(query3,(gDolar,iban))
                        self.conn.commit()
                        return "Başarılı"
                if durum == 0:
                    return "Başarısız"
        
        elif tur == "Tl":
            
            if miktar>ilkTl:
                return "Başarısız"
            else:
                
                ilkTl -= miktar
            
                query = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıTC = ?"
                
                self.cursor.execute(query,(ilkTl,tc))
                self.conn.commit()
                
                query2 = "Select * from kullanicilar"
                
                self.cursor.execute(query2)
                liste=self.cursor.fetchall()
                durum = 0
                for i in liste:
                    if i[3] == iban:
                        durum +=1
                        gTl = i[4] + miktar
                        
                        query3 = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıIBAN = ?"
                        self.cursor.execute(query3,(gTl,iban))
                        self.conn.commit()
                        return "Başarılı"
                if durum == 0:
                    return "Başarısız"
        
        
        
    def doviIslemi(self,turMiktari,miktar,sonuc,tc):

        query = "Select * from kullanicilar"
        self.cursor.execute(query)
        liste = self.cursor.fetchall()
        durum = 0
        for i in liste:

            if i[6] == tc:
                if turMiktari == "Dolar":
                    if (i[5] >= miktar):
                        durum += 1
                    
                        dSonuc = i[5] - miktar
                        
                        query2 = "Update kullanicilar set kullanıcıDöviz = ? where kullanıcıTC = ?"
                        self.cursor.execute(query2,(dSonuc,tc))
                        self.conn.commit()
                        
                        vSonuc = i[4] + sonuc
                        
                        query3 = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıTC = ?"
                        self.cursor.execute(query3,(round(vSonuc,2),tc))
                        self.conn.commit()
                        return "Başarılı"
                    
                
                if turMiktari == "Tl":
                    if (i[4] >= miktar):
                        durum += 1
                        dSonuc = i[4] - miktar
                        
                        query2 = "Update kullanicilar set kullanıcıBakiye = ? where kullanıcıTC = ?"
                        self.cursor.execute(query2,(dSonuc,tc))
                        self.conn.commit()
    
                        
                        vSonuc = i[5] + sonuc
                        query3 = "Update kullanicilar set kullanıcıDöviz = ? where kullanıcıTC = ?"
                        self.cursor.execute(query3,(round(vSonuc,2),tc))
                        self.conn.commit()
                        
                        return "Başarılı"

                
        if durum ==0:
            return "Başarısız"
        
        
        
        
        
        
        
        
    
