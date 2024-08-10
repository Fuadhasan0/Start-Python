marks = input("Enter a number\n~ ")
marks = int(marks)

if marks >= 80:
       grade = "A+"
elif marks >=  70:
       grade = "A"
elif marks >=60:
       grade = "B"
elif marks >50:
       grade = "C"
elif marks >= 40:                          
       grade = "D"
else:
       grade = "F"       

print("Your marks is:", marks,"\t Your grade is:", grade)       