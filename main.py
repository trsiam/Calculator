'''
Simple Calculator:
 Create a basic calculator that can perform addition, subtraction, multiplication, and
 division. Use functions for each operation, and implement basic error handling for invalid inputs.
'''
import sys
from termcolor import colored
temp_Vtwo=0           # Variables assigining once then using them acording to the need of the functions 
temp_Vthree=0


def addition():                      # Addition 
    global temp_Vtwo,temp_Vthree    
    temp_Vtwo=0
    temp_Vthree=0      # Variables assigining once then using them acording to the need of the functions 
    try:
        temp_Vtwo=list(map(int,input("Input Numbers to Perform Addition->").split()))       # Talking input side by side
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))   #Eror if given anything other that int
        addition()
    for i in range(len(temp_Vtwo)):
        temp_Vthree+=temp_Vtwo[i]
    print("Answer->",temp_Vthree)
    print()
    what_to_Do()

    return

def substraction():               # Substraction
    global temp_Vtwo,temp_Vthree
    temp_Vtwo=0
    temp_Vthree=0
    try:
        temp_Vtwo = int(input("Input the first number->")) 
        temp_Vthree=list(map(int,input("Input Numbers to Perform Substraction->").split()))
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))
        substraction()
    for i in range(len(temp_Vthree)):
        temp_Vtwo-=temp_Vthree[i]
    if temp_Vtwo < 0:
        print("0")
    else:
        print("Answer->",temp_Vtwo)
    what_to_Do()
    return

def multiplication():          # Multiplication
    global temp_Vtwo,temp_Vthree
    temp_Vtwo=0
    temp_Vthree=1
    try:
        temp_Vtwo=list(map(int,input("Input Numbers to Perform Multiplication->").split()))
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))
        multiplication()
    for i in range(len(temp_Vtwo)):
        temp_Vthree*=temp_Vtwo[i]
    print("Answer->",temp_Vthree)
    what_to_Do()
    return

def division():             # Division
    global temp_Vtwo,temp_Vthree
    temp_Vtwo=0
    try:
        temp_Vthree=int(input("Input the first number->"))
        temp_Vtwo=list(map(int,input("Input Numbers to Perform Division->").split()))
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))
        division()
    for i in range(len(temp_Vtwo)):
        temp_Vthree/=temp_Vtwo[i]
    print("Answer->",round(temp_Vthree))
    what_to_Do()
    return

def exit():              # Exiting the terminal
    print("Exiting.......")
    sys.exit()

def what_to_Do():                
    c='|'
    d='-'
    width=5
    for i in range(1):                      # Calculator Terminal Image 
        print((d*width*8).center(width))
    for i in range(3):
        print(c.ljust(10) +"CALCULATOR".center(8)+ (c.rjust(20)))
    for i in range(1):
        print((d*width*8).center(width))
    for i in range(2):
        print(c.ljust(4)+"1" +c.center(6) +"2" + c.center(7) +"3" + c.center(7) +"4" + c.center(7) +"5" +  c.center(7) )
    for i in range(1):
        print((d*width*8).center(width))
    for i in range(2):
        print(c.ljust(4)+"8" +c.center(6) +"9" + c.center(7) +"10" + c.center(7) +"C" + c.center(7) +"/" +  c.center(7) )
    for i in range(1):
        print((d*width*8).center(width))
    for i in range(2):
        print(c.ljust(4)+"00" +c.center(6) +"%" + c.center(7) +"!" + c.center(7) +"+" + c.center(7) +"-" +  c.center(7) )
    for i in range(1):
        print((d*width*8).center(width))

    print()
    print("1. Addition")                    # Calculation Options
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()

    try:
        temp_V=int(input("What Calculation you want to Do ->"))  
    except ValueError:
        print(colored("Invalid input: Please enter a number(1 or 2 or 3)","red"))
        what_to_Do()

    if(temp_V==1):
        addition()

    if(temp_V == 2):
        substraction()

    if(temp_V == 3):
        multiplication()

    if(temp_V==4):
        division()

    if(temp_V==5):
        exit()

what_to_Do()           # Recurrsively calling until user exits 


















