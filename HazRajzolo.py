import turtle

#Alapbeallitas
turtle.speed(0)
turtle.pensize(3)

#Negyzet
i=0
while i<4:
    turtle.forward(100)
    turtle.left(-90)

    i+=1

# háromszög
turtle.setheading(60)
turtle.forward(100)
turtle.setheading(-60)
turtle.forward(100)

turtle.done()