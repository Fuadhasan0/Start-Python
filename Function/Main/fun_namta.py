def myfun(num):
       
       for i in range(1, 11):
              if num == 0:
                     num = 1
              print(i,"X",num,"=",i*num)       
       
                     
              

number_of_namta = input("Enter number of namta\n~ ")
number_of_namta = int(number_of_namta)

print(number_of_namta,"namta:\n")
result = myfun(number_of_namta)
