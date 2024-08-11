def add_number(number):
       result = 0
       for number in number:
              result += number
       return result

number = input("Enter number and separetion with comma(-,-,-,)\n~ ")
number = list(map(int,number.split(',')))

result = add_number(number)

print("Summetion of list is",result)       

# function of sum is sum of all element in list

li = input("Enter number and separetion with comma(-,-,-,)\n~")
li = list(map(int,li.split(',')))
result = sum(li)

print("Summetion of list is", result)