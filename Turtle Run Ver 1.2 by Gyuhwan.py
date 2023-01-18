import turtle as t
import random

score = 0
playing = False
star_x = random.randint(-330, 330)
star_y = random.randint(-330, 330)


def right():
    t.setheading(0)
    
    
def up():
    t.setheading(90)
    
    
def left():
    t.setheading(180)
    
    
def down():
    t.setheading(270)


def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()
    
def play():
    global score
    global playing
    t.forward(10)
    
    if random.randint(1, 10) == 1:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = (score/5) + 5

    if random.randint(1, 10) == 1:
        ang = te2.towards(t.pos())
        te2.setheading(ang)
    speed = (score/5) + 5

    if random.randint(1, 10) == 1:
        ang = te3.towards(t.pos())
        te3.setheading(ang)
    speed = (score/5) + 5

    if random.randint(1, 10) == 1:
        ang = te4.towards(t.pos())
        te4.setheading(ang)
    speed = (score/5) + 5

    if speed > 11:
        speed = 11
    te.forward(speed)
    te2.forward(speed)
    te3.forward(speed)
    te4.forward(speed)
    
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over!", text)
        playing = False
        score = 0
    if t.distance(te2) < 12:
        text = "Score : " + str(score)
        message("Game Over!", text)
        playing = False
        score = 0
    if t.distance(te3) < 12:
        text = "Score : " + str(score)
        message("Game Over!", text)
        playing = False
        score = 0
    if t.distance(te4) < 12:
        text = "Score : " + str(score)
        message("Game Over!", text)
        playing = False
        score = 0

    if t.distance(ts) < 15:
        score += 1
        score = str(score)
        t.write(score + "점!")
        score = int(score)
        star_x = random.randint(-330, 330)
        star_y = random.randint(-330, 330)
        ts.goto(star_x, star_y)
        
    if t.distance(ty) < 15:
        score += 3
        score = str(score)
        t.write(score + "점!")
        score = int(score)
        star_x = random.randint(-330, 330)
        star_y = random.randint(-330, 330)
        ty.goto(star_x, star_y)
        
    if t.distance(ti) < 15:
        score += 2
        score = str(score)
        t.write(score + "점!")
        score = int(score)
        star_x = random.randint(-330, 330)
        star_y = random.randint(-330, 330)
        ti.goto(star_x, star_y)
        
    if playing:
        t.ontimer(play, 50)

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 20))
    t.home()

t.title("터틀런")     
    
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(-200, 250)

te2 = t.Turtle()
te2.shape("turtle")
te2.color("pink")
te2.speed(0)
te2.up()
te2.goto(200, 250)

te3 = t.Turtle()
te3.shape("turtle")
te3.color("purple")
te3.speed(0)
te3.up()
te3.goto(-200, -250)

te4 = t.Turtle()
te4.shape("turtle")
te4.color("brown")
te4.speed(0)
te4.up()
te4.goto(200, -250)

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -250)

ty = t.Turtle()
ty.shape("circle")
ty.color("yellow")
ty.speed(0)
ty.up()
syar_x = random.randint(-330, 330)
syar_y = random.randint(-330, 330)
ty.goto(star_x, star_y)

ti = t.Turtle()
ti.shape("circle")
ti.color("blue")
ti.speed(0)
ti.up()
star_x = random.randint(-330, 330)
star_y = random.randint(-330, 330)
ti.goto(star_x, star_y)
        
t.setup(700, 700)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(right, "Right")
t.onkeypress(up, "Up")
t.onkeypress(left, "Left")
t.onkeypress(down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")

