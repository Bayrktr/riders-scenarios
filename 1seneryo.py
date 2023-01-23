#!/usr/bin/env python
from cezeri_lib.cezeri import Cezeri
import rospy
import math
import time


Hedef_dogrultusu = False



def aciHesaplama(x,y,hedef_x,hedef_y):
    yeni_y = hedef_y - y 
    yeni_x = hedef_x - x#!/usr/bin/env python
from cezeri_lib.cezeri import Cezeri
import rospy
import math
import time


Hedef_dogrultusu = False



def aciHesaplama(x,y,hedef_x,hedef_y):
    yeni_y = hedef_y - y 
    yeni_x = hedef_x - x
    egim = math.atan2(yeni_y,yeni_x)
    
    #sonuc = egim * (math.pi/180)    
    dogrultu = abs((egim-cezeri.manyetometre.veri)*180/math.pi)

    if x > yeni_x and y > yeni_y:
        dogrultu = dogrultu
    elif x > yeni_x and y > yeni_y:
        dogrultu = dogrultu
    elif x < yeni_x and y < yeni_y:
        dogrultu = -dogrultu
    elif x < yeni_x and y > yeni_y:
        dogrultu = -dogrultu

    print(dogrultu)
        
    return dogrultu


cezeri = Cezeri(rapor = True)
cezeri.klavye = False
print(cezeri.manyetometre.veri)
guncel_x = cezeri.gnss.enlem
guncel_y = cezeri.gnss.boylam
print (guncel_x,guncel_y)
hedef = cezeri.hedefler[0]
print(hedef.bolge.enlem, hedef.bolge.boylam)
print (cezeri.irtifa_araligi[0])
print (cezeri.irtifa_araligi[1])
print (cezeri.zaman)
for x in cezeri.harita.hastaneler:
    print("{}\n".format(x))
#aciHesaplama(guncel_x,guncel_y,hedef.bolge.enlem,hedef.bolge.boylam)




while cezeri.aktif():
    hedef = cezeri.hedefler[0]
    hedef_x = hedef.bolge.enlem
    hedef_y = hedef.bolge.boylam

    guncel_x = cezeri.gnss.enlem
    guncel_y = cezeri.gnss.boylam

    boylam_fark = abs(hedef_y - guncel_y )


    if aciHesaplama(guncel_x,guncel_y,hedef_x,hedef_y) >= 2.5 and boylam_fark >= 6 :
        if boylam_fark >= 6:
            cezeri.don(-0.08)
    else:
        cezeri.dur()   
        if cezeri.gnss.irtifa <= cezeri.irtifa_araligi[0] and hedef.bolge.enlem - guncel_x > 0.2:
            cezeri.yukari_git(cezeri.ORTA)
        elif cezeri.gnss.irtifa > cezeri.irtifa_araligi[1] and hedef.bolge.enlem - guncel_x > 0.2:
            cezeri.asagi_git(cezeri.ORTA)
        elif cezeri.gnss.irtifa > cezeri.irtifa_araligi[0] and hedef.bolge.enlem - guncel_x > 0.2:
            cezeri.dur()
        # if  cezeri.irtifa_araligi[1] > cezeri.gnss.irtifa and cezeri.irtifa_araligi[0] < cezeri.gnss.irtifa and hedef.bolge.enlem - guncel_x > 0 and hedef.bolge.boylam - guncel_y < 0:
            cezeri.ileri_git(cezeri.ORTA)
        elif hedef.bolge.enlem - guncel_x < 0.2 and cezeri.radar.mesafe > 0:
            cezeri.dur()
            cezeri.asagi_git(cezeri.YAVAS)
    
    #print(cezeri.manyetometre.veri)
        
   

for hedef in cezeri.hedefler:
    print (hedef)
