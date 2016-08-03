from time import sleep #For waiting a specific number of seconds
from random import randint, uniform, choice #For generateing a random integer
from os import startfile,system #For system control


def getCoordinate(minTime,maxTime): #waits a number of seconds, finds a random coordinate, checks if this coordinate has already been hit, if not it hits it
    time = uniform(minTime,maxTime) * 5 #60 to get time from seconds to minutes; time is the amount of time to wait
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
            airStrike(coordinate_Letters,coordinate_Numbers)
            
            used_Coordinates_Numbers.append(coordinate_Numbers) #add to already hit numbers,letters
            used_Coordinates_Letters.append(coordinate_Letters)
            break;

def effectValue(): #An effect is chosen
    higher_value=99
    lower_value=1
    final_value = randint(lower_value, higher_value)
    #print(final_value)
    if final_value > 0 and final_value <6:
        print('Cluster Bomb!')
        effect='a'
    elif final_value > 5 and final_value < 41:
        print('Airstrike!')
        effect='b'
    elif final_value > 40 and final_value < 51:
        print('Heat seeking missile!')
        effect='c'
    elif final_value > 50 and final_value < 61:
        print('Nothing happens')
        effect='d'
    elif final_value > 60 and final_value < 81:
        print('Fællesskål!')
        effect='e'
    elif final_value > 80 and final_value < 96:
        print('Shots!')
        effect='f'
    else: #ranges from 96 to 99; 96 < final_value < 100
        print('something else!')
        effect='g'
    return effect

def airStrike(letter,number): #display sounds and message
    system('CLS') #clear screen - equal to matlab cls
    print("(" + letter + "," + str(number) + ")") #print coordinate
    
    if effectValue() == 'c':
        Player=choice(PlayerPool)
        print(Player + " is awarded a heat seeking missile!")
    startfile('Airstrike+sound+effect.mp3')# play sound
    
    
PlayerPool = ();
numberPlayers = int(input("Enter Number of players "))
for i in range(numberPlayers):
    x = (input("Enter player name "),);
    PlayerPool +=x;
    
letters = ('A','B','C','D','E','F','G','H','I','J'); #possible letters
numbers = (1,2,3,4,5,6,7,8,9,10); #possible numbers
used_Coordinates_Numbers = []; # coordinates which have already been hit
used_Coordinates_Letters = []; 

minTime = 0; #min wait time
maxTime = 1; #max wait time

while True: #keep running until game is done
    getCoordinate(minTime,maxTime)
