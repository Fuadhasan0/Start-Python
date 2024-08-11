import turtle

def rectangle(length):
       turtle.shape("turtle")
       turtle.color("red")
       turtle.speed(1)
       counter = 0
       while counter < 4:
              turtle.forward(length)
              turtle.left(120)
              counter += 1
       

length = input("Enter length\n~ ")
length = int(length)

rectangle(length)
turtle.exitonclick()