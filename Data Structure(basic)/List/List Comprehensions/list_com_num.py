# 1st code
li = [1, 2, 3, 4, 5]
new_li = []
for x in li:
       new_li.append(2 * x)
       
print(new_li)

# 1st code(short)
li = [1, 2, 3, 4, 5]
new_li = [2*x for x in li]

print(new_li)   

# 2nd code
li = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 45, 65, 76, 84, 24, 35, 75, 99, 100]
even_num = []

for x in li:
       if x % 2 == 0:
              even_num.append(x) 
              
print(even_num)   

# 2nd code(short)
li = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 45, 65, 76, 84, 24, 35, 75, 99, 100]
even_num = [x for x in li if x % 2 == 0]

print(even_num)       
