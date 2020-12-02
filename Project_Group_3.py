# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:39:01 2020

@author: adamt
"""
import math
def ColonyFormingUnit():
    NumberOfColonies = int(input("NumberOfColonies"))
    AmountOfPlatted = int(input("AmountOfPlatted"))
    DilutionFactor = int(input("DilutionFactor"))
    CFU= NumberOfColonies/ (AmountOfPlatted * DilutionFactor)
    print("CFU", CFU)

def NextTotalPopulation():
    Population = int(input("Population"))
    Births = int(input("Births"))
    Deaths = int(input("Deaths"))
    Immigration = int(input("Immigration"))
    Emigration = int(input("Emigration"))
    NextTotalPopulation = Population + Births - Deaths + Immigration - Emigration
    print("NextTotalPopulation", NextTotalPopulation)

def GenerationTime():
    Time = int(input("Time"))
    NumberOfGenerations = int(input("NumberOfGenerations"))
    GenerationTime = Time / NumberOfGenerations
    print("GenerationTime",GenerationTime)

def MarkAndRecapture():
    NumberOfCapturedFirstTime = int(input("NumberOfCapturedFirstTime"))
    NumberOfCapturedSecondTime = int(input("NumberOfCapturedSecondTime"))
    NumberOfRecaptured = int(input("NumberOfRecaptured"))
    NextTotalPopulation = (NumberOfCapturedFirstTime*NumberOfCapturedSecondTime) / NumberOfRecaptured
    print("NextTotalPopulation",NextTotalPopulation)
    
def GeometricGrowthOverTime():
    NetReproductiveRate = int(input("NetReproductiveRate"))
    StartingPopulation = int(input("StartingPopulation"))
    TotalPopulation = NetReproductiveRate * StartingPopulation
    print("TotalPopulation",TotalPopulation)
    
def ExponetialGrowthOverTime():
    PopulationAtTimeZero = int(input("PopulationAtTimeZero"))
    PerCapitaFiniteGrowthRate = int(input("PerCapitaFiniteGrowthRate"))
    Time = int(input("Time"))
    ExpontialTotalPopulation = PopulationAtTimeZero * math.exp(PerCapitaFiniteGrowthRate*Time)
    print("ExpontialTotalPopulation",ExpontialTotalPopulation)

def GeometricGrowth():
    GeometricGrowthRate = int(input("GeometricGrowthRate"))
    Population = int(input("Population"))
    GeometricGrowth = GeometricGrowthRate * Population
    print("GeometricGrowth",GeometricGrowth)
    
def ExpontialGrowth():
    ExpontialGrowthRate = int(input("GeometricGrowthRate"))
    Population = int(input("Population"))
    ExpontialGrowth = ExpontialGrowthRate * Population
    print("ExpontialGrowth",ExpontialGrowth)
    
    
    
    
    
def CalculationKa():
    pka = int(input("pka"))
    ka = 10**-pka
    print("ka",ka)  
    
def HydroxialIons