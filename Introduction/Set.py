#Sets
s = {"a", "b", "c", "d"}

#print the set
print(s)

#Sets are unordered, unchangeable and do not allow duplicates
s1 = {1, 2, 2, 3}
print(s1) #prints {1, 2, 3} no duplicates

#len() method can be used to get length of a set.
print(len(s))

#we can loop through set.
for x in s:
  print(x)

#we can check whether something is present in a set or not using in keyword.
print("b" in s)

#although items cannot be changed, but new items can be added using add() method.
s.add("e")
print(s)

#update() can be used to add items from another set to our set.

#remove() removes the provided element from the set.
s.remove("e") #discard() can also be used for removing an element

#pop() can also be used to remove elements. Since sets are unordered we cannot predict which item will be removed.
s.pop()

#clear() empties the entire set.
#del keyword will delete the entire set.
del s1
