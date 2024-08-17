import turtle
import random

color = ["red", "green", "blue", "yellow", "orange"]
turtle.penup()

for i in range(100):
       turtle.speed(10)
       x = random.randint(-200, 200)
       y = random.randint(-200, 200)
       turtle.setposition(x, y)
       i = random.randint(0, len(color)-1) # If you use (0, len(color)), you mean index is 5. But index is 4 .That's why loop come in 5 , it's not found and then you see error. 
       turtle.dot(color[i])
       
       
turtle.exitonclick()       

