import turtle

def setup():
    """ Provide the config for the screen """
    turtle.title('Turtle Hexagon Exercise')
    turtle.setup()
    turtle.hideturtle()


def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)


edge_size = 80
setup()

for _ in range(6):
    turtle.forward(edge_size)
    turtle.left(60)
    draw_hexagon(edge_size)
    turtle.right(120) 


# Add this so that the window will close when clicked on
turtle.exitonclick()