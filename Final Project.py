# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:00:04 2020
"""

# Import modules ---------------
from guizero import App, Text, PushButton                                      #Takes in the folder guizero, importing in each choicen module from that folder. Guizero is a module folder that contains the modules required to create a GUI.
import math                                                                    #Imports the module math which is used for many calculatios and contains useful things such as logs and Exponetial.
app = App("Calculator")
# Functions -------------
class Calculations():                                                          #Creates a class which stores all of the formula from the first semester in Year 1
    def ColonyFormingUnit():                                                   #Function that works out the number of colonys in a population of microoganisms, it takes in the dilution factor and number of plated from the user. 
        NumberOfColonies = int(app.question('Number of colonies', 'Please enter as a whole number the number of colonies')) 
        AmountOfPlatted = int(app.question("AmountOfPlatted"))
        DilutionFactor = float(app.question("DilutionFactor"))
        CFU= NumberOfColonies/ (AmountOfPlatted * DilutionFactor)              #Number of colony forming units is calculated by taking the number of of clonies and dividing it by the (amount of platted times the dilution actor).
        print("CFU", CFU)
        return CFU
    
    def Exponential_Growth():                                                  #Function that works out the expontial growth in a population, it takes in the expontial growth rate and the population from the user. 
        ExpontialGrowthRate = float(app.question("GeometricGrowthRate"))
        Population = int(app.question("Population"))
        ExponentialGrowth = ExpontialGrowthRate*Population                     #Expontial growth is calculated by timesing the eexpontial growth rate by the starting population.
        print("Exponential Growth", ExponentialGrowth)
        return ExponentialGrowth

    def Geometric_Growth_Over_Time():                                          #Function that works out the geometirc growth in a population over time, it takes in the net reproductive rate and the starting population from the user. 
        NetReproductiveRate = float(app.question("NetReproductiveRate"))
        StartingPopulation = int(app.question("StartingPopulation"))
        GeometricGrowthOverTime = NetReproductiveRate*StartingPopulation       #Geometirc growth over time is calculated by timesing the net reproductive rate and the starting population together.
        print("Geometric_Growth_over_time",GeometricGrowthOverTime)
        return GeometricGrowthOverTime 

    def Next_Total_Population():                                               #Function that works out the next total population, it takes in the population at time zero, births, deaths, immigration and emmigration from the user. 
        PopulationAtTimeZero = int(app.question("Population"))
        Births = int(app.question("Births"))
        Deaths = int(app.question("Deaths"))
        Immigration = int(app.question("Immigration"))
        Emigration = int(app.question("Emigration"))
        NextPopulation= PopulationAtTimeZero  + Births - Deaths + Immigration - Emigration #Next population is calculated by adding the population at time zero to births and immigration and taking away deaths and emigration
        print("NextPopulation", NextPopulation)
        return NextPopulation

    def Generation_Time():                                                     #Function that works out the next total population, it takes in the population at time zero, births, deaths, immigration and emmigration from the user. 
        Time = float(app.question("Time"))
        NumberOfGenerations = int(app.question("NumberOfGenerations"))
        GenerationTime= Time  / NumberOfGenerations
        print("GenerationTime", GenerationTime)
        return GenerationTime

    def Mark_And_Recapture():
        NumberOfCapturedFirstTime = int(app.question("NumberOfCapturedFirstTime"))
        NumberOfCapturedSecondTime = int(app.question("NumberOfCapturedSecondTime"))
        NumberOfRecaptured = int(app.question("NumberOfRecaptured"))
        EstimatedPopulation = (NumberOfCapturedFirstTime*NumberOfCapturedSecondTime) / NumberOfRecaptured
        print("EstimatedPopulation", EstimatedPopulation)
        return EstimatedPopulation


#Chem equations for the Project 

# % yeild = (mass of desired products/total mass of reactants)x100

    def Percentage_Yield():
        ActualYield = float(app.question("ActualYield"))
        TheoreticalYield = float(app.question("TheoreticalYield"))
        Perc_Yield = (ActualYield/TheoreticalYield)*100
        print("Percentage Yield",Perc_Yield)
        return Perc_Yield

# pH =-log10[H+]

    def pH_H():
        Hydrogen_ion_concentration = float(app.question("Hydrogen_ion_concentration"))
        pH = -1* (math.log10(Hydrogen_ion_concentration))
        print("pH",pH)
        return pH    


    def pH_OH():
        Hydroxide_ion_concentration = float(app.question("Hydroxide_ion_concentration"))
        pOH = -1* math.log10(Hydroxide_ion_concentration)
        print("pOH",pOH)
        return (pOH+14)



    

# App -------------------

#the app function was taken from the module guizero which was imported earlier in this code

app = App("Calculator")
# Widgets ---------------

#both widgets

title = Text(app, "Push the buttons to complete each calculations")

titlee = Text(app, "it will take you to the console")



CFU_button = PushButton(app, Calculations.ColonyFormingUnit, text="Colony Forming Unit")

EG_button = PushButton(app, Calculations.Geometric_Growth_Over_Time, text="Geometric Growth Over Time")

GG_button = PushButton(app, Calculations.Exponential_Growth, text="Exponetial Growth")

P_button = PushButton(app, Calculations.Next_Total_Population, text="Next Total Population Growth")

GT_button = PushButton(app, Calculations.Generation_Time, text="Generation Time")

MAR_button = PushButton(app, Calculations.Mark_And_Recapture, text="Mark And Recapture")

PY_button = PushButton(app, Calculations.Percentage_Yield, text="Percentage Yeild")

PY_button = PushButton(app, Calculations.pH_H, text="pH")

PY_button = PushButton(app, Calculations.pH_OH, text="pOH")

#print(top_text)
# Display ---------------
app.display()


