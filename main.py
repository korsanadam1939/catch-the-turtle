import turtle
import time
import tkinter
import random

ekran=turtle.Screen()
ok=turtle.Turtle()
yazı=turtle.Turtle()
yazı2=turtle.Turtle()
sure=turtle.Turtle()
sure.ht()
ekran.bgcolor("light blue")
ok.color("green")
ok.shape("turtle")
ekran.setup(800,740)
def ekranı_temizle():
    ok.clear()
ok.turtlesize(2)#kamlumbağanın boyutunu 2 katına çıkarır
puan=0
print(ekran.window_height())
print(ekran.window_width())
fare_konumx="yok"
fare_konumy="yok"
def fare_tiklandiginda(x,y):
    global fare_konumx
    global fare_konumy
    fare_konumx=x
    fare_konumy=y
yazı.penup()
yazı.ht()
yazı2.ht()
zaman=0
yazı2.penup()
while zaman <= 20:

    yazı.goto(8.0,330.0)
    yazı.write(f"Score= {puan}",font=("Arial", 24, "bold"),align="center",)
    yazı2.goto(1.0,300.0)
    yazı2.write(f"Time= {zaman}",font=("Arial", 24, "bold"),align="center",)




    ok.penup()
    ok.ht()#oku gizler
    ok.goto(random.randint(-250,250), random.randint(-300, 300))
    ok.st()#oku görünür yapar
    ok.pendown()

    ekran.onclick(fare_tiklandiginda)
    time.sleep(1)

    kamlumbagax=ok.xcor()
    kamlumbagay=ok.ycor()
    sayilarx=list(range(kamlumbagax-400,kamlumbagax+400))
    sayilary=list(range(kamlumbagay-400,kamlumbagay+400))
    xdurum=False
    ydurum=False
    for x in sayilarx:
        if x==fare_konumx:
            xdurum=True
    for y in sayilary:
        if y==fare_konumy:
            ydurum=True
    if xdurum and ydurum:
        puan=puan+1
        
    print(puan)
    print(fare_konumx,fare_konumy)

    fare_konumx = "yok"
    fare_konumy = "yok"
    yazı.clear()
    yazı.ht()
    zaman=zaman+1
    yazı2.clear()
ok.ht()
turtle.mainloop()
