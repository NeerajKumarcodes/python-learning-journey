#Dictionaries
d = {
  "Name": "Neeraj",
  "Age": 23,
  "Address": "abc"
}

print(d)

#Dictionaries are ordered, changeable and do not allow duplicates.
#Items are present in key:value pairs.

print(d["Name"])

#get() can also be used to get the value associated with the provided key.
print(d.get("Name"))

#keys() will give a list of all the keys.
print(d.key())

#Changes can be made by assigning a new value to the key. update() method can also be used for this.
d["Address"] = "def"
print(d["Address"])

#values() will give a list of all the values.
print(d.values())

#New items can be added by simply providing a new key with a value assignment. update() method can also be used for this.
d["Profile"] = "Developer"
print(d)

#pop() method can be used to remove a specified key value pair. del keyword can also be used for this.
d.pop("profile")
#popitem() method will remove the last item.
#clear() method empties the whole dictionary.

#copy() method can be used to copy an entire dictionary.
d1 = d.copy()

#dict() function can also be used to copy a dictionary.
d2 = dict(d)





