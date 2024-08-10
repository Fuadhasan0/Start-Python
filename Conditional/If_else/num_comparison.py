num1 = input("Enter first number\n~ ")
num2 = input("Enter second number\n~ ")
num3 = input("Enter third number\n~ ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num3:
       max_num = num1
elif num2 > num3:
       max_num = num2
else:
       max_num = num3       
       
print("Maximum:",max_num)