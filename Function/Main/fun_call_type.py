def info(*name):
       print("My name is " + name[2])
       
info("Sohag", "Pabel", "Fuad", "Ratul") 

def info_1(**name):
       print("My name is " + name["n2"])
       
info_1(n1 = "Sohag", n2 = "Pabel", n3 = "Fuad", n4 = "Ratul")     

def info_3(name = "Fuad"):
       print("My name is " + name)
       
info_3("Sohag")
info_3("Pabel") 
info_3()
info_3("Ratul")

def info_3(n):
       for x in n:
              print("My name is " + x)
              
name = ["Sohag", "Pabel", "Fuad", "Ratul"]              
info_3(name) 

