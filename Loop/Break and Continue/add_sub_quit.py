terminate = False
while not terminate:
       number1 = input("Enter a number\n~ ")
       number2 = input("Enter another number\n~ ")
       number1 = int(number1)
       number2 = int(number2)
       
       while True:
              operation = input("Enter add/sub or quit to exit\n~ ")
              if operation == "quit || Quit":
                     terminate == True
                     break
              if operation not in ["add", "sub"]:
                     print("Unknown operation")
                     continue
              if operation == "add":
                     print("Result is", number1 + number2)
                     break
              if operation == "sub":
                     print("Result is", number1 - number2)
                     break
              