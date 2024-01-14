# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:08:15 2023

@author: hilala-ug
"""

s = str(input("Enter a string (exit to stop): "))
s = s.lower()
outcome = ""

while s != "exit":
    if 1==1:
        for i in range(len(s)):
            word = s[i]
            if i == 0 or word != s[i-1]:
                outcome += word
        
        print("adjacent duplicates removed:", outcome)
        outcome=""
    s = str(input("Enter a string (exit to stop): "))