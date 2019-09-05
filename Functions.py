#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Functions 
def function1():
    print("Hello, Knowledge Shelf")
    
function1()


# In[3]:


#1. No Arguments No Return Type
def add():
    var1 = int(input("Enter the value of num1 : "))
    var2 = int(input("Enter the value of num2 : "))
    var3 = var1 + var2
    print("Sum = ",var3)
    
add()


# In[4]:


#2. With Arguments and No Retyrn Type
def sub(var1, var2):
    var3 = var1 - var2
    
    print("Sub = ",var3)
    
sub(12,6)


# In[5]:


#3. No Argument and with return type
def multiply():
    var1 = int(input("Enter the value of num1 : "))
    var2 = int(input("Enter the value of num2 : "))
    
    var3 = var1 * var2
    
    return var3

var4 = multiply()
print("Multiply = ",var4)


# In[8]:


#4. With Argument and With Return Type
def div(var1, var2):
    var3 = var1/var2
    return var3
var4 =  div(49,9)
print("Division = %.2f"%var4)

