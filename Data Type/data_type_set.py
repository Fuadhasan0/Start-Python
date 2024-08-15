p = {"I", "am", "Fuad"}
print(p)

p = input("Enter number and separet with comma(-,-,-,)\n~ ")
p = set(map(str,p.split(",")))
print(p)