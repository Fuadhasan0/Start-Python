def recursive(n):
       if n>0:
              result = n * recursive(n-1)
              print(result)
       else:
              result = 1
       
       return result

print("Recursive\n")
recursive(6)              