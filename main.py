import turtle
# Change the drawing window dimensions (units of measurement: pixels)
# Change the drawing pen size
# Change the shape of the turtle
# Change the background color

# Turtle Events
# Event (programming): Code that is run when something happens on the computer
# window = turtle.Screen()
# window.bgcolor("blue")
# turtle = turtle.Turtle()
# turtle.pensize(10) # Units of measurement in pixels
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.color("orange")

# # Changing the shape of the turtle
# turtle.shape("turtle")
# arrow
# square
# turtle
# triangle
# circle
# classic

# Practice with Turtle Events
window = turtle.Screen()
window.setup(500, 500)
random_turtle = turtle.Turtle()


def drawTriangle():
  random_turtle.forward(100)
  random_turtle.left(120)
  random_turtle.forward(100)
  random_turtle.left(120)
  random_turtle.forward(100)

def pattern():
  x = 0
  while x < 36:
    drawTriangle()
    random_turtle.right(100)
    x += 1
  # Incrementing a variable
  # x = x + 1
  # Decrementing a value
  # x = x - 1

window.onkey(pattern, "a")
window.listen()

# Key bind events: clicking or pressing of keys/buttons to activate things on the screen.
# Ex. Clicking mouse buttons to select something, pressing letter keys on a keyboard to type
# Event handling (programming): "listen" in for something to happen, if it happens run code.