import turtle
import random

#score
a = [0]
b = [0]

#food coord
fcoord = [0,0,0]

#position
pos = []

#head orientation
head = [0]

print "Gamemode:"
print "1. Normal"
print "2. Invisible Boundary"
chs = raw_input("Enter your choice:")
if chs == "1":
    wc = "white"
    gm = "Gamemode : Normal"
elif chs == "2":
    wc = "black"
    gm = "Gamemode : Invisible Boundary"
else:
    print "Invalid choice"

turtle.bgcolor("black")


def home(x,y):
    x = 0
    y = 0
    a[0] = 0 
    b[0] = 0
    head[0] = 0
    fcoord[2] = 0
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("red")
    turtle.goto(0,0) 
    turtle.write("Play",align="center",font=("Arial",30,"bold"))
    turtle.color("white")
    turtle.speed(5)
    turtle.goto(-45,45)
    turtle.pd()
    turtle.goto(45,45)
    turtle.goto(45,-5)
    turtle.goto(-45,-5)
    turtle.goto(-45,45)
    turtle.pu()
    turtle.goto(0,60)
    turtle.write(gm, align="center")
    turtle.title("Snake Game")
    turtle.onscreenclick(start)
    turtle.mainloop()


def boundary():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("black")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.pencolor(wc)
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    boundary()

    tfood = turtle.Turtle()

    tscore = turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.color("white")
    tscore.goto(0,-250)
    tscore.write("Score:" + str(a[0]), align="center",font=(10))
    
    while x > -205 and x < 205 and y > -205 and y <205:
        if fcoord[2] == 0:
            food(tfood)
            fcoord[2] = 1
        turtle.onkey(u,"Up")
        turtle.onkey(l,"Left")
        turtle.onkey(r,"Right")
        turtle.onkey(d,"Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()        
        if x > fcoord[0]*10-5 and x < fcoord[0]*10+5 and \
           y > fcoord[1]*10-5 and y < fcoord[1]*10+5:
            fcoord[2] = 0
            tfood.clear()
            a[0] += 1
            tscore.clear()
            tscore.write("Score:" + str(a[0]), align="center",font=(10))
        
        if len(pos) > 1:
            for i in range(1,len(pos)):
                if x < pos[i][0]+5 and x > pos[i][0]-5 and \
                   y < pos[i][1]+5 and y > pos[i][1]-5:
                        tscore.clear()
                        tfood.clear()
                        gameover()
    tscore.clear()
    tfood.clear()
    gameover()


#Food
def food(tfood):
    x = random.randrange(-20,20,1)   #Return a randomly selected element from range(start, stop, step).
    y = random.randrange(-20,20,1)
    fcoord[0] = x
    fcoord[1] = y
    tfood.hideturtle()
    tfood.pensize(1)
    tfood.pu()
    tfood.shape("turtle")
    tfood.color("red")
    tfood.goto(x*10,y*10)
    tfood.stamp()

#Up   
def u():
    if head[0] == 270:
        pass
    else:
        head[0] = 90
#Down
def d():
    if head[0] == 90:
        pass
    else:
        head[0] = 270
#Left
def l():
    if head[0] == 0:
        pass
    else:
        head[0] = 180
#Right
def r():
    if head[0] == 180:
        pass
    else:
        head[0] = 0

def move():
    turtle.pensize(1)
    turtle.color("green")
    turtle.pu()
    sped = 2
    if a[0] % 5 == 0:
        sped = sped + 1
    turtle.speed(sped)
    turtle.setheading(head[0])
    turtle.shape("circle")
    turtle.stamp()
    turtle.fd(10)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:     
        turtle.clearstamps(1)
        pos.insert(0,[round(x),round(y)])
        pos.pop(-1)
    else:
        pos.insert(0,[round(x),round(y)])       
        b[0] += 1


def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("white")
    turtle.write("GAME OVER",align="center", font=("Arial",15,"bold"))
    turtle.goto(0,100)
    turtle.write("Your Score : " + str(a[0]),align="center",font=(10))
    turtle.goto(200,-200)
    turtle.write("Click to return",align="right",font=(0.0000001))
    turtle.onscreenclick(home)
    turtle.mainloop()
    
        


if __name__ == '__main__':
    home(0,0)
