import os

bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:
    
    tekst_regel = tekst_regel.strip()

    print(tekst_regel)

    tekst_regel = bestand.readline()
    
os.mkdir(tekst_regel)
