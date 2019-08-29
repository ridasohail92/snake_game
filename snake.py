# Snake Game in Python 3 using turtle
# By @Rida
# 29 August 2019

import turtle
import time
import random

delay = 0.1 #seconds

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Rida")
wn.bgcolor("black")
wn.setup(width=500, height=500) # he did 600 600
# We put our game between tracer and mainloop
wn.tracer(0) # turns off the animation on screen

# Snake head
head = turtle.Turtle()
head.speed(0) # this is the animation speed of Turtle module..this is the fastest
head.shape("square") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
head.color("red")
head.penup() # means no drawing when moving
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0) # this is the animation speed of Turtle module..this is the fastest
food.shape("circle") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
food.color("green")
food.penup() # means no drawing when moving
food.goto(0,100)


segments = [] # for body of snake

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))


# Functions
def go_up():
  # this is to prevent the snake from killing itsel when reversed key pressed during playing
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"

def go_right():
  if head.direction != "left":
    head.direction = "right"
  

def move():
  if head.direction == "up":
    head.sety(head.ycor() + 20)

  if head.direction == "down":
    head.sety(head.ycor() - 20)

  if head.direction == "left":
    head.setx(head.xcor() - 20)

  if head.direction == "right":
    head.setx(head.xcor() + 20)

# Keyboard bindings - it connects a key press to a particular function
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main game loop
while True:
  wn.update() # it updates the screen

  # Check for collision with the border
  if head.xcor()>230 or head.xcor()<-230 or head.ycor()>230 or head.ycor()<-230:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
      segment.goto(1000, 1000)

    # Clear the segment list
    segments.clear()

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1

    pen.clear()
    pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 20, "normal"))



  # Check for collison with food
  if head.distance(food) < 20: # width/height of each turtle is 20 pixel; so from the mid the radius is 10 pixel and two object's 10 pixel equals 20. IN short it means that the two objects have collided
    # Move the food to a random spot 
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    food.goto(x,y)

    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    # Shorten the delay - as as more segments are added the game gets slow - Turtle thing
    # also the speed of game inc hence inc the difficulty of game
    delay -= 0.001

    # Increase the score
    score += 10

    if score > high_score:
      high_score = score

    pen.clear()
    pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 20, "normal"))

  

  # Move the end segment to first i.e. in reverse order
  for index in range(len(segments)-1, 0, -1):
    # find coordinates of second last segment
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()

    # set position of last segment to second last segment
    segments[index].goto(x,y)

  # Move segment 0 to where the head is; special case
  if len(segments) > 0: # meanign once we have one body part atlease then run this
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)



  move()

  # Check for head collision with the body segments
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      # Hide the segments
      for segment in segments:
        segment.goto(1000, 1000)

      # Clear the segment list
      segments.clear()

      # Reset the score
      score = 0

      # Reset the delay
      delay = 0.1
      
      pen.clear()
      pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 20, "normal"))


  time.sleep(delay)




wn.mainloop()

