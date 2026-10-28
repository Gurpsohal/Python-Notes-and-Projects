#https://inventwithpython.com/bigbookpython/project1.html
import random
import random as rd

"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

num_digits = 3
num_guess = 10

def main ():
    print ("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")



def get_secret_number():#number generator and picker
    numbers = [0,1,2,3,4,5,6,7,8,9]
    secret_number =''
    random.shuffle(numbers)
    for i in range(num_digits):
        secret_number += str(numbers[i])
        return secret_number


#def feedback_clues():#Checker
