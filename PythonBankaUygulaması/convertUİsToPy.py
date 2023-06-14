#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 01:02:58 2023

@author: murat
"""

from PyQt5 import uic

with open("login.py","w",encoding="utf-8") as file:
    
    uic.compileUi("login.ui", file)

with open("Ykayit.py","w",encoding="utf-8") as file:
    
    uic.compileUi("kayit.ui", file)

with open("sifremiUnuttum.py","w",encoding="utf-8") as file:
    
    uic.compileUi("sifremiUnuttum.ui", file)

with open("menu.py","w",encoding="utf-8") as file:
    
    uic.compileUi("Menu.ui",file)

with open("paraYatir.py","w",encoding= "utf-8") as file:
    
    uic.compileUi("paraYatir.ui", file)

with open("paraCekme.py","w",encoding = "utf-8") as file:
    
    uic.compileUi("paraCek.ui", file)

with open("paraGonder.py","w",encoding="utf-8") as file:
    uic.compileUi("paraGonder.ui",file)


with open("dovizIslemleri.py","w",encoding="utf-8") as file:
    uic.compileUi("dovizIslemleri.ui", file)



