class number:
       def __iter__(seft):
              seft.a = 1
              return seft
       def __next__(seft):
              x = seft.a
              seft.a += 1
              return x
       
myclass = number()
result = iter(myclass)

n = int(input("Who many number you print?\n~ "))
for x in range(n):
       print(next(result))
