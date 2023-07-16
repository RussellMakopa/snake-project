#Team Members : Russy Makopa and Khaleel Manderson
# 
# Russell
# I helped with the foundational set up of the program.
# I helped research the information needed to be gathered to start the set up.
# Created the initial idea of the project.
# As well as planned meeting times to discuss roles in creating the program.
# To end it off I helped with testing out errors in the programming. 
# 
#Khaleel 
# I furthered the completion of the project by adding in cosmetic features to the different snakes.
# I created the second snakes movements as well as color pattern. I edited the issue with the food overlapping the score
# by fixing the boundaries of where the food may appear. Edit the initial point system to add 5 points instead of ten while also
# creating a whole new player to the game that may be able to play at the same time as the other player and collect points.







import turtle
import time
import random
delay = 0.1
#Player 1 Score
score = 0
high_score = 0

#Player 2 Score
score2 = 0
high_score2 = 0


#Initial creation of color for snakes 
color1 = "red"
color2 = "red"
color3 = "blue"
color4 = "blue"


#creating the boundary in which our snake is going to be roaming in looking for food.
wn = turtle.Screen()
wn.title("Snake The Hunter")
wn.bgcolor('black')
wn.setup(width=700, height=700)
wn.tracer(0)
#Setting up player 1 and their placement 
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color(color1)
head.penup()
head.goto(-145,-145)
head.direction = "stop"

#Setting up player 2 and their placement created edited by us 
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("circle")
head2.color(color3)
head2.penup()
head2.goto(145,-145)
head2.direction = "stop"

#Creation of the food for the players to collect
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0,100)

#Setting up Score board
segments = []
segments2 = []

#Player 1 Score 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("    Player 1 Score:0 High score:0", align = "right", font=("Lucida Console", 12, "normal"))

#Created for space
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.shape("square")
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(0,260)

#Player Two Score
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,260)
pen2.write("  Player 2 Score:0 High score:0", align = "left", font=("Lucida Console", 12, "normal"))


#these functions put out the direcion of the snakes using
# if statements. The direction are based on which direction the heads are facing.
def go_up():
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
#All go functions are for Player 2 creation by us
def go_up2():
    if head2.direction != "down":
        head2.direction = "up"
def go_down2():
    if head2.direction != "up":
        head2.direction = "down"
def go_left2():
    if head2.direction != "right":
        head2.direction = "left"
def go_right2():
    if head2.direction != "left":
        head2.direction = "right"
        
        
        
#the movement of the snakes around the boundary.
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y+20)
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y-20)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x-20)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x+20)




#asigning the keyboard keys to control the movement of the snake.
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_up2, "Up")
wn.onkeypress(go_down2, "Down")
wn.onkeypress(go_left2, "Left")
wn.onkeypress(go_right2, "Right")

while True:
    wn.update()
    #Setting the boundarys and limitations of the gaming
    #Editing to account for second snake addition
    
    #For failure
    if head.xcor()>330 or head.xcor()<-330 or head.ycor()>335 or head.ycor()<-335:
        time.sleep(1)
        head.goto(-145,-145)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("   Player 1 Score:{} High score:{}   ".format(score, high_score),align="right", font=("Lucida Console", 12, "normal"))
        
    if head.distance(food) <20:
        #Edited in pattern for snake
        if color2 == color1:
            color2= "lightgreen"
        else:
            color2= "red"
        #Edited Food random placement to fix overlap onto score
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        food.goto(x,y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color(color2)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("   Player 1 Score:{} High score:{}".format(score, high_score),align="right", font=("Lucida Console", 12, "normal"))
        
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("   Player 1 Score:{} High score:{}  ".format(score, high_score),align="right", font=("Lucida Console", 12, "normal"))
    #Player 2's snake 
    if head2.xcor()>330 or head2.xcor()<-330 or head2.ycor()>335 or head2.ycor()<-335:
        time.sleep(1)
        head2.goto(145,-145)
        head2.direction = "stop"
        for segment in segments2:
            segment.goto(1000,1000)
        segments2.clear()
        score2 = 0
        delay = 0.1
        pen2.clear()
        pen2.write("  Player 2 Score:{} High score:{}".format(score2, high_score2),align="left", font=("Lucida Console", 12, "normal"))
        
    if head2.distance(food) <20:
        #Edited in pattern for snake
        if color4 == color3:
            color4= "lightblue"
        else:
            color4= "blue"
        #Edited Food random placement to fix overlap onto score
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        food.goto(x,y)
        new_segment2 = turtle.Turtle()
        new_segment2.speed(0)
        new_segment2.shape("circle")
        new_segment2.color(color4)
        new_segment2.penup()
        segments2.append(new_segment2)
        delay -= 0.001
        score2 += 5
        if score2 > high_score2:
            high_score2 = score2
        pen2.clear()
        pen2.write("  Player 2 Score:{} High score:{}".format(score2, high_score2),align="left", font=("Lucida Console", 12, "normal"))
    for index in range(len(segments2)-1,0,-1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x,y)
    if len(segments2)>0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x,y)
    move2()
    #For Failure
    for segment in segments2:
        if segment.distance(head)<20:
            time.sleep(1)
            head2.goto(0,0)
            head2.direction = "stop"
            for segment in segments2:
                segment.goto(1000,1000)
            segments2.clear()
            score2 = 0
            delay = 0.1
            pen2.clear()
            pen2.write("  Player 2 Score:{} High score:{}".format(score2, high_score2),align="left", font=("Lucida Console", 12, "normal"))
    time.sleep(delay)
wn.mainloop()







# go = turtle.Screen()
# go.title("GAME OVER")
# go.bgcolor('black')
# go.setup(width=600, height=600)
# go.tracer(0)
# pen2 = turtle.Turtle()
# pen2.speed(0)
# pen2.shape("square")
# pen2.color("red")
# pen2.penup()
# pen2.hideturtle()
# pen2.goto(0,0)
# pen2.write("Game Over", align = "center", font=("Courier", 24, "normal"))