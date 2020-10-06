import turtle

turtle.speed(30)
turtle.bgcolor("orange")
turtle.title("Vitaj v mojom prvom programe srdiečko!")

print("Program running...")


def meno():
    turtle.forward(150)

def nemo():
    turtle.bye()
    

##var_1 = turtle.textinput("Prompt", "Enter integer number > 0 :")
#            Priklad 1
turtle.penup()
turtle.setposition(-300,0)
turtle.pendown()
for i in range(4):
        for j in range(5):
            turtle.fd(50)
            turtle.left(90)
            turtle.fd(50)
            turtle.right(90)
        turtle.fd(50)
        turtle.right(90)

turtle.clear()
        
#            Priklad 2
for i in range(4):
    for j in range(1):
        turtle.fd(150)
        turtle.left(90)
        turtle.fd(150)
    turtle.right(90)
    turtle.fd(150)
    turtle.right(90)
              
turtle.clear()
        
#            Priklad 3
for j in range(10):
    for i in range(5):
        turtle.fd(80)
        turtle.left(360/5)
    turtle.left(360/10)

turtle.clear()

#           Priklad 4
for j in range(12):
    for i in range(12):
        turtle.fd(80)
        turtle.left(360/12)
    turtle.left(360/12)

turtle.clear()

#           Priklad 5
turtle.home()
var=0
for i in range(5):
    for j in range(3):
        if (var==0):
            turtle.fd(50)
            var3=turtle.position()
            turtle.left(90)
            turtle.fd(50)
            var=+1
        else:
            turtle.setheading(
              
        var1=turtle.position()
        turtle.home()
        var2=turtle.distance(int(var1))
        


turtle.onkeypress(nemo, "q")

turtle.onkeypress(meno, "Up")

turtle.onscreenclick(turtle.goto)

turtle.listen()

       

