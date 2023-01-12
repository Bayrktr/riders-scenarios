#!/usr/bin/env python
from cezeri_lib.cezeri import Cezeri
import rospy
import math
import time



class matematikIslemleri:

    @classmethod
    def egimhesaplama(guncel_x,guncel_y,gidilecek_x,gidilecek_y):
        yeni_y = hedef_y - y 
        yeni_x = hedef__x - x
        egim = math.atan2(yeni_y,yeni_x)
        sonuc = egim * (180/math.pi)
        return sonuc
    
    @classmethod
    def hedefMesafeHesaplama(self,guncel_x,guncel_y,hedef_x,hedef_y):
        yeni_x = (hedef_x - guncel_x) ** 2
        yeni_y = (hedef_y - guncel_y) ** 2
        mesafe =  math.sqrt((yeni_x + yeni_y))
        return mesafe



class arac:
    def __init__(self,cezeri):
        self.cezeri = cezeri
        self.hedefler = self.cezeri.hedefler
        self.mesafelerlistesi = []
        self.kordinatlarListesi = []

    
    def hedef(self):
        for x in self.hedefler:
            self.kordinatlarListesi.append([self.guncel_x,self.guncel_y])
            self.mesafelerlistesi.append(matematikIslemleri.hedefMesafeHesaplama(self.guncel_x,self.guncel_y,x.bolge.enlem,x.bolge.boylam))
        
        print(self.mesafelerlistesi)
        print(self.kordinatlarListesi)


    def start(self):
        while self.cezeri.aktif():
            print("saa")
            self.guncel_x = self.cezeri.gnss.enlem
            self.guncel_y = self.cezeri.gnss.boylam
            self.hedef()



p1 = arac(Cezeri(rapor = False))
p1.start()
