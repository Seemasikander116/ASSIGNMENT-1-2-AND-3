#!/usr/bin/env python
# coding: utf-8

# Seema Sikander
# seemasikander116@gmail.com
# Assignment #1
# PY04134

# In[4]:


##1.	Write python program to print the following string in a specific format. 
a="Twinkle"
b="twinkle"
c="little"
d="star"
e="wonder"
f="diamond"
g="world"
print(a, b,c, d+",")
print("    How I ",e +" What You are!")
print("             Up above the " + g +" so high,")
print("                 Like a diamomd in the sky,")
print(a, b,c, d+",")

print("    How I ",e +" What You are")


# In[5]:


##2.Calculate the circle 
Pi=3.142
r=float(input("Enter radius:"))
area=Pi*r * r
print("Area of Cicle is:")
print(area)


# In[6]:


##3.Sum of two numbers by taking input from user.
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
summ=x+y
print("Sum:")
print(summ)


# In[7]:


##4.Write a program to print current date and time

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[8]:


##5. Write a program take input from user first name and last name and print them in reverse order

firsname = input("Enter First Name : ")
lastname = input("Enter your Last Name : ")
print ( " "+ lastname + " " + firsname)


# In[9]:


##6. Write a python program to get the Python Version you are using.

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[ ]:




