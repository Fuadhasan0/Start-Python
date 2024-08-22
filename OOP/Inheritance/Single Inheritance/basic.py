# Start main class
class main:
       def __init__(seft, fname, lname, year, college_name):
              seft.fname = fname
              seft.lname = lname
              seft.year = year
              seft.college_name = college_name
              
       def __str__(seft):
              return f"Name: {seft.fname} {seft.lname}\nYear: {seft.year}\nCollege Name: {seft.college_name}"

# Start sub class       
class sub(main):
       def __init__(seft, fname, lname, main_instanse):
              super().__init__(fname, lname, main_instanse.year, main_instanse.college_name)                  

# Input all value       
fname_1 = input("Enter first name\n~ ")
lname_1 = input("Enter last name\n~ ")
year = input("Enter year\n~ ")
college_name = input("Enter College name\n~ ")

# call main class
cls_main = main(fname_1, lname_1, year, college_name)
print(cls_main, "\n")

# input some value
n = int(input("Who main time you run this code?\n~ "))

# call sub class and work with loop
i = 0
while i<n:
       
       fname_2 = input("Enter first name\n~ ")
       lname_2 = input("Enter last name\n~ ")

       cls_sub = sub(fname_2, lname_2, cls_main)
       print(cls_sub, "\n")
       i += 1
