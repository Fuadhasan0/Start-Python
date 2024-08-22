class personal_info:
       def __init__(seft, fname, lname):
              seft.fname = fname
              seft.lname = lname
       def __str__(seft):
              return f"Name: {seft.fname} {seft.lname}"
       
class academic_info:
       def __init__(seft, year, department, Univarsity):
              seft.year = year
              seft.department = department
              seft.univarsity = Univarsity
       def __str__(seft):
              return f"Year: {seft.year}\tDepartment: {seft.department}\t Univarsity: {seft.univarsity}"

class Main(personal_info, academic_info):
       def __init__(seft, fname, lname, year, department, Univarsity):
              personal_info.__init__(seft, fname, lname)
              academic_info.__init__(seft, year, department, Univarsity)
       def __str__(seft):
              return f"{personal_info.__str__(seft)}\t{academic_info.__str__(seft)}"
       
class Sub_1(Main):
       def __init__(seft, fname, lname, year, department, univarsity):
               super().__init__(fname, lname, year, department, univarsity)

class Sub_2(Sub_1):
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

class_of_sub_1 = Sub_1(fname_2, lname_2, year_2, department_1, university_1)

# Sub_2 class
print("Sub_2 class:\n")
fname_3 = input("Enter first name\n~ ")
lname_3 = input("Enter last name\n~ ")

class_of_sub_2 = Sub_2(fname_3, lname_3, year_2, department_1, university_1)

# Print all class
print(class_of_main)
print(class_of_sub_1)
print(class_of_sub_2)
       
              
              