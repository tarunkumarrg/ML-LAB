import numpy as np
import pandas as pd

n=int(input("Enter the number of attributes "))
l=int(input("Enter the number of rows "))

print("Enter the ",n,"ättributes")
attributes=[]
for i in range(1,n+1):
  print("Enter the name of ",i," attribute ")
  name=input()
  
for i in range(1,l+1):
  print("Ënter the values of ",i," row")
  print("Enter the values of attributes")
  res=[]
  for j in range(1,l+1):
    res.append(input())
  attributes.append(res)

print("Enter the target values")
target=[]
for i in range(1,l+1):
  print("Enter the value of ",i," target")
  x=input()
  target.append(x)
  
print("\n The attributes are: ",attributes)
print("\n The target is: ",target)

def findS(c,t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                 
    return specific_hypothesis
  
 print("\n The final hypothesis is:",findS(attributes,target))
