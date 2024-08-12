import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()

def go_to(x, y):
    my_turtle.goto(x, y)

screen.onclick(go_to)
screen.mainloop()
