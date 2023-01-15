#!/usr/bin/env python
from cezeri_lib.cezeri import Cezeri
import rospy
import math
import time

def aciHesaplama(x,y,hedef_x,hedef_y):
    yeni_y = hedef_y - y 
    yeni_x = hedef_x - x
    myradians = math.atan2(yeni_y, yeni_x)
    return myradians



class arac:
    def __init__(self,cezeri):
        self.cezeri = cezeri
        self.mesafelerlistesi = []

    
    
    @classmethod
    def hedefMesafeHesaplama(self,guncel_x,guncel_y,hedef_x,hedef_y):
        yeni_x = (hedef_x - guncel_x) ** 2
        yeni_y = (hedef_y - guncel_y) ** 2
        mesafe =  math.sqrt((yeni_x + yeni_y))
        return mesafe

        
    def start(self):
        hedef_x = self.cezeri.hedefler[0].bolge.enlem
        hedef_y = self.cezeri.hedefler[0].bolge.boylam
        self.guncel_x = self.cezeri.gnss.enlem
        self.guncel_y = self.cezeri.gnss.boylam
        self.cezeri.don(aciHesaplama(self.guncel_x,self.guncel_y,hedef_x,hedef_y))
        self.cezeri.bekle(3.14)
        while self.cezeri.aktif():
            self.guncel_x = self.cezeri.gnss.enlem
            self.guncel_y = self.cezeri.gnss.boylam
            if self.guncel_x == hedef_x and self.guncel_y == hedef_y:
                self.cezeri.dur()
                self.cezeri.asagi_git(self.cezeri.YAVAS)
            else:
                if(self.cezeri.gnss.irtifa > (self.cezeri.irtifa_araligi[0]+self.cezeri.irtifa_araligi[1])/2):
                    self.cezeri.asagi_git(self.cezeri.HIZLI)
                else:
                    self.cezeri.yukari_git(self.cezeri.HIZLI)
                self.cezeri.ileri_git(self.cezeri.HIZLI)
           



p1 = arac(Cezeri('TUFU TEAM'))
p1.start()
