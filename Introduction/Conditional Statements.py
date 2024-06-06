# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 10
b = 7

#if statement can be written by useing if keyword.
if a > b:
  print("a is greater than b")

b = 10
#elif (else if) as the name implies if the prior conditions were not true, try this condition.
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")

b = 20
#else statement catches anything that was not caught by preceding conditions.
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")
else:
  print("a is less than b")

#Multiple conditional statements can be combined together using logical operators such as "and", "or" or "not".
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#if statements cannot be left empty. If our if statement is without content, we can type in pass statement to avoid error.
a = 33
b = 200

if b > a:
  pass
