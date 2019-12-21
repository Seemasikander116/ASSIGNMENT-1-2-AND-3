#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Seema Sikander
#Assignment 5
seemasikander116@gmail.com


# In[1]:


#Q1
def isPositiveInteger(number):
    if int(number) > 0 :
        return True
    else:
        return False
def calcFactorial(number):
    factorial = 1
    if isPositiveInteger(number) == True:
        number = int(number)
        for i in range(1, number + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("Invalid input")

factCalc = input("Enter Number to calculate it's factorial: ")
calcFactorial(factCalc)




# In[16]:


#Q2
def CountUpperLower(stns):
    upper=0;
    lower=0;
    for i in stns:
        if i>="A" and i<="Z":
            upper +=1;
        elif i>="a" and i<="z":
            lower +=1;
    print("Upper case",upper);
    print("Lower case", lower);

s = input("Enter String:");
CountUpperLower(s);


# In[17]:


#Q3
List = [];
n = int(input("Enter number of element you want to enter"));
for i in range(0, n):
    num= int(input());
    List.append(num)
#print(List);
def EvenNum(List):
    for num in List:
        if num % 2==0:  
            print(num, end =", ");
EvenNum(List);


# In[18]:


#Q4
num = int(input("Enter num to check it is prime or not: "));
def checkPrime(num):
    if num>1:
        for i in range(2,num//2):
            if(num % i)==0:
                print(num, " is not a prime");
                break;
            else:
                print(num, "is a prime number ");
    else:
        print(num, "is not a prime number");

checkPrime(num);


# In[19]:


#Q5
def checkPaln(string):
    if(string==string[::-1]):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")
string= input("Etner word to check is it Palindrome: ");
checkPaln(string)


# In[ ]:




