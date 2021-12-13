# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:41:18 2021

@author: end user
"""

import re

string = "two too"
m  = re.findall("t[wo]o", string, re.IGNORECASE) #[wo] find w or o after t and behind o
print(m)

line = "123?45 hello!"
me = re.findall("\d", line, re.I)
print(me)


##TAREA 8
"""
1) Write a regular expression that matches the word Dutch in The Zen of Python.
"""
import re

file  = open("zen_of_python.txt", "r")
text  = file.read()
word = re.findall("Dutch", text, re.IGNORECASE)
print(word)
file.close()

"""
2) Come up with a regular expression that matches all the digits in the string Arizona 479, 501, 870. California 209, 213, 650.

"""
string  = "Arizona 479, 501, 870. California 209, 213, 650."

import re 
digits = re.findall("\d", string, re.IGNORECASE)
print(digits)


"""
In Bash
Write a regular expression that matches the word Dutch in The Zen of Python.

grep Dutch zen.txt

Come up with a regular expression that matches all the digits in the string Arizona 479, 501, 870. California 209, 213, 650.

echo Arizona: 479, 501, 870. California: 209, 213, 650. | grep [[:digit:]]
"""
string = "The ghost that says boo haunts the loo"
exp = re.findall(".oo", string, re.IGNORECASE)
print(exp)