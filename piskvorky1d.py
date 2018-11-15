from random import randrange
from ai import tah_pocitace
from ai import strategie_utok
from ai import strategie_obrana
from ai import pozice_pocitace
from util import tah

def vyhodnot(pole):
    #funkce, ktera vyhodnoti zda vyhraji kolecka nebo krizky
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-" #hra neskoncila


def tah_hrace(pole, symbol_hrace):
    #funkce pro vyber pole pro vlozeni symbolu, vrati cislo pole
    while True: #podminka pro zadani cisla v danem rozmezi
        try:
            cislo_pole_hrace = int(input("Zadej cislo pole, kam chces znak obsadit!: ")) -1
        except ValueError:
            print ("Zadavej pouze cisla, ne znaky!")
        else:
            if cislo_pole_hrace + 1 < 0:
                print("Zadane cislo nesmi byt zaporne cislo.")
            elif cislo_pole_hrace + 1 == 0:
                print("Zadane cislo nesmi byt 0.")
            elif cislo_pole_hrace + 1 > len(pole):
                print("Zadane cislo nesmi byt vetsi nez delka hraciho pole.")
            elif pole[cislo_pole_hrace] != "-":
                print("pole je obsazena, zadej volnou pozici: " )
            else:
                return tah(pole,cislo_pole_hrace, symbol_hrace)

def vyber_symbol():
    #funkce pro vyber symbolu hracem
    while True:
        symbol_hrace = input("Zadej kolečko(o) nebo krizek(x) : ").lower()
        if not symbol_hrace in ("x","o"):   #podminka pro zadani x,o
            print("Zadej pouze x nebo o!:")
            continue
        else:
            print("\n")
            print("Hrajes za : ", symbol_hrace)
            return symbol_hrace

def vrat_symbol_pocitace(symbol_hrace):
    #funkce pro vyber symbolu pocitace v zavislosti na vyberu hrace
        if symbol_hrace == "x":
            symbol_pocitace = "o"
            print("Pocitac hraje za: ", symbol_pocitace)
            return symbol_pocitace
        else:
            symbol_pocitace = "x"
            print("Pocitac hraje za: ", symbol_pocitace)
            return symbol_pocitace

def vrat_pole():
    #funkce pro delku pole zadanou uzivatelem
    while True:
        try:
            pole_uzivatel = int(input("Zadej delku herniho pole pro piskvorky: "))
            if pole_uzivatel < 4 or pole_uzivatel > 100:
                print("Minimalni delka pole je 4 a max. 100.")
                continue
        except ValueError:
            print ("Zadavej pouze cisla, ne znaky!")
        else:
            pole = "-" * pole_uzivatel
            return pole

def piskvorky1d():
    print("Vítej ve hře 1-D piškvorky.")
    pole = vrat_pole()#vrati delku hraciho pole zadaneho uzivatelem
    pocet_kol = 0
    strategie = randrange(2)#nahodne vybere ze dvou strategii pocitace, bud obrana nebo utok
    symbol_hrace = vyber_symbol() #hrac si vybere symbol
    symbol_pocitace = vrat_symbol_pocitace(symbol_hrace)#vrati symbol pocitace v zavislosti na vyberu hrace

    print("\n")
    print("Zadavej cisla od 1 do", len(pole))
    print(pole)

    while "-" in pole:

        #tah hrace
        pole = tah_hrace(pole, symbol_hrace)#vlozi symbol na vybranou pozici
        pocet_kol = pocet_kol + 1
        print("Tvuj tah: ")
        print(pocet_kol,".kolo: ",pole)#vypise herni pole s vlozenymi symboly

        vysledek = vyhodnot(pole)#vyhodnoti stav hry
        if vysledek != "-": #pokud se v hernim poli nevyskytuje -, je hra ukoncena
            print(vysledek)
            break

        #tah pocitace
        pole = tah_pocitace(pole, symbol_pocitace, strategie)#vlozi symbol na vybranou pozici
        pocet_kol = pocet_kol + 1
        print("Tah pocitace: ")
        print(pocet_kol,".kolo: ", pole)#vypise herni pole s vylozenymi symboly

        vysledek = vyhodnot(pole)#vyhodnoti stav hry
        if vysledek != "-": #pokud se v hernim poli nevyskytuje -, je hra ukoncena
            print(vysledek)
            break
