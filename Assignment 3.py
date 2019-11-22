#!/usr/bin/env python
# coding: utf-8

# Seema Sikander
# seemasikander116@gmail.com
# Assignment #3
# PY04134
# question 1: Make calculator with addition , subtraction, multiplication, division and power

# In[1]:


print('***Calculator***')
x=int(input('Enter Number1:')) 
y=int(input('Enter Number2:'))
print('Sum of {} + {} = '.format(x,y))
print(x+y)
print('Subtraction of {} - {} = '.format(x,y))
print(x-y)
print('Multiplication of {} x {} = '.format(x,y))
print(x*y)
print('Division of {} / {} = '.format(x,y))
print(x/y)

print('Power of Number1 {}= '.format(x))
print(x*x)

print('Power of Number2 {}= '.format(y))
print(y*y)


# Question 2:Check if any numeric value present in the list.

# In[2]:


list1 = [1,5,-19,7,89,-99] 
for num in list1: 
       
    if num >= 0: 
       print(num,end=" ")


# Question 3:Add a key to a dictionery

# In[3]:


a = {0:30, 12:10}
print(a)
a.update({9:40})
print(a)


# Question 4:Sum all numeric items in the dictionery 

# In[4]:


d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))


# Question 5:Identify dublicate values.

# In[5]:


my_list = [20,30,50,30,6,50,15,11,20,40,50,15,6,7]
 
my_list.sort()
print(my_list)
 
new_list = sorted(set(my_list))
dup_list =[]
 
 
for i in range(len(new_list)):
        if (my_list.count(new_list[i]) > 1 ):
            dup_list.append(new_list[i])
        
print(dup_list)


# Question 6:Check of given key is already exits in a dictionery.

# In[6]:


def checkKey(dict, key): 
      
    if key in dict: 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  
dict = {'a': 100, 'b':200, 'c':300} 
  
key = 'b'
checkKey(dict, key) 
  
key = 'w'
checkKey(dict, key) 


# In[ ]:




