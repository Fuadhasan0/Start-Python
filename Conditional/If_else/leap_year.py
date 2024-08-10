year = input("Enter year\n~ ")
year = int(year)

if year % 4 == 0:
       if year % 100 == 0:
              if year % 400 == 0:
                     print(year,"is a leap year.\n")
              else:
                     print(year,"isn't a leap year.\n")       
       else:
              print(year,"is a leap year.\n") 
else:
       print(year,"isn't a leap year.\n")                           

                            