# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:57:25 2020

@author: adamt
"""
Choices = int(input("Enter in  a number"))

class CFU():
    def __init__(self, NumberOfColonies, AmountOfPlatted, DilutionFactor):
        self.NOC = NumberOfColonies
        self.AOP = AmountOfPlatted
        self.DF = DilutionFactor
    def ColonyFormingUnit(self):
        CFU= self.NOC/ (self.AOP * self.DF)
        print("CFU", CFU)
        return CFU

if Choices == 1:
    NumberOfColonies = int(input("NumberOfColonies"))
    AmountOfPlatted = int(input("AmountOfPlatted"))
    DilutionFactor = int(input("DilutionFactor"))
    ColonyA = CFU(NumberOfColonies,AmountOfPlatted,DilutionFactor)
    


class Exponetial_Growth():
    def __init__(self, GeometricGrowthRate, Population):
        self.GeometricGrowthRate = GeometricGrowthRate
        self.Population = Population
    def Exponential_Growth(self):
        ExponentialGrowth = self.GeometricGrowthRate*self.Population
        print("Exponential Growth", ExponentialGrowth)
        return ExponentialGrowth
    
if Choices == 2:        
    ExpontialGrowthRate = float(input("GeometricGrowthRate"))
    Population = int(input("Population"))
    ExpontialGrowth = Exponetial_Growth(ExpontialGrowthRate,Population)

class Geometric_Growth_over_time():
    def __init__(self, NetReproductiveRate, StartingPopulation):
        self.NetReproductiveRate = NetReproductiveRate
        self.StartingPopulation = StartingPopulation
    def GeometricGrowthOverTime(self):
        GeometricGrowthOverTime = self.NetReproductiveRate*StartingPopulation
        print("Geometric_Growth_over_time",GeometricGrowthOverTime)
        return GeometricGrowthOverTime
        
if Choices == 3:    
    NetReproductiveRate = float(input("NetReproductiveRate"))
    StartingPopulation = int(input("StartingPopulation"))
    TotalPopulation = Geometric_Growth_over_time(NetReproductiveRate, StartingPopulation)


class Population():
    def __init__(self, PopulationAtTimeZero, Births, Deaths, Immigration, Emigration):
        self.N = PopulationAtTimeZero
        self.B = Births
        self.D = Deaths
        self.I = Immigration
        self.E = Emigration
    def Next_Total_Population(self):
        NextPopulation= self.P  + self.B - self.B + self.I - self.E
        print("NextPopulation", NextPopulation)
        return NextPopulation

if Choices == 4:
    PopulationAtTimeZero = int(input("Population"))
    Births = int(input("Births"))
    Deaths = int(input("Deaths"))
    Immigration = int(input("Immigration"))
    Emigration = int(input("Emigration"))
    NextPopulation = Population(PopulationAtTimeZero,Births,Deaths,Immigration,Emigration)
    
    
    
    
class GenerationTime():
    def __init__(self, Time, NumberOfGenerations):
        self.T = Time
        self.NOG = NumberOfGenerations
    def Generation_Time(self):
        GenerationTime= self.T  / self.NOG
        print("GenerationTime", GenerationTime)
        return GenerationTime

if Choices == 5:
    Time = float(input("Time"))
    NumberOfGenerations = int(input("NumberOfGenerations"))
    TimeOfGeneration = GenerationTime(Time,NumberOfGenerations)
    
    
    

class MarkAndRecapture():
    def __init__(self, NumberOfCapturedFirstTime, NumberOfCapturedSecondTime,NumberOfRecaptured,):
        self.NOCFT = NumberOfCapturedFirstTime
        self.NOCST = NumberOfCapturedSecondTime
        self.NOR = NumberOfRecaptured
    def Mark_And_Recapture(self):
        EstimatedPopulation = (self.NOCFT*self.NOCST) / self.NOR
        print("EstimatedPopulation", EstimatedPopulation)
        return MarkAndRecapture

if Choices == 6:
    NumberOfCapturedFirstTime = int(input("NumberOfCapturedFirstTime"))
    NumberOfCapturedSecondTime = int(input("NumberOfCapturedSecondTime"))
    NumberOfRecaptured = int(input("NumberOfRecaptured"))
    EstimatedPopulation = MarkAndRecapture(NumberOfCapturedFirstTime,NumberOfCapturedSecondTime,NumberOfRecaptured)
    
    
    