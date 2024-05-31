#strings
w = "Hello, World!"

print(w) #prints "Hello, World!"

print(w[1]) #strings are indexed and hence specific elements can be accessed. This will print "e" since indexing is done from 0.

for i in range(w): #strings are basically arrays, so we can loop through them.
    print(i)
  
print(len(w)) #len() can be used to print length of a string.

print ("Hello" in w) #this can be used to check whether a phrase or character is present in a string or not.
#True or false type result is printed. It can also be used in if-else statements.

print(w[2:5]) #prints characters from index 2 to 5(not including 5)
print(w[:5]) #print from start
print(w[2:]) #print to end

print(w.upper()) #prints the string in uppercase.
print(w.lower()) #prints the string in lowercase.

print(w.replace("o", "u")) #characters or phrases can be replaced using replace()

print(w.split(",")) #splits the string into substrings upon encountring the provided separation instance.

s = "This is Neeraj"

print(w + s) #concatenate two different strings(without space). To add space, add + " " + between the strings

#F-string used to format strings. Directly combine integers to the strings
p = 1
q = f"This is number one - {p}" #A f string is identified by f infront of string literal. 
#The placeholder can contain variables, operations, functions etc.
print(q)

#\" Double Quotes \'	Single Quote	\\	Backslash	\n	New Line	\r	Carriage Return	\t	Tab	\b	Backspace	\f	Form Feed	\ooo	Octal value	
#\xhh	Hex value are few escape characters that can help in insert characters that might generate error otherwise.

