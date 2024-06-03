#Tuple
t = ("rock", "and", "roll")

#Tuples are ordered, immutable, and allows duplicates

print(len(t)) #tuple length

#tuples are indexed
print(t[1])

#to make changes into tuple, we can convert them into list.
t1 = list(t)
#we can make changes to t1 such as append, remove, concatenate and then store this t1 back in t as tuple to update the tuple.

#tuples have a few methods to help us through tasks
#count() method will give a count of a number of times a specified value occurs in the tuple.
t2 = (1, 2, 3, 2, 4, 4, 5, 1, 1)
print(t2.count(1))

#index() method finds and returns the index of a specified value.
print(t2.index(3))
