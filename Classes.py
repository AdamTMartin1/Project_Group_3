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


class Exponetial_Growth():
    def __init__(self, GeometricGrowthRate, Population):
        self.GeometricGrowthRate = GeometricGrowthRate
        self.Population = Population
    def Exponential_Growth(self):
        ExponentialGrowth = self.GeometricGrowthRate*self.Population
        print("Exponential Growth", ExponentialGrowth)
    
    
        
ExpontialGrowthRate = float(input("GeometricGrowthRate"))
Population = int(input("Population"))
ExpontialGrowth = ExpontialGrowthRate * Population

class Geometric_Growth_over_time():
    def __init__(self, NetReproductiveRate, StartingPopulation):
        self.NetReproductiveRate = NetReproductiveRate
        self.StartingPopulation = StartingPopulation
    def GeometricGrowthOverTime(self):
        Geometric_Growth_over_time = self.NetReproductiveRate*StartingPopulation
        print("TotalPopulation",TotalPopulation)
    
NetReproductiveRate = float(input("NetReproductiveRate"))
StartingPopulation = int(input("StartingPopulation"))
TotalPopulation = NetReproductiveRate * StartingPopulation
    