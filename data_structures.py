# lists
mylist=["pickling","scrubbing","hydration","esterification","hydrolysis","oxidation"]
mylist.append("substitution")
print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print(mylist[5])
mylist[1]="saponification"      # mutable
print(mylist[1], "method is used in manufacturing industries")


thislist = [1, 2, 5, 7, 11]
thislist.insert(2, 3)
print(thislist)

# tuple
print(type(mylist))
# tuple datastructure
mytuple=("watermelon","pomegranate","oranges","plums","grapes")
print(mytuple)

print("I like eating", mytuple[1])

# set datastructure
myset={"CH3OH","C2H5OH","C3H7OH","C4H9OH","C5H11OH"}
print(myset)