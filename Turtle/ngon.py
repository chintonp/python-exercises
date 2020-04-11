import turtle

def setup():
    """ Provide the config for the screen """
    turtle.title('Turtle n-gon Exercise')
    turtle.setup()
    #turtle.hideturtle()


def draw_ngon(n, size):
    angle = int(360/n)
    for _ in range(n):
        turtle.forward(size)
        turtle.left(angle)


edge_size = 50
nsides = 8

setup()

left_angle = int(360/nsides)
right_angle = int((nsides - 2) * 180 / nsides)

for _ in range(2):
    turtle.forward(edge_size)
    turtle.left(left_angle)
    draw_ngon(nsides, edge_size)
    turtle.right(right_angle) 


# Add this so that the window will close when clicked on
turtle.exitonclick()