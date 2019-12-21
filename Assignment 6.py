#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Seema Sikander
seemasikander116@gmail.com
Assignment 6


# In[ ]:


Q 1

Object-oriented programming is one of the most effective approaches to writing software. In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes.

Q 2

It provides a clear modular structure for programs which makes it good for defining abstract datatypes in which implementation details are hidden. Objects can also be reused within an across applications. ... It makes software easier to maintain. ... Reuse also enables faster development

Q 3

function describes the behaviour of the model, they donot have any varable. methods are called by variables

Q 4

class is a function of attribues and functions. object is inheritance of a class attributes are the variables your class have like model name etc behaviour is the way the object can do anything


# In[2]:


class Car():
    def __init__(self, name,colour,year,company,miles):
        self.name = name
        self.colour=colour
        self.year = year
        self.company = company
        self.miles = miles
    def description(self):
        full_name= f"the name of car is {self.company} {self.name} {self.year}"
        return full_name
    def color(self):
        print (f"The colour of the car is {self.colour}")
    def read_odometer(self):
        print (f"the car has run  {self.miles} miles")


# In[3]:


Car = Car('mehran','grey',2012,'suzuki',900)


# In[4]:



Car.description()


# In[5]:


Car.read_odometer()


# In[6]:


Car.color()


# In[ ]:




