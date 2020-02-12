#importing random package
import random

#list of answers
listAnswer = ['hangman','apples','banana','orange']

#selecting a random answer
answer = listAnswer[random.randint(0,4)]
#creating a list of characters of the answer
A = list(answer)
#creating a list of '-' of same length as A
L = ['_']*len(answer)
play = True
chance = 0

#infinte while loop
while play == True:
    #asking the user to guess the letter
    print('Guess a letter in the word: ')
    guess = str(input())
    #if the guessed letter is present in the list A
    if guess in A:
        a = 0
        print('GOOD GUESS!')
        #replacing the places in the list L where the guessed letter in the list A is present
        for i in answer:
            if i == guess:
                L[a] = i
        a += 1
        #printing the list L
        for i in L:
           print(i,end = '')
           print('\n')
         #if the guessed letter was wrong
        else:
           print('BAD GUESS!')
           #chance increases by 1
           chance += 1
         #if chance becomes equal to six 
        if chance == 6:
             #Game over
            print('You have run out of chances. YOU LOSE!')
            break;
         #if you have guessed all correct answers
        if A == L:
             #loop terminates
             play = False
             print('GREAT JOB. YOU WIN!')