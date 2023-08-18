from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rec):
        if rec.point1.x < self.x < rec.point2.x and rec.point1.y < self.y < rec.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x)*(self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 200), randint(0, 200)),
                         Point(randint(200, 400), randint(200, 400)))

# Print rectangle coordinates
print("Rectangle coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point from user
user_point = GuiPoint(float(input("Enter x: ")), float(input("Enter y: ")))

print("Point is in rectangle: ", user_point.falls_in_rectangle(rectangle))

if float(input("Guess area of rectangle: ")) == rectangle.area():
    print("Correct!")
else:
    print("Wrong! Rectangle area is: ", rectangle.area())

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_point.draw(myturtle)
turtle.done()
