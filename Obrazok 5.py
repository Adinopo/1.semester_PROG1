
import turtle

i = 0
for i in range(5):
    if (i==0):
        turtle.fd(50)
        var3=turtle.position()
        turtle.left(90)
        turtle.fd(50)
        var2=turtle.position()
        turtle.home()
        var1=turtle.distance(var2)
        turtle.setheading(turtle.towards(var2))
        turtle.fd(var1)
        turtle.left(90)
        i=+1
    else:
        turtle.fd(50)
        var2=turtle.position()
        turtle.home()
        var1=turtle.distance(var2)
        turtle.setheading(turtle.towards(var2))
        turtle.fd(var1)
        turtle.left(90)
    
turtle.fd(50)    
    
#print(turtle.towards(var2))
#print(var1)


        #    turtle.setheading(
              
    #    var1=turtle.position()
    #    turtle.home()
      #  var2=turtle.distance(int(var1))
