import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black') # Set the background color

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0) # Set the fastest speed
spiral_turtle.width(2) # Set the width of the turtle's pen

# Define colors
colors = ['red','orange','yellow','green','darkblue','purple']

# Draw a colorful spiral
for i in range(360):
	spiral_turtle.pencolor(colors[i % 6]) # Change color
	spiral_turtle.forward(i) # Move forward
	spiral_turtle.right(59) # Turtle right
	
# Hide the turtle and finish
spiral_turtle.hideturtle()
turtle.done()