from time import sleep #For waiting a specific number of seconds
from random import randint, uniform #For generateing a random integer
import os #For system control


def getCoordinate(minTime,maxTime,effects): #waits a number of seconds, finds a random coordinate, checks if this coordinate has already been hit, if not it hits it
    time = uniform(minTime,maxTime) * 60 #60 to get time from seconds to minutes; time is the amount of time to wait
    sleep(time) #waits for "time" seconds
    
    while True: #run until a coordinate which has not been hit before has been hit
        coordinate_Numbers = numbers[randint(0,len(numbers)-1)]; #-1 due to zero index #random coordinate number
        coordinate_Letters = letters[randint(0,len(letters)-1)]; #-1 due to zero index #random coordinate letter
        
        notAlreadyHit = True; #condition to check if a coordinate has already been hit
        
        for i in range(0,len(used_Coordinates_Numbers)): #runs through all coordinates which have already been hit
            if(coordinate_Numbers == used_Coordinates_Numbers[i] and coordinate_Letters == used_Coordinates_Letters[i]): #if a coordinate has already been hit
                notAlreadyHit = False; #Coordinate has already been hit, we need to try another one
                break; #breaks the for loop since the coordinate has already been hit
            
        if(notAlreadyHit): #if the coordinate has not been hit, call airstrike to display what's going to happen and play sound
            airStrike(effects,coordinate_Letters,coordinate_Numbers)
            
            used_Coordinates_Numbers.append(coordinate_Numbers) #add to already hit numbers,letters
            used_Coordinates_Letters.append(coordinate_Letters)
            break;

def airStrike(effects,x,y): #display sounds and message
    os.system('CLS') #clear screen - equal to matlab cls
    print("(" + x + "," + str(y) + ")") #print coordinate
    print(effects[randint(0,len(effects)-1)]) #-1 due to zero index; print message
    os.startfile('Airstrike+sound+effect.mp3')# play sound
    

letters = ('A','B','C','D','E','F','G','H','I','J'); #possible letters
numbers = (1,2,3,4,5,6,7,8,9,10); #possible numbers
used_Coordinates_Numbers = []; # coordinates which have already been hit
used_Coordinates_Letters = []; 

minTime = 0; #min wait time
maxTime = 1; #max wait time

effects = ('a','b','c'); #messages about what's going to happen

while True: #keep running until game is done
    getCoordinate(minTime,maxTime,effects)
