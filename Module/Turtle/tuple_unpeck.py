print("1.\n")
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("2.\n")
fruits = ("apple", "banana", "cherry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print("3.\n")
fruits = ("apple", "banana", "cherry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("$.\n")
fruits = ("apple", "banana", "cherry")

(*green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
