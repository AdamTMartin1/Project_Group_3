# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:57:25 2020

@author: adamt
"""
import math
class CFU():
    def ColonyFormingUnit():
        NumberOfColonies = int(input("NumberOfColonies"))
        AmountOfPlatted = int(input("AmountOfPlatted"))
        DilutionFactor = int(input("DilutionFactor"))
        CFU= NumberOfColonies/ (AmountOfPlatted * DilutionFactor)
        print("CFU", CFU)
