import turtle

turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.bgcolor('black')
turtle.speed(2) 

#base
turtle.color('red', 'red')
turtle.circle(10,180)
turtle.circle(25,110)
turtle.left(50)
turtle.circle(60,45)
turtle.circle(20,170)
turtle.right(24)
turtle.forward(30)

turtle.left(10)
turtle.circle(30,110)
turtle.forward(20)
turtle.left(40)

turtle.circle(90,70)
turtle.circle(30,150)
turtle.right(30)
turtle.forward(15)
turtle.circle(80,90)
turtle.left(15)
turtle.forward(20)
turtle.left(3)
turtle.circle(150,80)
turtle.left(50)
turtle.circle(150,90)


turtle.left(150)
turtle.circle(-90,70)
turtle.left(20)
turtle.circle(75,105)
turtle.setheading(60)
turtle.circle(80,98)
turtle.circle(-90,40)
turtle.left(180)
turtle.circle(90,40)
turtle.circle(-80,98)
turtle.setheading(-83)

#hoja1
turtle.forward(30)
turtle.left(90)
turtle.forward(25)
turtle.left(45)
turtle.color('green')
turtle.circle(-80,90)
turtle.right(90)
turtle.circle(-80,90)
turtle.end_fill()
turtle.right(135)
turtle.forward(60)
turtle.left(180)
turtle.forward(85)
turtle.left(90)
turtle.forward(80)


#hoja2
turtle.right(90)
turtle.right(45)
turtle.color('green')
turtle.circle(80,90)
turtle.left(90)
turtle.circle(80,90)
turtle.end_fill()
turtle.left(135)
turtle.forward(60)
turtle.left(180)
turtle.forward(60)
turtle.right(90)
turtle.circle(200,60)

#corazon
turtle.fillcolor('red')
turtle.begin_fill()



# Mensaje
turtle.hideturtle()
turtle.penup()
turtle.goto(-360,-230)
turtle.pendown()
turtle.color('white')
turtle.write("Mi Princesa", align='left', font=('Times New Roman', 15, 'normal'))
turtle.goto(-360,-250)
turtle.write("Prometo amarte mas que ayer, pero no tanto como mañana <3", align='left', font=('Times New Roman', 15, 'normal'))
turtle.goto(-360,-270)
turtle.write("Misael", align='left', font=('Times New Roman', 12, 'normal'))

turtle.done()