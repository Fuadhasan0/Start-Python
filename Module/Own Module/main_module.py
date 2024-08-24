class main:
       def __init__(seft, name, age, job):
              seft.name = name
              seft.age = age
              seft.job = job
       def __str__(seft):
              return f"Name: {seft.name}\tAge: {seft.age}\tJob: {seft.job}."
       
n = int(input("Who many time you run this code?\n~ "))
i = 0
result = None

while i<n:
       name_inp = input("Enter name\n~ ")
       age_inp = input("Enter age\n~ ")
       job_inp = input("Enter job\n~ ")
       
       result = main(name_inp, age_inp, job_inp)
       i += 1

print(result)       
       