from time import sleep #For waiting a specific number of seconds
from random import randint, uniform, choice #For generateing a random integer
from os import startfile,system #For system control


def getCoordinate(minTime,maxTime): #waits a number of seconds, finds a random coordinate, checks if this coordinate has already been hit, if not it hits it
    time = uniform(minTime,maxTime) #"time" is the amount of time to wait
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
#            system('CLS') #clear screen - equal to matlab cls        
            saveCoordinate,clusterBomb = effectValue()            
            
            if(saveCoordinate):
                used_Coordinates_Numbers.append(coordinate_Numbers) #add to already hit numbers,letters
                used_Coordinates_Letters.append(coordinate_Letters)
                airStrike(coordinate_Letters,coordinate_Numbers)    
                
                
            if(clusterBomb):
                airStrike(coordinate_Letters,coordinate_Numbers)
            #even though the try except block works. It will sometimes give a result due to pythons negative index of lists.
            #To avoid that the index have been set to positive by the two if statements below.
            #This is done since the negative index can at most be -9 so setting this to 0 just shifts the for 
            #loop to the right which is countered by addIndex being one less. i.e.
            #it goes from -9 to +1 to 0 to +2 by the if statements and then addindex makes it 0 to +1 which is desired.
                
                addIndexNumber = 2; #for python negative index 
                addIndexLetter = 2; #for python negative index 
                if(letters.index(coordinate_Letters)-1 < 0): #to remove the negative index in python
                    coordinate_Letters = letters[letters.index(coordinate_Letters)+1];
                    addIndexLetter = 1;
                if(numbers.index(coordinate_Numbers)-1 < 0): #to remove the negative index in python
                    coordinate_Numbers = numbers[numbers.index(coordinate_Numbers)+1];
                    addIndexNumber = 1
                    
                    
                for i in range(letters.index(coordinate_Letters)-1,letters.index(coordinate_Letters)+addIndexLetter):
                    for j in range(numbers.index(coordinate_Numbers)-1,numbers.index(coordinate_Numbers)+addIndexNumber):
                        try: 
                            numbers[j] #does it exist
                            letters[i] #does it exist
                            used_Coordinates_Numbers.append(numbers[j])
                            used_Coordinates_Letters.append(letters[i])
                        except:
                            pass
            break;

def effectValue(): #An effect is chosen
    higher_value=100
    lower_value=1
    final_value = randint(lower_value, higher_value)
    saveCoordinate = False # do not save the coordinate where it hit
    clusterBomb = False;

    if 1 <= final_value <= 5: #5 procent
        print('Cluster Bomb!')
        clusterBomb = True;
        
        
    elif 6 <= final_value <= 35: #30 procent
        print('Airstrike!')
        saveCoordinate = True; # do not save the coordinate     
        
        
    elif 36 <= final_value <= 45: # 10 procent
        print('Heat seeking missile!')
        Player=choice(PlayerPool)
        print(Player + " is awarded a heat seeking missile!")
        
        
    elif 46 <= final_value <= 55: #10 procent
        print('Strongest player drinks 5!') 
        
        
    elif 56 <= final_value <= 70: #15 procent
        print('Fællesskål!')
        
        
    elif 71 <= final_value <= 80: #10 procent
        print('A shot!')
        
        
    else: #ranges from 81 <= final_value <= 100 #20 procent
        print('If water was hit you have to drink 5');
        print("If a ship was hit you have to drink 5");
        print("If a ship was hit, but the ship had already been hit before you can give away 3");
        
        
    return saveCoordinate,clusterBomb

def airStrike(letter,number): #display sounds and message
    print("(" + letter + "," + str(number) + ")") #print coordinate
#    startfile('Airstrike+sound+effect.mp3')# play sound
    
    
PlayerPool = (); #init
numberPlayers = int(input("Enter Number of players! "))

for i in range(numberPlayers): #keep adding players
    x = (input("Enter player name "),);
    PlayerPool +=x;
system('CLS') #clear screen - equal to matlab cls      
letters = ('A','B','C','D','E','F','G','H','I','J'); #possible letters
numbers = (1,2,3,4,5,6,7,8,9,10); #possible numbers
used_Coordinates_Numbers = []; # coordinates which have already been hit
used_Coordinates_Letters = []; 

minMinutes = int(input("Enter minimum minutes to wait ")) #minimum minutes to wait
minSeconds = int(input("Enter minimum seconds to wait ")) #minimum seconds to wait

maxMinutes = int(input("Enter maximum minutes to wait ")) #maximum minutes to wait
maxSeconds = int(input("Enter maximum seconds to wait ")) #maximum seconds to wait

minTime = 60*minMinutes + minSeconds; #min wait time in seconds

maxTime = 60*maxMinutes + maxSeconds; #max wait time in seconds

system('CLS') #clear screen - equal to matlab cls 
while True: #keep running until game is done
    getCoordinate(minTime,maxTime)
