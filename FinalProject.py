# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:08:54 2020


"""
""" Module imports"""

from guizero import App, Text, PushButton                                      
    #Takes in the folder guizero, importing in each choicen module from that folder. 
    #Guizero is a module folder that contains the modules required to create a GUI.
import math                                                                    
    #Imports the module math which is used for many calculatios and contains useful things such as logs and Exponetial.

""" Class with all the functions within"""

   
class Calculations():          
    """Creates a class which stores all of the formula from the first semester in Year 1"""     
    def ColonyFormingUnit():                                                   
        """Function that works out the number of colonys in a population of microoganisms, 
            it takes in the dilution factor and number of plated from the user. """
        NumberOfColonies = int(app.question('Number of colonies', 'Please enter as a whole number the number of colonies')) 
        AmountOfPlatted = int(app.question("AmountOfPlatted","AmountOfPlatted"))
        DilutionFactor = float(app.question("DilutionFactor","DilutionFactor"))
        CFU= NumberOfColonies/ (AmountOfPlatted * DilutionFactor)              
            #Number of colony forming units is calculated by taking the number of of clonies and dividing it by the (amount of platted times the dilution actor).
        print("CFU", CFU)
        return CFU       
                                
    def Exponential_Growth():
        """Function that works out the expontial growth in a population, 
            takes in the expontial growth rate and the population from the user."""
        ExpontialGrowthRate = float(app.question("Exponential Growth Rate","Please enter as a number (e.g '1.78') the geometric growth rate"))
        Population = int(app.question('Population',"Please enter as a whole number (e.g '1') the population"))
        ExponentialGrowth = ExpontialGrowthRate*Population
            #Expontial growth is calculated by timesing the eexpontial growth rate by the starting population.
        print("Exponential Growth",ExponentialGrowth)
        return 
    
    def Geometric_Growth_Over_Time():                                          
        """Function that works out the geometirc growth in a population over time, 
        it takes in the net reproductive rate and the starting population from the user. """
        NetReproductiveRate = float(app.question("NetReproductiveRate","NetReproductiveRate"))
        StartingPopulation = int(app.question("StartingPopulation","StartingPopulation"))
        GeometricGrowthOverTime = NetReproductiveRate*StartingPopulation       
            #Geometirc growth over time is calculated by timesing the net reproductive rate and the starting population together.
        print("Geometric_Growth_over_time",GeometricGrowthOverTime)
        return GeometricGrowthOverTime 

                                                   
    def Next_Total_Population():                                               
        """Function that works out the next total population, it takes in the population at time zero, 
            births, deaths, immigration and emmigration from the user."""
        PopulationAtTimeZero = int(app.question('Population at time zero',"Please enter as a whole number (e.g '1') the population at time 0"))
        Births = int(app.question('Births',"Please enter as a whole number (e.g '1') the number of births"))
        Deaths = int(app.question('Deaths',"Please enter as a whole number (e.g '1') the number of deaths"))
        Immigration = int(app.question('Immigration',"Please enter as a whole number (e.g '1') the number of Immigrants"))
        Emigration = int(app.question('Emigration',"Please enter as a whole number (e.g '1') the number of Emigrants"))
        NextPopulation= PopulationAtTimeZero  + Births - Deaths + Immigration - Emigration 
            #Next population is calculated by adding the population at time zero to births and immigration and taking away deaths and emigration
        print("NextPopulation", NextPopulation)
        return NextPopulation

    def Generation_Time():                                                     
        """Function that works out the Generation time, it takes in the time and number of generations from the user."""
        Time = float(app.question('Time',"Please enter as a number (e.g '1.75') the value for time"))
        NumberOfGenerations = int(app.question('Number of generations',"Please enter as a whole number (e.g '2') the number of generations"))
        GenerationTime = Time / NumberOfGenerations
            #Generation time is calculated by dividing the time by the number of generations.   
        print("Generation time",GenerationTime)
        return GenerationTime
   
    def Mark_And_Recapture():
        """Function that works out total population using mark and recapture, number captured first time, 
            the number captured the second time and the number of recaptured from the user. """
        NumberOfCapturedFirstTime = int(app.question('Number Captured First Time',"Please enter as a whole number (e.g '1') the number captured the first time"))
        NumberOfCapturedSecondTime = int(app.question('Number Captured Second Time',"Please enter as a whole number (e.g '1') the number captured the second time"))
        NumberOfRecaptured = int(app.question('Number Recaptured',"Please enter as a whole number (e.g '1') the number recaptured "))
        NextTotalPopulation = (NumberOfCapturedFirstTime*NumberOfCapturedSecondTime) / NumberOfRecaptured
            #Total population is calculated by timesing number captured first time by the number captured in the second time divided by the number of recaptured.
        print("NextTotalPopulation",NextTotalPopulation)
        return NextTotalPopulation
   

                         
    """Chem equations"""


    def Percentage_Yield():
        """Function that works out percentage yeild using actual yield and therotical yeild.  """
        ActualYield = float(app.question('Actual Yield',"Please enter as a number (e.g '1.890') the actual yield"))
        TheoreticalYield = float(app.question('Theoretical Yield',"Please enter as a number (e.g '1.890') the theoretical yield"))
        Perc_Yield = (ActualYield/TheoreticalYield)*100
            #Percentage yeild is calculated by dividing the actual yeild by the theoretical yeild and timesing it by 100
        print("Percentage Yield",Perc_Yield)
        return Perc_Yield



    def pH_H():
        """function that calculates the pH of an equation using Hydrogen ions (H+), it requires a Hydrogen Ion Concentration, 
            which it takes the log of (to the base 10) and multiplies by negative 1, giving pH."""
        Hydrogen_ion_concentration = float(app.question('Hydrogen Ion Concentration',"Please enter as a number (e.g '1.890') the hydrogen ion concentration"))
        pH = -1* (math.log10(Hydrogen_ion_concentration))
        print("pH",pH)
        return pH    


    def pH_OH():
        """function that calculates the pH of an equatin using Hydroxide ions (OH-), 
            it requires the Hydoxide ion Concentration, which it then takes the log of (to the base 10) and multiplies by negative 1, 
            then it adds the answer to 14 to give pOH."""
        Hydroxide_ion_concentration = float(app.question('Hydroxide Ion Concentration',"Please enter as a number (e.g '1.890') the hydroxide ion concentration"))
        pOH = -1* math.log10(Hydroxide_ion_concentration)
        print("pOH",pOH+14)
        return (pOH+14)



   

"""App"""

#the app function was taken from the module guizero which was imported earlier in this code

app = App("Calculator")                                                        
    #Opens the module App, creating a GUI 


title = Text(app, "Push the buttons to complete each calculations")            
    #Displays on the GUI a title with the text  
titlee = Text(app, "it will take you to the console")                          
    #Displays on the GUI a title with the text 


"""Buttons on the GUI """
CFU_button = PushButton(app, Calculations.ColonyFormingUnit, text="Colony Forming Unit")                
    #Buttons text Colony forming units, once the button is pressed it runs the function ColonyFormingUnit from the class calculations
EG_button = PushButton(app, Calculations.Geometric_Growth_Over_Time, text="Geometric Growth Over Time") 
    #Buttons text Geometric growth over time, once the button is pressed it runs the function Geometric_Growth_Over_Time from the class calculations
GG_button = PushButton(app, Calculations.Exponential_Growth, text="Exponetial Growth")                  
    #Buttons text Exponential growth, once the button is pressed it runs the function Exponential_Growth from the class calculations
P_button = PushButton(app, Calculations.Next_Total_Population, text="Next Total Population Growth")     
    #Buttons text Next total population, once the button is pressed it runs the function Next_Total_Population from the class calculations
GT_button = PushButton(app, Calculations.Generation_Time, text="Generation Time")                       
    #Buttons text Generation time, once the button is pressed it runs the function Generation_Time from the class calculations
MAR_button = PushButton(app, Calculations.Mark_And_Recapture, text="Mark And Recapture")                
    #Buttons text Mark and recapture, once the button is pressed it runs the function Mark_And_Recapture from the class calculations
PY_button = PushButton(app, Calculations.Percentage_Yield, text="Percentage Yeild")                     
    #Buttons text Percentage yield, once the button is pressed it runs the function Percentage_Yield from the class calculations
PH_button = PushButton(app, Calculations.pH_H, text="pH")                                               
    #Buttons text pH_H, once the button is pressed it runs the function pH_H from the class calculations
POH_button = PushButton(app, Calculations.pH_OH, text="pOH")                                            
    #Buttons text pH_OH, once the button is pressed it runs the function pH_OH from the class calculations

app.display()       
    #Runs all the app programming created and displays it in R studio as a GUI. It opens the GUI 


