#Objective: Revise how to add and remove an item from a list in Python
ninjabelts = ['white', 'yellow', 'orange', 'green', 'blue', 'brown', 'black']

# Add 'bronze' and remove 'blue' from the ninjabelts list.
ninjabelts.append("bronze")
ninjabelts.remove("blue")

#Expected Outcome: Bronze
print(ninjabelts[-1])
#Expected Outcome: Brown
print(ninjabelts[4])
