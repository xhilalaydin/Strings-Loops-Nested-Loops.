# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:54:31 2023

@author: hilala-ug
"""

"""
: Write a program Lab02_Q1.py to input a positive integer n and displays the sum of the
first n terms of the sequence: In other words, the program should generate the following
sequence: 1 + (1/2) + (1/3) + (1/4) + (1/5) + ... + (1/n)
Assume that the input n is positive. The sum of the fractions should be displayed in 3 digits
after the decimal point.

Sample Run:
Enter an integer (-1 to stop): 1
the sum of 1 is 1.000

Sample Run:
Enter an integer (-1 to stop): 2
the sum of 1 + 1/2 is 1.500

Sample Run:
Enter an integer (-1 to stop): 6
the sum of 1 + 1/2 + 1/3 + 1/4 +
1/5 + 1/6 is 2.450

Sample Run:
Enter an integer (-1 to stop): 10
the sum of 1 + 1/2 + 1/3 + 1/4 +
1/5 + 1/6 + 1/7 + 1/8 + 1/9 +
1/10 is 2.929

"""
sum = 0
n = int(input("Enter an integer (-1 to stop): "))

if n != -1:
    print ("the sum of " , end ="")    
    for i in range(1, n+1):
       sum +=  1 / i
       if i == 1:
           print("1 ", end="")
       else:
           print (f" + 1/{i}" , end="" )
           
    print(f" is {sum:.3f}") 






"""          
       elif i != n:
           print (f" + 1/{i}" , end="" )
       elif i == n:
           print( f" + 1/{i}" , end="")
           
print(f" is {sum:.3f}")
else: 
    print("bye")       
           

"""
           
         
               
          
       
    
    