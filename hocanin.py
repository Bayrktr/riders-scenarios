#!/usr/bin/env python
from cezeri_lib.cezeri import Cezeri
import rospy
import math
import time


def aciHesaplama(guncel_x,guncel_y,hedef_x,hedef_y):
    yeni_y = hedef_y - y 
    yeni_x = hedef_x - x
    egim = abs(yeni_y / yeni_x)
    carpan = 1
    sure = 0
    if yeni_y > 0 and yeni_x > 0:
    carpan = 1
    sure = math.atan2(egim)
    elif yeni_y > 0 and yeni_x < 0:
    carpan = 1
    sure = math.pi - math.atan2(egim)
    elif yeni_y < 0 and yeni_x < 0:
    carpan = -1
    sure = math.pi - math.atan2(egim)
    elif yeni_y < 0 and yeni_x > 0:
    carpan = -1
    sure = math.pi - math.atan2(egim)
    return sure
    #return sonuc

cezeri = Cezeri(rapor = True)
cezeri.klavye = False
guncel_x = cezeri.gnss.enlem
guncel_y = cezeri.gnss.boylam
print (guncel_x,guncel_y)
hedef = cezeri.hedefler[0]
print(hedef.bolge.enlem, hedef.bolge.boylam)
print (cezeri.irtifa_araligi[0])
print (cezeri.irtifa_araligi[1])
cezeri.don(carpan)
print (cezeri.zaman)
cezeri.bekle(sure)
print (cezeri.zaman)
cezeri.dur()
print (cezeri.zaman)
for x in cezeri.harita.hastaneler:
    print("{}\n".format(x))

while cezeri.aktif():
    hedef = cezeri.hedefler[0]
    hedef_x = hedef.bolge.enlem
    hedef_y = hedef.bolge.boylam

    guncel_x = cezeri.gnss.enlem
    guncel_y = cezeri.gnss.boylam

    aciHesaplama(guncel_x,guncel_y,hedef_x,hedef_y)

    if cezeri.gnss.irtifa <= cezeri.irtifa_araligi[0] and hedef.bolge.enlem - guncel_x > 0:
        cezeri.yukari_git(cezeri.ORTA)
    elif cezeri.gnss.irtifa > cezeri.irtifa_araligi[1] and hedef.bolge.enlem - guncel_x > 0:
        cezeri.asagi_git(cezeri.ORTA)
    elif cezeri.gnss.irtifa > cezeri.irtifa_araligi[0] and hedef.bolge.enlem - guncel_x > 0 :
        cezeri.dur()
       # if  cezeri.irtifa_araligi[1] > cezeri.gnss.irtifa and cezeri.irtifa_araligi[0] < cezeri.gnss.irtifa and hedef.bolge.enlem - guncel_x > 0 and hedef.bolge.boylam - guncel_y < 0:
        cezeri.ileri_git(cezeri.ORTA)
    elif hedef.bolge.enlem - guncel_x <= 0 and cezeri.radar.mesafe > 0:
        cezeri.dur()
        cezeri.asagi_git(cezeri.YAVAS)

for hedef in cezeri.hedefler:
    print (hedef)
