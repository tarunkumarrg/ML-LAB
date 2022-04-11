import numpy as np
import pandas as pd
data=pd.read_csv("data.csv")
print(data,"\n")
d=np.array(data)[:,:-1]
print("\nThe attributs are : ",d)
target=np.array(data)[:,-1]
print("\nTarget is : ",target)
def find(c,t):
    for i,val in enumerate(t):
        if val=="Yes":
            s=c[i].copy()
            break
            
    for i,val in enumerate(c):
            if t[i]=="Yes":
                for x in range(len(s)):
                    if val[x] != s[x]:
                          s[x]='?'
                    else:
                        pass
    return s

print("final hythosis is:",find(d,target))
