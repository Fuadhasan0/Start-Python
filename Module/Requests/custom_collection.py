class main:
       def __init__(seft, item):
              seft.item = item
              seft.index = 0
       def __iter__(seft):
              return seft
       def __next__(seft):
                    if seft.index < len(seft.item):
                           item = seft.item[seft.index]
                           seft.index += 1
                           return item
                    else:
                           raise StopIteration
                    
input_item = input("Enter item and separeted by comma(-,-,-,)\n~ ")
input_item = list(map(str,input_item.split(",")))

result = main(input_item)

for x in result:
       print(x)                    