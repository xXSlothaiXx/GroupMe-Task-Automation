import random

mylist = ['1', '2', '3', '4', '5']
used = [] 

index = 0

for i in range(len(mylist)):

    selected = mylist[index] 
    print(selected)
    used.append(selected) 
    index = index + 1 

    print(used) 
