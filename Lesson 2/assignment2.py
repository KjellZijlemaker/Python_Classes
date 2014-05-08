import time
import os

#!usr/bin/env python

# Created by Kjell Zijlemaker #
# Free to use for own purpose #
   
# Main function with cases for executing calculator options
def main():
    choices = ['1', '2', '3', '4', 'q']
    print("What do you want to do?")
    print("1) Add \n2) subtract \n3) multiply \n4) Divide \nq) Quit this program")
    choice = input("Your choice? ")
 
    if choice.lower() or choice.upper() == choices[0]:
        print()
        add()
    elif choice.lower() or choice.upper() == choices[1]:
        print()
        subtract()
    elif choice.lower() or choice.upper() == choices[2]:
        print()
        multiply()
    elif choice.lower() or choice.upper() == choices[3]:
        print()
        divide()
    elif choice.lower() or choice.upper() == choices[4]:
        print()
        
    else:
        print("\nInvalid option selected, try again!")
        time.sleep(2)
        main()
 
#######################################################
# Function for displaying loading bar and counting down

def loadingBar():
    i = 4
    while(i > 0):
        print (i)
        time.sleep(1)
        i -= 1 
    print("Done!")
    
#######################################################
# Function for resetting calculator

def resetCalc():
    print()
    choices = ['y', 'n']
    startOver = input("Would you like to do something else with the calculator? [Y / N]: ")
    print("Please wait, compiling data for shutdown")
    loadingBar();
    if startOver.lower() == choices[0]:
        main()
    else:
        print ("=" *30)
        print("Shutting down fital components..")
        time.sleep(2)
        print("Program ended..")
        os._exit(1)
 
########################################################
# Function for addition with the calculator 
 
def add():
    print("You have chosen addition.")
    time.sleep(0.5)
    howMuch = int(input("How much numbers do you want to add? "))
    print()
    numbers = []
    result = 0
    l = 0

    while l < howMuch:
        numbers.append(l)
        if (numbers[l] == 0):
            numbers[l] = int(input("choose beginning number: "))
            result = numbers[l]
        else:
            numbers[l] = int(input("choose number #" + str(l + 1) + " to sum with: "))
            result += numbers[l]
        l += 1
    print("\ncalculating... Please wait!")
    loadingBar()
    print("Result: %s" % str(result))
    resetCalc()
 
########################################################
# Function for substraction with the calculator
   
def subtract():
    print("You have chosen subtraction.")
    time.sleep(0.5)
    howMuch = int(input("How much numbers do you want to substract with each other? "))
    numbers = []
    result = 0
    l = 0
    while l < howMuch:
        numbers.append(l)
        if (numbers[l] == 0):
            numbers[l] = int(input("choose beginning number: "))
            result = numbers[l]
        else:
            numbers[l] = int(input("choose number #" + str(l + 1) + " to substract with: "))
            result -= numbers[l]
        l += 1
    print("\ncalculating... Please wait!")
    loadingBar()
    print("Result: %s" % str(result))
    resetCalc()
 
########################################################
# Funtion for multiplication with the calculator 

def multiply():
    print("You have chosen multiplication.")
    time.sleep(0.5)
    howMuch = int(input("How much numbers do you want to multiply with each other? "))
    numbers = []
    result = 0
    l = 0
    
    while l < howMuch:
        numbers.append(l)
        if (numbers[l] == 0):
            numbers[l] = int(input("choose beginning number: "))
            result = numbers[l]
        else:
            numbers[l] = int(input("choose number #" + str(l + 1) + " to multiply with: "))
            result *= numbers[l]
        l += 1
    print("\ncalculating... Please wait!")
    loadingBar()
    print("Result: %s" % str(result))
    resetCalc()
 
########################################################
# Function for division with the calculator 
   
def divide():
    print("You have chosen division.")
    time.sleep(0.5)
    howMuch = int(input("How much numbers do you want to divide with each other? "))
    numbers = []
    result = 0
    l = 0
    while l < howMuch:
        numbers.append(l)
        if (numbers[l] == 0):
            numbers[l] = int(input("choose beginning number: "))
            while numbers[0] <= 0:
                print("Can't devide with 0, or less then 0! Try again!")
                numbers[l] = int(input("choose beginning number: "))
            result = numbers[l]
        else:
            numbers[l] = int(input("choose number #" + str(l + 1) + " to devide with: "))
            while numbers[0] <= 0:
                print("Can't devide with 0, or less then 0! Try again!")
                numbers[l] = int(input("choose number #" + str(l + 1) + " to devide with: "))
            result /= numbers[l]
        l += 1
    print("\ncalculating... Please wait!")
    loadingBar()
    print("Result: %s" % str(result))
    resetCalc()
 
######################################################
 
# Starting main application
main()