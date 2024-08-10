#1st way

result = 0
num = 1

for num in range(1, 50):
       if num % 2 ==0:
              print(num)
       result += num
       num = num + 2
       
print("1st Summetion is",result)

print("-------------------------------------")

#2nd way

result = 0
for num in range(51): #automatically num = 1 assign
       if num % 2 == 0:
              print(num)
       result = result + num # result and num pera rally increase
       
print("2nd Summetion is",result)