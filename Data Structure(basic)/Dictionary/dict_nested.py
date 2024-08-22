info = {
       "student_1": {
              "Name": "Fuad Hasan",
              "Roll": "4079"
       },
       "student_2": {
              "Name": "Kazi Sohag",
              "Roll": "4080"
       },
       "student_3": {
              "Name": "Ratul Hasan Pabel",
              "Roll": "4064"
       },
       "student_4": {
              "Name": "Md. Rakibul Hasan Rabbi",
              "Roll": "4060"
       }
}

print(info)

x = info.keys()       
print(x) 

for x in info:
       print(info[x])

print(info["student_2"]["Name"])

for x, obj in info.items():
       print(x)
       for y in obj:
              print(y + ":" , obj[y])
              
              