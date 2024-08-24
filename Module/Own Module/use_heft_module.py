from main_module import main

name_inp = input("Enter name\n~ ")
age_inp = input("Enter age\n~ ")       
job_inp = input("Enter job\n~ ")

result = main(name_inp, age_inp, job_inp)
print(result)