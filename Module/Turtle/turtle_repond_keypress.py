import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    my_turtle.forward(50)
    
def move_backward():
       my_turtle.backward(50)
       
def move_left():
       my_turtle.left(50)  
       
def move_right():
       my_turtle.right(50)                

screen.listen()
screen.onkey(move_forward, "f")  # Move forward when "f" is pressed
screen.onkey(move_backward, "b") # Move backward when "b" is pressed
screen.onkey(move_left, "l") # Move left when "l" is pressed
screen.onkey(move_right, "r") # Move right when "r" is pressed

screen.mainloop()
