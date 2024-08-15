p = ["I", "am", "Fuad"]
print(p)

p = input("Enter\n~")
p = list(map(str,p.split(",")))
print(p)

# With range

p = range(5)
print(list(p))

p = int(input("Enter\n~ "))
p = range(p)
print(list(p))