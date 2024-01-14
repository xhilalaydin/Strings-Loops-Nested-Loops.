# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


: Write a program Lab02_Q2.py to input two integers and print the sequence of integers
between the two input integers, separated by commas and enclosed in square brackets. Display an
increasing sequence if the first argument is smaller than the second; otherwise, display a
decreasing sequence. If the two numbers are the same, that number should be displayed by itself.

Sample Run:
Enter the first integer: 5
Enter the second integer: 12
[5, 6, 7, 8, 9, 10, 11, 12]

Sample Run:
Enter the first integer: 17
Enter the second integer: 10
[17, 16, 15, 14, 13, 12, 11, 10]

Sample Run:
Enter the first integer: 115
Enter the second integer: 115
[115 ]  
    
"""

i = int(input("Enter the first integer: "))
j = int(input("Enter the first integer: "))
print("[" , end= "")

if i < j:
    for k in range(i, j+1):
        print(f"{k}" , end="")
        if k != j:
            print(" ,", end="")
        
elif j < i:
    for k in range (j, i +1):
        print(f"{k}" , end= "")
        if k != i:
            print(" ," , end="")
        
else:
    print(f"{i}" , end= "")
    
print("]")

         
               
               
              