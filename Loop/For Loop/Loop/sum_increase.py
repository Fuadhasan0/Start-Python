"""1st code: Where increase 1 between two number"""

print("Increase 1 between two number:")

num_start = input("Enter start number\n~ ")
num_end = input("Enter end number\n~ ")
result = 0

num_start = int(num_start)
num_end = int(num_end)

for num in range(num_start, num_end+1):
       result += num
       
print("Summetion is",result,"\n")   

"""2nd code: Where increase 5 between two number"""   

print("Increase 5 between two number:") 

num_start = input("Enter start number\n~ ")
num_end = input("Enter end number\n~ ")
result = 0

num_start = int(num_start)
num_end = int(num_end)

for num in range(num_start, num_end+1, 5):
       result += num
       
print("Summetion is",result)       