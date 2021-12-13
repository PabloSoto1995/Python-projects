# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:22:41 2021

@author: end user
"""

"""
Write a program with an infinite loop and a list of numbers.

Each time through the loop the program should ask the user to guess a number

(or type q to quit). If they type q, the program should end.

Otherwise, it should tell them whether or not they successfully guessed a number

in the list or not.
"""
lista = [1,2,3,4,5]
while True:
    character = input("enter a number: ")
    if character == "q":
        break
    elif int(character) in lista:
        print("Great guess")
    else:
        print("wrong guess")