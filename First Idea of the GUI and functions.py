# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:04 2020

@author: adamt
"""

# Imports ---------------
from guizero import App, Text, PushButton
import math
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



#Chem equations for the Project 

# % yeild = (mass of desired products/total mass of reactants)x100

class Perc_Yield():
    def Percentage_Yield():
        ActualYield = float(input("ActualYield"))
        TheoreticalYield = float(input("TheoreticalYield"))
        Perc_Yield = (ActualYield/TheoreticalYield)*100
        print("Percentage Yield",Perc_Yield)
        return Perc_Yield

# pH =-log10[H+]

class pH():
    def pH_H():
        Hydrogen_ion_concentration = float(input("Hydrogen_ion_concentration"))
        pH = -1* (math.log10(Hydrogen_ion_concentration))
        print("pH",pH)
        return pH
    

class pOH():
    def pH_OH():
        Hydroxide_ion_concentration = float(input("Hydroxide_ion_concentration"))
        pOH = -1* math.log10(Hydroxide_ion_concentration)
        print("pOH",pOH)
        return (pOH+14)



    

# App -------------------

#the app function was taken from the module guizero which was imported earlier in this code

app = App("Calculator")
# Widgets ---------------
title = Text(app, "Push the buttons to complete each calculations")
titlee = Text(app, "it will take you to the console")
#top_text = TextBox(app, "top text")


CFU_button = PushButton(app, CFU.ColonyFormingUnit, text="Colony Forming Unit")

EG_button = PushButton(app, GeometricGrowthOverTime.Geometric_Growth_Over_Time, text="Geometric Growth Over Time")

GG_button = PushButton(app, ExponetialGrowth.Exponential_Growth, text="Exponetial Growth")

P_button = PushButton(app, Population.Next_Total_Population, text="Next Total Population Growth")

GT_button = PushButton(app, GenerationTime.Generation_Time, text="Generation Time")

MAR_button = PushButton(app, MarkAndRecapture.Mark_And_Recapture, text="Mark And Recapture")

PY_button = PushButton(app, Perc_Yield.Percentage_Yield, text="Percentage Yeild")

PY_button = PushButton(app, pH.pH_H, text="pH")

PY_button = PushButton(app, pOH.pH_OH, text="pOH")

#print(top_text)
# Display ---------------
app.display()


