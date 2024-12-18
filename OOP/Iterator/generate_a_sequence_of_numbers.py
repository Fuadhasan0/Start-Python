class my_rang:
       def __init__(seft, start, end):
              seft.start = start
              seft.end = end
              seft.current = start
       def __iter__(seft):
              return seft
       def __next__(seft):
              if seft.current <= seft.end:
                     number = seft.current
                     seft.current += 1
                     return number
              else:
                     raise StopIteration
              
start_inp = int(input("Enter start number\n~ "))
end_inp = int(input("Enter end number\n~ "))

result = my_rang(start_inp, end_inp)

for x in result:
       print(x)         
