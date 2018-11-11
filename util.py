
def tah(pole, cislo_pole, symbol):
    #funkce pro ulozeni pole na herni pole pro jednotlive tahy hracu
    return pole[:cislo_pole] + symbol + pole[cislo_pole + 1:]
