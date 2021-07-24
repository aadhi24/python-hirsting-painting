import turtle as t
import random

colour_list = [(245, 238, 243), (247, 244, 242), (240, 241, 245), (202, 109, 164), (238, 245, 240), (150, 49, 75),
               (223, 135, 201), (52, 124, 93), (172, 40, 154), (140, 19, 30), (133, 185, 163), (198, 71, 91),
               (46, 86, 122), (72, 35, 43), (145, 148, 178), (13, 71, 99), (233, 164, 175), (161, 158, 142),
               (105, 77, 74), (55, 50, 46), (183, 171, 205), (36, 74, 60), (18, 90, 86), (81, 129, 148), (148, 20, 17),
               (14, 64, 70), (30, 100, 68), (107, 153, 127), (174, 97, 94), (176, 209, 192)]
timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
timmy.shape("arrow")
timmy.shapesize(0.5)
timmy.penup()
timmy.speed("fastest")
def hirst():
    count = -250
    for _ in range(10):
        timmy.setpos(-250, count)
        count += 50
        for i in range(10):
            ram = random.choice(colour_list)
            timmy.color(ram)
            timmy.dot(20)
            timmy.fd(50)
    timmy.color("white")

hirst()


screen.exitonclick()
