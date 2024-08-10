import turtle

turtle.color("black")
turtle.speed(10)

counter = 0
while counter < 36: # Who many shape create
       for i in range(4): # one square
              turtle.forward(100)
              turtle.right(90)
       turtle.right(10) # space between two square
       counter += 1
       
turtle.exitonclick()              