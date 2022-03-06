#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to print "Hello Python"?

# In[1]:


print("hello python")


# 2.	Write a Python program to do arithmetical operations addition and division.?

# In[2]:


# Input numbers:  
num1 = 20
num2 = 5 
  
# Add two numbers  
sum = float(num1) + float(num2)  
#Divide two numbers  
div = float(num1) / float(num2)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum)) 
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  


# 3.	Write a Python program to find the area of a triangle?

# In[4]:


# Three sides of the triangle is a, b and c:  
a = float(input("Enter first side: "))  
b = float(input("Enter second side: "))  
c = float(input("Enter third side: "))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print("The area of the triangle is %0.2f" %area)   


# 4.	Write a Python program to swap two variables?

# In[5]:


# Python swap program   
x = input('Enter value of x: ')  
y = input('Enter value of y: ')  
  
# create a temporary variable and swap the values  
temp = x  
x = y  
y = temp  
  
print('The value of x after swapping: {}'.format(x))  
print('The value of y after swapping: {}'.format(y))  


# 5.	Write a Python program to generate a random number?

# In[7]:


import random
print(random.random())


# In[ ]:




