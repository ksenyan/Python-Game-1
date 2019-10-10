import random
import time

def displayIntro(): 
    print ("You are in a land full of dragons. In front of you, \
you see two caves. In one cave, the dragon is friendly and will \
share his treasure with you. The other dragon is greedy and hungry, \
and will eat you on sight.")
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' :
        print('Which cave will you go into? (1 or 2)')
        cave = input() #Lets user enter data on a new line

    return cave

def checkCave(chosenCave): #This function is the entire game
        print ('You approach the cave...')
        time.sleep(2)
        print ('A large dragon jumps out in front of you! He opens his jaws and...')
        time.sleep(2)

        friendlyCave = random.randint(1,2)
        
        if chosenCave == str(friendlyCave): #First choicem, if random matches chosen
            print ('It gives you the treasure!')
            time.sleep(2)
            treasure = ''
            
            while treasure != 'yes' and treasure != 'no':
                print('Will you keep the treasure? (yes or no) ')
                treasure = input()
                
                if treasure == 'yes' :
                    print ('The dragon looks at you and...')
                    time.sleep(2)
                    chosenCave = '' #This allows code to go to next if statement
                                    #Even if this part has also been excecuted
                    
                else :
                    time.sleep(2)
                    print ('The dragon appreciates your kindness, but insists you keep the treasure.')
                    time.sleep(2)
                                    #After this is over, it jumps to the end.
                    
        if chosenCave != str(friendlyCave): 
            print ('Is ready to fight!')
            time.sleep(2)
            attack = ''
            attacks = ''
            agains = '' #Set all the variables to avoid issues
            
            while attack != 'punch' and attack != 'kick' :
                print('Will you punch or kick? ')
                attack = input()
                winningAttack = random.randint(1,2)
                winningAttacks = random.randint(1,2) 
                if attack == 'punch' :
                    attacks = '1'      #Converts to numbers to then compare to random                         
                if attack == 'kick' :  #Since I can't do randint() with strings
                    attacks = '2'
                    
                if str(winningAttack) != str(attacks) :
                    time.sleep(2)
                    print ('You begin to try and fight... ')
                    time.sleep(2)
                    print ('...but the dragon bites your ear right off. ')
                    
                    if attack == 'punch' : #Depending on choice, the fight is slightly different.
                        print('Would you like to try punching with your other arm or kicking?\
(punch or kick) ')
                        again  = input()
                        
                        if again == 'punch':
                            agains = '1'
                        if again == 'kick' :
                            agains = '2'
                            
                    if attack == 'kick' :
                        print('Would you like to try punching with your \
left or right arm? (left or right) ')
                        again = input()
                        
                        if again == 'left':
                            agains = '1'
                        if again == 'right' :
                            agains = '2'
                    time.sleep(2)
                    
                    if str(winningAttacks) == str(agains) : #Another random ending
                        print('You try your best, but the dragon chomps you up.')
                    else :
                        print('You jump up, and out of nowhere, the dragon surrenders. Congrats!')

                if str(winningAttack) == str(attacks) :
                    time.sleep(2)
                    print ('You jump up, and out of nowhere, the dragon surrenders. Congrats!')
                    time.sleep(2)
                    
                

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' : 
    displayIntro()
    caveNumber = chooseCave() 
    checkCave(caveNumber) #Excecutes the code, then again if the player says yes

    print ('Do you want to play again? (yes or no)')
    playAgain = input()
