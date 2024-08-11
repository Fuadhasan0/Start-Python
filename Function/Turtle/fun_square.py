import turtle

def draw_square(side_length):
       for i in range(4):
              turtle.forward(side_length)
              turtle.left(90)

num_of_square = input("Enter who many square you need\n~ ")
gap = input("Enter who mach gap between two square\n~ ")
num_of_square = int(num_of_square)
gap = int(gap)

counter = 0
while counter < num_of_square:
       draw_square(100)
       turtle.right(gap)
       turtle.speed(10)
       counter += 1
turtle.exitonclick ()     