print("In this project, there are 4 different patterns which can be drawn, and all can be drawn by the click of one key on a keyboard. If you press the 'a' key on your keyboard, a white pattern consisting of triangles will be drawn. Or, if you press the 'b' key on your keyboard, an orange pattern consisting of squares will be drawn. On the other hand, if you press the 'c' key on your keyboard, a blue pattern consisting of a spiral will be drawn. Finally, if you press the 'd' key on your keyboard, a red pattern consisting of circles will be drawn.")
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
window.setup(1000, 1000)
window.bgcolor("black")
random_turtle = turtle.Turtle()



def drawTriangle():
  random_turtle.forward(100)
  random_turtle.left(120)
  random_turtle.forward(100)
  random_turtle.left(120)
  random_turtle.forward(100)
  random_turtle.pencolor("white")

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

def drawSquare():
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.forward(100)
  random_turtle.left(90)
  random_turtle.forward(100)
  random_turtle.pencolor("orange")

def pattern():
  x = 0
  while x < 36:
    drawSquare()
    random_turtle.right(100)
    x += 1

window.onkey(pattern, "b")
window.listen()

def spiral():
  x = 10
  for i in range(x * 4):
    random_turtle.forward(i * 10)
    random_turtle.left(90)
    random_turtle.pencolor("blue")
    x += 1

window.onkey(spiral, "c")
window.listen()

def Circle():
  random_turtle.circle(100)
  random_turtle.pencolor("red")

def pattern2():
  x = 0
  while x < 50:
    Circle()
    random_turtle.left(50)
    x += 1


window.onkey(pattern2, "d")
window.listen()



# Key bind events: clicking or pressing of keys/buttons to activate things on the screen.
# Ex. Clicking mouse buttons to select something, pressing letter keys on a keyboard to type
# Event handling (programming): "listen" in for something to happen, if it happens run code.