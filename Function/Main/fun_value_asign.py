def myfun(x, z, y=10):
       print("X =", x,"Y =",y,"Z =", z)
       
myfun(x=1, y=2, z=5)
a = 5
b = 6
myfun(x = a, z = b)
a = 1
b = 2
c = 3
myfun(y = a, z = b, x = c)   