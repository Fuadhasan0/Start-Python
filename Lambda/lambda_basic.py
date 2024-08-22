# lambda with one value
X = lambda A: A + 1
print(X(4))

# lambda with two value
Y = lambda n, m: n * m
print(Y(2, 3))

# lambda with tree value
Z = lambda a, b, c: (a*b) - c
print(Z(10, 3, 20))

# lambda with a function
def lambda_1(n):
       x = lambda a : a + 1
       result = x(n)
       print(result)
       
lambda_1(4)

# lambda with a functiion and input type
def lambda_fun(num1, num2):
       X = lambda x, y: (x+y) / 2
       result = X(num1, num2)
       return result

number_1 = int(input("Enter value of X \n~ "))
number_2 = int(input("Enter a value of Y\n~ "))
avg = lambda_fun(number_1, number_2)

print(f"The average is {avg}.")