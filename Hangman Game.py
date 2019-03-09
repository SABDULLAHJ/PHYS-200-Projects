#!/usr/bin/python
# Date : 31/12/2018
# Author : Syed Abdullah Jelani
# Version : v.1
# Description :Hangman word game.

import random
import os
import sys

os.chdir("C:\\Users\\Syed Abdullah Jelani\\Desktop\\RGB to grayscale converter pics\\hangman")
word_file = open("words.txt", "r")



def parser(word_file):
    word_list = list(word_file)
    word_list =[s.replace('\n', '') for s in word_list]
    word_list= [ x for x in word_list if len(x)>4 ]
        
    return word_list


def hangman(word_file):
    word_list = parser(word_file)
    yo = input("Would you like to play Hangman? Y/N")
    while yo != "Y" or "N":
        if yo == "N":
            return("Have a good day")
            break
           
        elif yo != "Y" and yo !="N" :
            print("Type either Y/N my guy" )
            yo = input("Would you like to play Hangman? Y/N")
        
   
        else:
            word = random.choice(word_list)
            tape = list("_" * len(word))
            tape[0] = word[0]
            lives = 4
            i=0
            while lives!=0:
                guess = input("Guess a lowercase letter!!! " + "\n" + str(tape));
                                
                
                
                if str(guess) in word:
                    indices = [a for a, x in enumerate(word) if x == guess]
                    for a in indices:
                        tape[a] = guess
                        word2 = "".join(tape)
                        if word2 == word:
                            return(word2 + " Congrats You won!!")
                
                elif str(guess)== "EXIT":
                    sys.exit()
                
                elif str(guess) == "NEW WORD":
                    i=0
                    break
                
                elif str(guess) == "HINT" :
                    if i == 0:
                        tape[tape.index("_")] = word[tape.index("_")]
                        i+=1
                    else:
                        print("YOU ONLY GET ONE HINT!!!!")
                    
                
                else:
                    lives = lives - 1
                    print("Try Again! Lives left:", lives)
                    if lives ==0:
                        return("The correct word was : " + str(word))


print(hangman(word_file))

###DONE###