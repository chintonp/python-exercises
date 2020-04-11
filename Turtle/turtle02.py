import turtle

def setup():
    """ Provide the config for the screen """
    turtle.title('Multiple Squares Animation')
    turtle.setup()
    turtle.hideturtle()


def draw_square(size):
    """ Draw a square in the current direction """
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)


setup()
for _ in range(0, 24):
    draw_square(150)
    # Rotate the starting direction
    turtle.right(105)

# Add this so that the window will close when clicked on
turtle.exitonclick()