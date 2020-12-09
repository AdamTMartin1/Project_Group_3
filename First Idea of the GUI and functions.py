# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:04 2020

@author: adamt
"""

# Imports ---------------
from guizero import App, Text, PushButton, TextBox
#from random import choice
# Functions -------------
class CFU():
    def ColonyFormingUnit():
        NumberOfColonies = int(input("NumberOfColonies"))
        AmountOfPlatted = int(input("AmountOfPlatted"))
        DilutionFactor = float(input("DilutionFactor"))
        CFU= NumberOfColonies/ (AmountOfPlatted * DilutionFactor)
        print("CFU", CFU)
        return CFU
    
class ExponetialGrowth():
    def Exponential_Growth():
        ExpontialGrowthRate = float(input("GeometricGrowthRate"))
        Population = int(input("Population"))
        ExponentialGrowth = ExpontialGrowthRate*Population
        print("Exponential Growth", ExponentialGrowth)
        return ExponentialGrowth
    
class GeometricGrowthOverTime():
    def Geometric_Growth_Over_Time():
        NetReproductiveRate = float(input("NetReproductiveRate"))
        StartingPopulation = int(input("StartingPopulation"))
        GeometricGrowthOverTime = NetReproductiveRate*StartingPopulation
        print("Geometric_Growth_over_time",GeometricGrowthOverTime)
        return GeometricGrowthOverTime
        
class Population():
    def Next_Total_Population():
        PopulationAtTimeZero = int(input("Population"))
        Births = int(input("Births"))
        Deaths = int(input("Deaths"))
        Immigration = int(input("Immigration"))
        Emigration = int(input("Emigration"))
        NextPopulation= PopulationAtTimeZero  + Births - Deaths + Immigration - Emigration
        print("NextPopulation", NextPopulation)
        return NextPopulation
    
class GenerationTime():
    def Generation_Time():
        Time = float(input("Time"))
        NumberOfGenerations = int(input("NumberOfGenerations"))
        GenerationTime= Time  / NumberOfGenerations
        print("GenerationTime", GenerationTime)
        return GenerationTime

class MarkAndRecapture():
    def Mark_And_Recapture():
        NumberOfCapturedFirstTime = int(input("NumberOfCapturedFirstTime"))
        NumberOfCapturedSecondTime = int(input("NumberOfCapturedSecondTime"))
        NumberOfRecaptured = int(input("NumberOfRecaptured"))
        EstimatedPopulation = (NumberOfCapturedFirstTime*NumberOfCapturedSecondTime) / NumberOfRecaptured
        print("EstimatedPopulation", EstimatedPopulation)
        return MarkAndRecapture



    

# App -------------------
app = App("Calculator")
# Widgets ---------------
title = Text(app, "Push the red button to find out your spy name")
#top_text = TextBox(app, "top text")

Text = Text(app, "CFU")

CFU_button = PushButton(app, CFU.ColonyFormingUnit, text="Colony Forming Unit")

EG_button = PushButton(app, GeometricGrowthOverTime.Geometric_Growth_Over_Time, text="Geometric Growth Over Time")

GG_button = PushButton(app, ExponetialGrowth.Exponential_Growth, text="Exponetial Growth")

P_button = PushButton(app, Population.Next_Total_Population, text="Next Total Population Growth")

GT_button = PushButton(app, GenerationTime.Generation_Time, text="Generation Time")

MAR_button = PushButton(app, MarkAndRecapture.Mark_And_Recapture, text="Mark And Recapture")


#print(top_text)
# Display ---------------
app.display()


