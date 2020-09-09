# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:48:23 2020

@author: hp
"""

import turtle


#game window
game_window = turtle.Screen()
game_window.title('Ping Pong Ultimate')
game_window.bgcolor('white')
game_window.setup(width=800,height=600)
game_window.tracer(0)     #stops window from updating



#scoring system
score_a = 0
score_b = 0


#Player A

player_A = turtle.Turtle() #turtle object
player_A.speed(0) #speed of animation(max speed)
player_A.shape('square')
player_A.color('black')
player_A.penup()    #not draw while moving
player_A.goto(-375,0)
player_A.shapesize(stretch_wid=5,stretch_len=1)  #by default 20x20 so now 20*5 and 20*1



#Player B
player_B= turtle.Turtle() #turtle object
player_B.speed(0) #speed of animation(max speed)
player_B.shape('square')
player_B.color('black')
player_B.penup()    #not draw while moving
player_B.goto(375,0)
player_B.shapesize(stretch_wid=5,stretch_len=1)  #by default 20x20 so now 20*5 and 20*1




#Pong Ball
pB = turtle.Turtle() #turtle object
pB.speed(0) #speed of animation(max  speed)
pB.shape('circle')
pB.color('blue')
pB.penup()    #not draw while moving
pB.goto(0,0) #player_B.shapesize(stretch_wid=5,stretch_len=1)  #by default 20x20 so now 20*5 and 20*1
pB.dx = 0.2
pB.dy = 0.2



#pen for scoring
score = turtle.Turtle()
score.speed(0)
score.color('black')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A : 0  - -  0 : Player B", align='center',font=('Impact',24,'normal'))
#functions
def player_A_up():
    y = player_A.ycor()  #return y cordinate
    y += 20 
    player_A.sety(y)
    
def player_A_down():
    y = player_A.ycor()  #return y cordinate
    y -= 20 
    player_A.sety(y)
    
def player_B_up():
    y = player_B.ycor()  #return y cordinate
    y += 20 
    player_B.sety(y)
    
def player_B_down():
    y = player_B.ycor()  #return y cordinate
    y -= 20 
    player_B.sety(y)
    
    
#keyboad binding
game_window.listen() #listen for keyboard input
game_window.onkeypress(player_A_up,'w') #when clicked w key
game_window.onkeypress(player_A_down,'s') #when clicked s key
game_window.onkeypress(player_B_up,'Up') #when clicked w key
game_window.onkeypress(player_B_down,'Down') #when clicked s key






#MAIN GAME-always in loop

while True:
    game_window.update()
    
    #move ball
    pB.setx(pB.xcor() + pB.dx)
    pB.sety(pB.ycor() + pB.dy)
    
    #border checking
    if pB.ycor() > 290:
        pB.sety(290)
        pB.dy *= -1
        
    if pB.ycor() < -290:
        pB.sety(-290)
        pB.dy *= -1
        
    if pB.xcor() > 390:
        pB.goto(0,0)
        pB.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A : " +str(score_a)+"  - -  "+str(score_b)+ " : Player B", align='center',font=('Impact',24,'normal'))

        
    if pB.xcor() < -390:
        pB.goto(0,0)
        pB.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A : " +str(score_a)+"  - -  "+str(score_b)+ " : Player B", align='center',font=('Impact',24,'normal'))
   
        #paddle boundary
    if player_A.ycor() > 240:
        player_A.sety(240)
        
    if player_A.ycor() < -240:
        player_A.sety(-240)
        
    if player_B.ycor() > 240:
        player_B.sety(240)
        
    if player_B.ycor() < -240:
        player_B.sety(-240)
        
     #bouncing
     
    if(pB.xcor() > 360 and (pB.ycor() < player_B.ycor()+40 and pB.ycor() > player_B.ycor()-40)):
        pB.setx(360)
        pB.dx *= -1
    
    if(pB.xcor() < -360 and (pB.ycor() < player_A.ycor()+40 and pB.ycor() > player_A.ycor()-40)):
        pB.setx(-360)
        pB.dx *= -1