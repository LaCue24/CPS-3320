# Gift-assigner program

import random

numPeople = int(input("How many people are playing? "))

givers = []

recivers = list(range(numPeople))

print("Please enter their names: ")

# Get all of the players' names and add them to the list

for i in range(numPeople):
    givers.append(input(""))

# Randomly assign gift givers to gift receivers. Check to make sure that nobody is assigned themselves (which is no fun!), and that each person can only give one gift and can only receive one gift (no repeats). Keep trying (looping) until everyone is giving a gift to someone else.
g=[]
for i in range(numPeople):
    g.append(givers[i])
k=numPeople
j=0
while j < numPeople:
    recivers[j] = g[random.randint(0,k-1)]
    if recivers[j]!=givers[j]:
        g.remove(recivers[j])
        k=k-1
        j=j+1
# Print results

print()

print("Gift Assignments...")

for k in range (numPeople):
    print(givers[k], "will buy a gift for,",recivers[k])

print()

