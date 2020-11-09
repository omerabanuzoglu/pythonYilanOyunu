# coding=utf-8
import turtle
import time
import random


hiz = 0.15
pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("black")
pencere.setup(width=600,height=600)
pencere.tracer(0)

bas = turtle.Turtle()
bas.speed(0)
bas.shape("square")
bas.color("red")
bas.penup()
bas.goto(0,100)
bas.direction = "stop"

hungry = turtle.Turtle()
hungry.speed(0)
hungry.shape("circle")
hungry.color("white")
hungry.penup()
hungry.goto(0,0)
hungry.shapesize(0.80, 0.80 )

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle()
yaz.write("Puanınız : {}".format(puan), align="center", font=("Courier",24,"normal"))

def move():
    if bas.direction == "up":
        y = bas.ycor()
        bas.sety(y + 20)
    if bas.direction == "down":
        y = bas.ycor()
        bas.sety(y - 20)
    if bas.direction == "right":
        x = bas.xcor()
        bas.setx(x + 20)
    if bas.direction == "left":
        x = bas.xcor()
        bas.setx(x - 20)


def goUp():
    if bas.direction != "down":
        bas.direction = "up"

def goDown():
    if bas.direction != "up":
        bas.direction = "down"

def goRight():
    if bas.direction != "left":
        bas.direction = "right"

def goLeft():
    if bas.direction != "right":
        bas.direction = "left"

pencere.listen()
pencere.onkey(goUp,"Up")
pencere.onkey(goDown,"Down")
pencere.onkey(goRight,"Right")
pencere.onkey(goLeft,"Left")



while True:
    pencere.update()

    if bas.xcor() > 300 or bas.xcor() < -300 or bas.ycor() > 300 or bas.ycor() < -300:
        time.sleep(1)
        bas.goto(0,0)
        bas.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)

        kuyruklar = []
        puan = 0
        yaz.clear()
        yaz.write("Puanınız : {}".format(puan), align="center", font=("Courier", 24, "normal"))
        hiz = 0.15


    if bas.distance(hungry) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        hungry.goto(x,y)

        puan = puan + 10
        yaz.clear()
        yaz.write("Puanınız : {}".format(puan), align="center", font=("Courier", 24, "normal"))

        hiz = hiz - 0.001

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("square")
        yeniKuyruk.color("gray")
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) -1, 0, -1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x,y)

    if len(kuyruklar) > 0:
        x = bas.xcor()
        y = bas.ycor()
        kuyruklar[0].goto(x,y)

    move()
    time.sleep(hiz)
