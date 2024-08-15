p = int(input("Who many dictionary?\n~ "))

my_fun = {}

for _ in range(p):
       name = str(input("Enter name\n~"))
       roll = int(input("Enter roll\n~ "))
       my_fun[name] = roll
       
print("Output\n~\n ", my_fun) # first output for this


import pprint

pprint.pprint(my_fun)  # second output for this
    