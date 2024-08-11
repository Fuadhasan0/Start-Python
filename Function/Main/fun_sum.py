def add(n1, n2):
       return n1 + n2

num1 = input("Enter number-1\n~ ")
num2 = input("Enter number-2\n~ ")
num1 = int(num1)
num2 = int(num2)

result = add(num1, num2)
print("Summetion\n~",result)

print("Summetion\n~",add(num1, num2))

print("No input\n~",add(10, 20))

