x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

"""
All elements of the tuple are fixed. You cannot change any element in the tuple. But if you want to change any element in the tuple, you change the element in the tuple when converting the tuple to a list.

The syntax is list name = list(tuple name)
"""