# Normal 
name = [(1, "Labib"), (2, "Hasan"), (3, "Tahmid"), (4, "Fuad")]

sorted_name = sorted(name, key=lambda name: name[1])
print(name)
print(sorted_name)

# With a function
def sorted_list(name_1):
       sorted_name_1 = sorted(name_1, key=lambda name_1: name_1[1])
       return sorted_name_1
       
name_1 = [(1, "Labib"), (2, "Hasan"), (3, "Tahmid"), (4, "Fuad"), (5, "Sohag")]
after_name_1 = sorted_list(name_1)

print(name_1)
print(after_name_1)
