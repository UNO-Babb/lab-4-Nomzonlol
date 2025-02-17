#TurtleGraphics.py
#Name:Nomaan Ahmed
#Date:2/16/25
#Assignment:Lab 4

import turtle

def drawSquare(myTurtle, size):
    """Draws a square of given size."""
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def fillQuadrant(myTurtle, size, quadrant):
    """Fills the specified quadrant of a larger square."""
    
    # Draw the main square
    drawSquare(myTurtle, size)
    myTurtle.penup()
    
    # Position for top-left quadrant
    myTurtle.goto(-size/2, size/2)  # Go to start of main square
    myTurtle.forward(size/4)  # Move right by 1/4 of the size
    myTurtle.right(90)  # Face downward
    myTurtle.forward(size/4)  # Move down by 1/4 of the size
    myTurtle.left(90)  # Face right again
    
    myTurtle.pendown()
    myTurtle.fillcolor("black")
    myTurtle.begin_fill()
    drawSquare(myTurtle, size/2)  # Draw the filled square half the size of original
    myTurtle.end_fill()

def main():
    # Set up the turtle
    myTurtle = turtle.Turtle()
    myTurtle.speed(3)
    
    # Center the drawing
    myTurtle.penup()
    myTurtle.goto(-50, 50)  # Starting point for main square
    myTurtle.pendown()
    
    # Draw and fill the square
    fillQuadrant(myTurtle, 100, 1)
    
    turtle.done()

main()
