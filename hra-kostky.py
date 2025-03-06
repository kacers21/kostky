#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jednoduchá hra kostky
Autor: Šimon Kačer
Licence: MIT
"""

import random
import time


class HraKostky:
    def __init__(self):
        self.skore_hrac = 0
        self.skore_pocitac = 0
        self.kolo = 1
        self.max_kol = 5

    def hod_kostkou(self):
        """Simuluje hod kostkou a vrací náhodné číslo od 1 do 6."""
        print("Kostka se hází...", end="", flush=True)
        time.sleep(0.5)
        print(".", end="", flush=True)
        time.sleep(0.5)
        print(".", end="", flush=True)
        time.sleep(0.5)
        return random.randint(1, 6)

    def zobraz_hod(self, cislo):
        """Zobrazí graficky hod kostkou."""
        print("\n")
        if cislo == 1:
            print("┌───────┐")
            print("│       │")
            print("│   ●   │")
            print("│       │")
            print("└───────┘")
        elif cislo == 2:
            print("┌───────┐")
            print("│ ●     │")
            print("│       │")
            print("│     ● │")
            print("└───────┘")
        elif cislo == 3:
            print("┌───────┐")
            print("│ ●     │")
            print("│   ●   │")
            print("│     ● │")
            print("└───────┘")
        elif cislo == 4:
            print("┌───────┐")
            print("│ ●   ● │")
            print("│       │")
            print("│ ●   ● │")
            print("└───────┘")
        elif cislo == 5:
            print("┌───────┐")
            print("│ ●   ● │")
            print("│   ●   │")
            print("│ ●   ● │")
            print("└───────┘")
        elif cislo == 6:
            print("┌───────┐")
            print("│ ●   ● │")
            print("│ ●   ● │")
            print("│ ●   ● │")
            print("└───────┘")
        print()

    def hraj_kolo(self):
        """Odehraje jedno kolo hry."""
        print(f"\n===== KOLO {self.kolo} =====")
        
        input("Stiskni Enter pro hod kostkou...")
        hod_hrac = self.hod_kostkou()
        self.zobraz_hod(hod_hrac)
        print(f"Tvůj hod: {hod_hrac}")
        
        print("\nTeď hází počítač...")
        time.sleep(1)
        hod_pocitac = self.hod_kostkou()
        self.zobraz_hod(hod_pocitac)
        print(f"Hod počítače: {hod_pocitac}")
        
        if hod_hrac > hod_pocitac:
            print("\n🎉 Vyhráváš toto kolo! 🎉")
            self.skore_hrac += 1
        elif hod_pocitac > hod_hrac:
            print("\n😢 Počítač vyhrává toto kolo.")
            self.skore_pocitac += 1
        else:
            print("\n🤝 Remíza v tomto kole.")
        
        print(f"\nAktuální skóre: Ty {self.skore_hrac} - {self.skore_pocitac} Počítač")
        self.kolo += 1
    
    def spust_hru(self):
        """Spustí celou hru."""
        print("="*50)
        print("VÍTEJ VE HŘE KOSTKY!")
        print("="*50)
        print("Pravidla jsou jednoduchá:")
        print("1. Ty a počítač budete házet kostkou.")
        print("2. Kdo hodí vyšší číslo, vyhrává kolo.")
        print("3. Hrajeme na", self.max_kol, "kol.")
        print("4. Kdo vyhraje více kol, vyhrává celou hru.")
        print("="*50)
        
        while self.kolo <= self.max_kol:
            self.hraj_kolo()
            if self.kolo <= self.max_kol:
                input("\nStiskni Enter pro pokračování...")
        
        print("\n"+"="*30)
        print("HRA SKONČILA!")
        print("="*30)
        print(f"Konečné skóre: Ty {self.skore_hrac} - {self.skore_pocitac} Počítač")
        
        if self.skore_hrac > self.skore_pocitac:
            print("\n🏆 Gratuluji! Vyhrál jsi hru! 🏆")
        elif self.skore_pocitac > self.skore_hrac:
            print("\n😭 Bohužel, počítač vyhrál hru.")
        else:
            print("\n🤝 Hra skončila remízou!")


if __name__ == "__main__":
    hra = HraKostky()
    hra.spust_hru()
    
    # Zeptáme se, zda chce hráč hrát znovu
    while True:
        znovu = input("\nChceš hrát znovu? (ano/ne): ").lower()
        if znovu in ["ano", "a", "yes", "y"]:
            hra = HraKostky()
            hra.spust_hru()
        elif znovu in ["ne", "n", "no"]:
            print("\nDěkuji za hru! Měj se hezky!")
            break
        else:
            print("Nerozumím odpovědi. Zadej 'ano' nebo 'ne'.")
