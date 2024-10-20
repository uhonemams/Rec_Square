import turtle as t

#drawing the rectangle
def rectangle(length,height):
    t.pensize(6)
    t.pencolor("blue")
    t.forward(length)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(height)
    
  
#drawing the square 
def square(side):
    for i in range(4):
        t.pensize(2)
        t.pencolor("orange")
        t.backward(side)
        t.left(90)
        


#prompting the dimensions of the rectangle
length = float(input("Enter the length of the rectangle: "))
height = float(input("The breadth of the rectangle: "))

print("")
print("Hint:   Enter 0 to get the default number of squares that fit in the rectangle or \n\tenter any custom number as long as it is not bigger than one of your recangle's dimensions")
print("")
#prompting the dimensions of the square
sqr_side = float(input("Enter the side of the square: "))


if(sqr_side == 0): # if the user wants to know the default squares that fit in the rectangle
        if(length < height):
            sqr_side = length
        elif(length > height):
            sqr_side = height

# Create two additional turtles for text and labels
label = t.Turtle()
gName = t.Turtle()
number = t.Turtle()

number.pencolor("orange")

gName.font = ("Arial", 72,"Bold")
gName.pencolor("Orange")
gName.pensize(10)

# Write the project name on the turtle graphics window
gName.up()
gName.goto(-500, 290)
gName.down()
gName.write("JBS- Project 17", font=("Arial", 25))
label.font = ("Arial", 16)
label.pencolor("orange")

# Write rectangle dimensions on the turtle graphics window
label.up()
label.goto(-500,200)
label.down()
label.write("Given rectangle dimensions : " + "LENGTH = " + str(int(length)) + "\tBREADTH = " + str(int(height)), font=("Arial", 16))

label.up()
label.goto(-500, 150)
label.down()
label.write("Given square dimensions : " + "Side = " + str(int(sqr_side)), font=("Arial", 16))

# Write the number of squares that fit in the rectangle
label.up()
label.goto(-500,100)
label.down()



if(sqr_side > height):
    
    print("The square won't fit because it is bigger than the rectangle")
    label.write("The square won't fit because it is bigger than the rectangle", font=("Arial", 16))
    
elif(length == height):
    
    print("The dimensions entered are those of a square since both length and breadth are equal")
    
else:
        
    hori_shift = length/sqr_side #calculates the number of squares to fit horizontally
    verti_shift = height/sqr_side #calculates the number of squares to fit vertically

    num_sqaure = int(hori_shift) * int(verti_shift) #calculates the total number of squares to fit in the rectangle
    
    print("")
    print("Number of sqaures = ", num_sqaure)
    
    label.write("The number of squares that would fit in the given rectangle dimensions = " + str(int(num_sqaure)), font=("Arial", 16))
    
    #drawing everything
    rectangle(length,height)
    incri = 0
    num = 1
    for j in range(int(verti_shift)):
        x_axis = int(sqr_side)
        y_axis = int(sqr_side)
        if j == 0:
            for i in range(int(hori_shift)):
                t.goto(x_axis * i,(y_axis) * j)
                square(sqr_side)
                number.up()
                number.goto((x_axis * i) + x_axis/4, y_axis * -1)
                number.down()
                if(sqr_side > 30):
                    number.write(str(num), font=("Arial",16))
                else:
                    number.write(str(num), font=("Arial",9))
                num += 1
        elif j > 0:
            t.goto(0,(incri * -1))
            for i in range(int(hori_shift)):
                t.goto(x_axis * i,(y_axis * -1) * j)
                square(sqr_side)
                number.up()
                number.goto((x_axis * i) + x_axis/4,(y_axis) * ((j + 1)*-1))
                number.down()
                if(sqr_side > 30):
                    number.write(str(num), font=("Arial",16))
                else:
                    number.write(str(num), font=("Arial",9))
                num += 1
            incri += sqr_side
            
            
number.hideturtle() 
gName.hideturtle()
label.hideturtle()
t.hideturtle()
t.exitonclick()
