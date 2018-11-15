from random import randrange
from util import tah

def tah_pocitace(pole, symbol_pocitace, strategie):
    #vybere nahodne strategii pocitace na zacatku kazde hry, bud brani nebo utoci
    symbol_hrace = None
    if strategie == 0:
        return strategie_utok(pole, symbol_pocitace)
    if strategie == 1:
        if symbol_pocitace == "x":
            symbol_hrace = "o"
            return strategie_obrana(pole, symbol_pocitace, symbol_hrace)
        if symbol_pocitace =="o":
            symbol_hrace = "x"
            return strategie_obrana(pole, symbol_pocitace, symbol_hrace)

def pozice_pocitace(pole,symbol_pocitace):
    #funkce pro nahodne vlozeni symbolu pocitace na nahodnou pozici
    while True: #overi, zda pocitac nechce vlozit symbol na jiz jiny vlozeny symbol
        cislo_pole_pocitace = randrange(0, len(pole))
        if pole[cislo_pole_pocitace] != "-":
            continue
        else:
            return tah(pole, cislo_pole_pocitace, symbol_pocitace)

def strategie_utok(pole, symbol_pocitace):
    #pocitac se snazi napsat tri symboly vedle sebe, nesnazi se zabranit hraci ve vitezstvi
    utok= pole.find("-" + "-"+ symbol_pocitace)
    if utok != - 1:
        return tah(pole, utok + 1, symbol_pocitace)
    utok = pole.find(symbol_pocitace + "-" + "-")
    if utok != - 1:
        return tah(pole, utok + 1, symbol_pocitace)
    utok = pole.find(symbol_pocitace + symbol_pocitace + "-")
    if utok != - 1:
        return tah(pole, utok + 2, symbol_pocitace)
    utok = pole.find("-" + symbol_pocitace + symbol_pocitace)
    if utok != - 1:
        return tah(pole, utok, symbol_pocitace)
    utok = pole.find(symbol_pocitace + "-" + symbol_pocitace)
    if utok != - 1:
        return tah(pole, utok + 1, symbol_pocitace)
    utok = pole.find("-" + "-" + "-")
    if utok != -1:
        return tah(pole, utok + 1, symbol_pocitace)
    if utok == -1:#nenajde jinou moznost, naprd x_o , o_x, -> vrati nahodnou volnou pozici
        return pozice_pocitace(pole, symbol_pocitace)

def strategie_obrana(pole, symbol_pocitace, symbol_hrace):
        #pocitac brani hraci zapsat tri symboly vedle sebe
        obrana = pole.find("-" + "-"+ symbol_hrace)
        if obrana != - 1:
            return tah(pole, obrana + 1, symbol_pocitace)
        obrana = pole.find(symbol_hrace + "-" + "-")
        if obrana != - 1:
            return tah(pole, obrana + 1, symbol_pocitace)
        obrana = pole.find(symbol_hrace + symbol_hrace + "-")
        if obrana != - 1:
            return tah(pole, obrana + 2, symbol_pocitace)
        obrana = pole.find("-" + symbol_hrace + symbol_hrace)
        if obrana != - 1:
            return tah(pole, obrana, symbol_pocitace)
        obrana = pole.find(symbol_hrace + "-" + symbol_hrace)
        if obrana != - 1:
            return tah(pole, obrana + 1, symbol_pocitace)
        if obrana == -1:#nenajde jinou moznost, naprd x_o , o_x, -> vrati nahodnou volnou pozici
            return pozice_pocitace(pole, symbol_pocitace)
