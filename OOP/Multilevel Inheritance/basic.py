class Main:
    def __init__(self, fname, lname, year, department, university):
        self.fname = fname
        self.lname = lname
        self.year = year
        self.department = department
        self.university = university
        
    def __str__(self):
        return f"Name: {self.fname} {self.lname}\tYear: {self.year}\tDepartment: {self.department}\tUniversity: {self.university}" 

class Sub1(Main):
    def __init__(self, fname, lname, year, department, university):
        super().__init__(fname, lname, year, department, university)

class Sub2(Sub1):
    def __init__(self, fname, lname, year, department, university):
        super().__init__(fname, lname, year, department, university)

# Main class
print("Main class:\n")              
fname_1 = input("Enter first name\n~ ")
lname_1 = input("Enter last name\n~ ")
year_1 = input("Enter year\n~ ")
department_1 = input("Enter department\n~ ")
university_1 = input("Enter university\n~ ")

class_of_main = Main(fname_1, lname_1, year_1, department_1, university_1)

# Sub_1 class
print("Sub_1 class:\n")
fname_2 = input("Enter first name\n~ ")
lname_2 = input("Enter last name\n~ ")
year_2 = input("Enter year\n~ ")

class_of_sub_1 = Sub1(fname_2, lname_2, year_2, department_1, university_1)

# Sub_2 class
print("Sub_2 class:\n")
fname_3 = input("Enter first name\n~ ")
lname_3 = input("Enter last name\n~ ")

class_of_sub_2 = Sub2(fname_3, lname_3, year_2, department_1, university_1)

# Print all class
print(class_of_main)
print(class_of_sub_1)
print(class_of_sub_2)
