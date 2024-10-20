# QUESTION 10
# Open "numbers.txt" in write mode and write numbers from 1 to 100, each on a new line
with open("numbers.txt", "w") as file: 
    for i in range(1, 101):  
        file.write(f"{i}\n") 

# QUESTION 14 - Drawing shapes using the turtle module

from turtle import Turtle, done

# Initialize turtle object
t = Turtle()

# Function to draw an equilateral triangle
def triangle():
    t.pencolor("red")
    for _ in range(3):
        t.forward(200)
        t.right(120)

# Function to draw a circle at a specific position
def draw_circle():
    t.penup()
    t.setposition(200, 100)
    t.pencolor("blue")
    t.pendown()
    t.circle(100)

# Function to draw a star-like pattern of spikes
def spikes():
    t.penup()
    t.setposition(-600, 100)
    t.pencolor("black")
    t.pendown()
    t.left(75)
    for _ in range(5):
        t.forward(200)
        t.right(150)
        t.forward(200)
        t.left(150)

# Call the drawing functions
triangle()
draw_circle()
spikes()

# Hide the turtle and complete the drawing
t.hideturtle()
done()

# Additional turtle drawings

# Function to draw an octagon
def octogon(t, x, y, color):
    t.pencolor(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    for _ in range(8):
        t.forward(80)
        t.right(45)

# Function to draw a spiral
def spiral(t, x, y, color):
    distance = 0.2
    angle = 40
    t.pencolor(color)
    t.penup()
    t.setposition(x, y)
    t.pendown()
    for _ in range(100):
        t.forward(distance)
        t.left(angle)
        distance += 0.5

# Draw octagon and spiral
octogon(t, -45, 100, 'red')
spiral(t, 0, 0, 'blue')

# Function to draw a star
def star():
    t.pencolor("red")
    for _ in range(5):
        t.forward(150)
        t.right(144)

# Function to draw a pentagon
def pentagon():
    t.pencolor("red")
    for _ in range(5):
        t.forward(150)
        t.right(72)

# Draw star and pentagon
star()
t.penup()
t.setposition(200, -150)
t.pendown()
pentagon()

# Function to draw a grid of specified rows, columns, and cell size
def draw_grid(rows, cols, cell_size):
    for i in range(rows + 1):  # Draw horizontal lines
        t.penup()
        t.setposition(0, i * cell_size)
        t.pendown()
        t.forward(cols * cell_size)

    t.left(90)  # Turn to draw vertical lines
    for j in range(cols + 1):  # Draw vertical lines
        t.penup()
        t.setposition(j * cell_size, 0)
        t.pendown()
        t.forward(rows * cell_size)

# Draw a 5x5 grid with cell size of 50 units
draw_grid(5, 5, 50)

# Hide the turtle and complete the drawing
t.hideturtle()
done()
