txt = ["I", "am", "Fuad", "Hasan"]

# for loop 1st way
for i in txt:
       print(i)

#for loop 2nd way
for i in range(len(txt)):
       print(txt[i])
       
# for loop 3rd way       
[print(x) for x in txt]

# while loop
i = 0 
while i < len(txt):
       print(txt[i])
       i += 1
       
