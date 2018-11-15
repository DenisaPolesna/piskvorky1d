from ai import tah_pocitace, strategie_utok, strategie_obrana, pozice_pocitace
from piskvorky1d import piskvorky1d, vyhodnot, vrat_symbol_pocitace, vrat_pole
from util import tah
import pytest


#testy na funkci tah
def test_tah_prazdne_pole():
    assert tah("----",1,"x") == "-x--"

def test_tah_vyplnene_pole():
    assert tah("xx-ox", 2, "x") == "xxxox"

def test_kratke_pole():
    assert tah("-", 0, "o") == "o"

def test_tah_dlouhe_pole():
    pole = tah("---------------",13,"o")
    assert pole.index("o") == 13
    assert len(pole)== 15
    assert pole.count("-") == 14

#testy na funkci vyhodnot
def test_vyhodnot_hru_vitez_x():
    assert vyhodnot("xxx-o-o") == "x"

def test_vyhodnot_hru_vitez_o():
    assert vyhodnot("ooo-xx") == "o"

def test_vyhodnot_hru_remiza():
    assert vyhodnot("oxoxoxo") == "!"

def test_vyhodnot_hru_pokracuje():
    assert vyhodnot("oxox-ox") == "-"


#testy na funkci tah_pocitace
def test_tah_pocitace_obrana():
    assert tah_pocitace("x--","o", 1) == "xo-"

def test_tah_pocitace_velke_pole():
    assert tah_pocitace("x-----------------------------", "o",1) == "xo----------------------------"

def test_tah_pocitace_utok():
    assert tah_pocitace("x---","o",0) == "x-o-"


#testy na funkci strategie_utok
def test_strategie_utok_jeden_symbol():
    assert strategie_utok("--x", "x") == "-xx"

def test_strategie_utok_dva_symboly_prazdna_pozice_uprosted():
    assert strategie_utok("x-x", "x") == "xxx"

def test_strategie_utok_tri_prazdne_pozice():
    assert strategie_utok("---", "x") == "-x-"

def test_strategie_utok_dva_symboly_vedle_sebe_zprava():
    assert strategie_utok("-xx","x") == "xxx"

def test_strategie_utok_dva_symboly_vedle_sebe_zleva():
    assert strategie_utok("xx----", "x") == "xxx---"


#testy na funkci strategie_utok
def test_strategie_obrana_hrac_zprava():
    assert strategie_obrana("--x", "o", "x") == "-ox"

def test_strategie_obrana_hrac_zleva():
    assert strategie_obrana("x--", "o", "x") == "xo-"

def test_strategie_obrana_hrac_zleva_zprava():
    assert strategie_obrana("-x-x-","o","x") == "-xox-"

def test_strategie_obrana_hrac_dva_vedle_sebe():
    assert strategie_obrana ("-xx-","o","x") == "-xxo"


#testy na funkci vrat_symbol_pocitace
def test_vrat_symbol_pocitace_hrac_ma_x():
    assert vrat_symbol_pocitace("x") == "o"

def test_vrat_symbol_pocitace_hrac_ma_o():
    assert vrat_symbol_pocitace("o") == "x"
