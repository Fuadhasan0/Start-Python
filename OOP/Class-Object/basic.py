class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    def print_name(selt):
           print( "Name: " + selt.name + ", Age: " + selt.age)
 

# Taking input from the user
input_name = input("Enter your name\n~ ")
input_age = input("Enter your age\n~ ")

# Creating an instance of the class
output = Person(input_name, input_age)

# Printing the attributes
print(output.name)
print(output.age)

# Printing the string representation of the object
print(output)

output.print_name()
