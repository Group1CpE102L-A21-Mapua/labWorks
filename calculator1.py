# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 19:20:09 2018

@author: EJ
"""

counter = 1
summation = 0
numCount = int(input("Number of Values: "))
while counter <= numCount:
    summation += int(input("Enter a Number: "))
    counter += 1
print(summation)