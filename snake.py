# Turtle is a pre-installed Python library that enables users to create pictures and shapes by providing them with a virtual canvas. It is mainly used for drawing.
import turtle
# The time() function returns the number of seconds passed.
import time
# Import random module, which contains a variety of things to do with random number generation.
import random
# Initialising the delay to 0.1 
delay = 0.1
# Initialising the delay to 0.1 
# Initially the score and highscore is assigning to zero
# turtle.screen() is a method to configure the screen properties.
# Using sd.title(), we giving name as ìsnake gameî. 
#  Screen background colour is blue.
# Size setup upto width equal to 600 height equal to 600.
# After finishing configuring
s = 0
hs = 0
sd = turtle.Screen()
sd.title("Snake Game")
sd.bgcolor("blue")
sd.setup(width=600, height=600)
# Configuring the properties of head from method turtle.Turtle() designing the head properties.
# Head shape is square.
# Initialising speed is zero.
# Making colour of head is black.
# penup is used to pick up total without leaving tracks when the error exception handling occurs ,	
sd.tracer(0)
h = turtle.Turtle()
h.speed(0)
h.shape("square")
h.color("black")
h.penup()
# Hence, it will stop.
# By using method turtle.Turtle() initially the item speed is zero(static).
# Shape of item is circle.
# Colour of item is red.
# penup method tells to leave the ink on the screen.
#  it will go up to 0 to 100 range.
h.goto(0,0)
h.direction = "stop"
item = turtle.Turtle()
item.speed(0)
item.shape("circle")
item.color("red")
item.penup()
item.goto(0,100)
# Hence, it will stop.
# By using method turtle.Turtle() initially the item speed is zero(static).
# Shape of item is circle.
# Colour of item is red.
# penup method tells to leave the ink on the screen.
#  it will go up to 0 to 100 range.
#  Making a list for segments as new_layer.
# Pen is method containing dictionary with some keys and it is assigning to turtle.Turtle().
# Initial speed is zero.	
# when snake catches it will add another square.
# Colour of the square is in white color.
# penup() method is used to add the further items.
new_layer = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
# It will hide turtle and it describes the size ,alignment and font size of score and highscore.
pen.goto(0, 260)
pen.write("SCORE: 0  HIGH SCORE: 0", align="center", font=("Courier", 24, "normal"))
# Defining the go up function.
# If head direction is not equal to down then head direction is assigned to upper
def go_up():
    if h.direction != "down":
        h.direction = "up"
#  Defining the go down function.
#  If head direction is not equal to up then head direction is assigned to down.

def go_down():
    if h.direction != "up":
        h.direction = "down"
# Defining the go left function.
#  If head direction is not equal to right then head direction is assigned to left.

def go_left():
    if h.direction != "right":
        h.direction = "left"
# Defining the go right function.
# If head direction is not equal to left then head direction is assigned to right

def go_right():
    if h.direction != "left":
        h.direction = "right"
# Defining the move function.
# If head direction is equal to up. Assigning y varaiable to y coordinate method and setting y values to some extend

def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y + 20)
#  If head direction is equal to down. Assigning y varaiable to y coordinate method and setting y values to some extend.
    if h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)
#  If head direction is equal to left. Assigning x varaiable to x coordinate method and setting x values to some extend.
    if h.direction == "left":
        x = h.xcor()
        h.setx(x - 20)
#  If head direction is equal to right. Assigning x varaiable to x coordinate method and setting x values to some extend.
    if h.direction == "right":
        x = h.xcor()
        h.setx(x + 20)
#  keyboard pressing to move various direction is defined.
sd.listen()
sd.onkeypress(go_up, "w")
sd.onkeypress(go_down, "s")
sd.onkeypress(go_left, "a")
sd.onkeypress(go_right, "d")
#  Main game of the loop starts here. While True means, it will proceed.
while True:
#  update() method is used to update all the levels of the game.
    sd.update()
#  It will check for a collision with the border, if the xcoordinate() is greater than 290 or less than -290 or y coordinate ,it will stop.
    if h.xcor()>290 or h.xcor()<-290 or h.ycor()>290 or h.ycor()<-290:
        time.sleep(1)
        h.goto(0,0)
        h.direction = "stop"
#  Hiding the layers.
        for i in new_layer:
            i.goto(1000, 1000)
# It will clear the layers.
# Score is reseted to 0.
# Delay is reseted to 0.1

        new_layer.clear()

        s = 0

        delay = 0.1
#  It will delete the turtleís drawing from the screen.
# write() method will return the score and high score

        pen.clear()
# Checking for a collision with the item.
        pen.write("SCORE: {}  HIGH SCORE: {}".format(s, hs), align="center", font=("Courier", 24, "normal")) 


    if h.distance(item) < 20:
#  If distance is less than 20 then move the item to a random spot.
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        item.goto(x,y)
#  It will add a layer with the shape square and grey colour and it will append the new layer.
        layer_1 = turtle.Turtle()
        layer_1.speed(0)
        layer_1.shape("square")
        layer_1.color("grey")
        layer_1.penup()
        new_layer.append(layer_1)
#  It will shorten the delay.
        delay -= 0.001
#  It will shorten the delay.
# Every time catching item will increase 10 points to the score.
# If score is greater than high score then high score is assigned to score.
# It will delete the screen and it will return and display the score and high score.

        s += 10

        if (s > hs):
            hs = s
        
        pen.clear()
#  It will shorten the delay.
# Every time catching item will increase 10 points to the score.
# If score is greater than high score then high score is assigned to score.
# It will delete the screen and it will return and display the score and high score.
#  For loop is used to move the end layers first in reverse order.
#  It will move layer 0 at the head when length of layer  is  greater than zero.

        pen.write("SCORE: {}  HIGH SCORE: {}".format(s, hs), align="center", font=("Courier", 24, "normal")) 

    for i in range(len(new_layer)-1, 0, -1):
        x = new_layer[i-1].xcor()
        y = new_layer[i-1].ycor()
        new_layer[i].goto(x, y)

    if len(new_layer) > 0:
        x = h.xcor()
        y = h.ycor()
        new_layer[0].goto(x,y)
 # move() method is to move from one location to another and returns the destination.
    move()    
 #  It will check for the head collision with body layers if the distance is less than 20 and collided after it will stop.
    for i in new_layer:
        if i.distance(h) < 20:
            time.sleep(1)
            h.goto(0,0)
            h.direction = "stop"
#  It will check for the head collision with body layers if the distance is less than 20 and collided after it will stop.
#  For loop will hide the layers
#  After hiding it will clear the layers list.
#  Score is resetted,
# Delay is resetted.

            for i in new_layer:
                i.goto(10000, 10000)
        
            new_layer.clear()

            s= 0

            delay = 0.1
#  It will check for the head collision with body layers if the distance is less than 20 and collided after it will stop.
#  For loop will hide the layers
#  After hiding it will clear the layers list.
#  Score is resetted,
# Delay is resetted.
#  It will update the score display and clears the screen using clear method.
#  write() method will return the score and high score.
#  It will suspend oneís execution with some delay.

            pen.clear()
            pen.write("SCORE: {}  HIGH SCORE: {}".format(s, hs), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

sd.mainloop()