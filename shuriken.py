from turtle import Turtle, mainloop

t = Turtle()

def circle():
 t.penup()
 t.setposition(90, 90)
 t.pencolor("blue")
 t.pendown()
 t.circle(10) 
 t.penup


circle()

# Function to draw one arm of the shuriken
def draw_arm():
    for _ in range(1):
        t.forward(100)   # Draw one side of the arm
        t.left(60)      # Sharp turn for the inner point
        t.forward(100)   # Draw the other side of the arm
        t.left(120)     # Turn back to start position

# Draw four arms to make the shuriken
for _ in range(4):
    draw_arm()
    t.left(90)  # Rotate 90 degrees to draw the next arm

t.hideturtle()  # Hide the turtle after drawing
mainloop()  # Keep the window open
