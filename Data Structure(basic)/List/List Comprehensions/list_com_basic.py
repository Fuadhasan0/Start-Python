# string sift-1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
       newlist.append(x)
       
print("1.\t", newlist)       

# short way-1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]

print("Short 1.\t",newlist)


# string sift with condition-2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
       if "a" in x:
              newlist.append(x)
       
print("2.\t",newlist) 

# short way-2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print("Short 2.\t", newlist)

# remove element in string-3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

print("3.\t", newlist)

# number element in string-4
mylist = [213, 3 , 45, 40, 67, 88, 24, 435, 87, 54]
newlist = [x for x in mylist if x <100]

print("4.\t", newlist)

# .upper all element in newlist-5
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print("5.\t", newlist)

# assign all element of "Hello" in string-6
newlist = ["Hello" for x in range(10)]

print("6.\t", newlist)

# repleace element in string-7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

print("7.\t", newlist)