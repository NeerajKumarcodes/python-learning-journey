x = 10
y = 12.4
z = 18j
w = "Hello, World!"

#numbers
#converting numbers
a = float(x)
b = int(y)
c = complex(x) 
#complex numbers cannot be converted.

#random() function generates a random number in a given range.
import random
print(random.randrange(3, 9))  # random.randrange(start, stop, step) start and step are optional, stop is required.

#casting is used for scenarios when we want to specify the type of a variable.
p = float(3.14)
q = str("s1")

#strings
print(w) #prints "Hello, World!"
print(w[1]) #strings are indexed and hence specific elements can be accessed. This will print "e" since indexing is done from 0.
for i in range(w): #strings are basically arrays, so we can loop through them.
    print(i)
print(len(w)) #len() can be used to print length of a string.
print ("Hello" in w) #this can be used to check whether a phrase or character is present in a string or not.
#True or false type result is printed. It can also be used in if-else statements.


