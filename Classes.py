# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:57:25 2020

@author: adamt
"""

class CFU():
    def __init__(self, NumberOfColonies, AmountOfPlatted, DilutionFactor):
        self.NOC = NumberOfColonies
        self.AOP = AmountOfPlatted
        self.DF = DilutionFactor
    def ColonyFormingUnit(self):
        CFU= self.NOC/ (self.AOP * self.DF)
        print("CFU", CFU)


NumberOfColonies = int(input("NumberOfColonies"))
AmountOfPlatted = int(input("AmountOfPlatted"))
DilutionFactor = int(input("DilutionFactor"))
ColonyA = CFU(NumberOfColonies,AmountOfPlatted,DilutionFactor)
ColonyA.ColonyFormingUnit()