# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:31:42 2021

@author: end user
"""
#MORE OOP EXERCISES THE SELF TAUGHT PROGRAMER


class Square():
    
    square_list = []
    
    def __init__(self,s1):
        self.s1 = s1
        self.square_list.append(self.s1)
    
    
    def change_size(self, number):
        self.s1 = (self.s1) + number
        return self.s1
        
    
    def calculate_perimeter(self):
        return (self.s1)*4
    
    def print_perimeter(self):
        return("""{} by {} by {} by {}""".format(self.s1, self.s1, self.s1, self.s1))
    
    
    
square_1 = Square(2)
square_12 = square_1
square_2 = Square(4)
square_3 = Square(5)
print(square_3.square_list)
print(square_3.print_perimeter())


def same (ob1, ob2):
    return ob1 is ob2

print(same(square_1, square_2))
print(same(square_1, square_12))
