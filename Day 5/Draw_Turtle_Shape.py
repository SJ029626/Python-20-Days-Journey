import turtle
def square_draw(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create The turtle Brads-Draw a Square
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    square_draw(brad)
    #Create the turtle angie- Draw A square
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("Blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
