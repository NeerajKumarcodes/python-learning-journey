#Lists

#These are used to store multiple items in same variable
_list = ["Mercury", "Venus", "Earth", "Mars"]

print(_list) #Prints the whole list

#Lists are ordered, changeable and allows duplicates. It is indexed from [0] to [length - 1].

#len() can be used to return the length of the list.
print(len(_list))

#List can contain multiple data types within itself.
_list1 = [1, "qwerty", True, 2]

#We can check the presence of items in the list.
print("Earth" in _list)

#We can change items in a list since it is changeable.
_list[2] = "Home" #List becomes ["Mercury", "Venus", "Home", "Mars"]

#We can insert new items in the list at a desired index using insert() method.
_list.insert(0, "Sun") #insert(index, item)

#Intems can be added at the end of the list using append() method.
_list.append("Asteroid Belt")

#To append items from another list extend() method is used.
_extendedList = ["Jupiter", "Saturn", "Uranus", "Neptune"]
_list.extend(_extendedList) #Any iterable object such tuples, sets, dictionaries can be appended.



