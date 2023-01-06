# -*- coding:utf-8 -*-
#Nuosekliai, papunkčiui, pagal duotą UNIT testą sukurti programą, skaičiuojančią KMI:
def kmi(svoris, ugis):
    if svoris < 30:
        raise ValueError("Svoris per mažas")
    if svoris > 200:
        raise ValueError("Svoris per didelis")
    if ugis < 1.0:
        raise ValueError("Ūgis per mažas")
    if ugis > 3.0:
        raise ValueError("Ūgis per didelis")
    return svoris / (ugis**2)
  
  #output
  Process finished with exit code 0
