# COMP 115 - Project 1: Artistic Drawing Using Turtle
# Theme: Fencing Final (two epee fencers on a piste)

import turtle

# ---------- Set up the screen and the turtle ----------
screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("lightskyblue")   # this is the wall of the arena
screen.title("Fencing Final")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# ---------- Small helper functions (used by the bigger functions) ----------

def go_to(x, y):
    # move the turtle without drawing, then put the pen down
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_line(x1, y1, x2, y2, color, size):
    # draw one straight line from (x1, y1) to (x2, y2)
    go_to(x1, y1)
    t.pencolor(color)
    t.pensize(size)
    t.goto(x2, y2)


def draw_rectangle(x, y, width, height, color):
    # (x, y) is the bottom left corner
    go_to(x, y)
    t.color(color)
    t.pensize(1)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_circle(x, y, radius, color):
    # (x, y) is the center of the circle
    go_to(x, y - radius)   # turtle circles start at the bottom
    t.color(color)
    t.pensize(1)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def write_text(x, y, words, size, color):
    go_to(x, y)
    t.pencolor(color)
    t.write(words, align="center", font=("Arial", size, "bold"))


# ---------- Main drawing functions ----------

def draw_background():
    # the floor of the arena
    draw_rectangle(-450, -300, 900, 200, "tan")


def draw_lights():
    # four overhead lights hanging from the ceiling
    for x in range(-300, 301, 200):
        draw_line(x, 300, x, 270, "black", 2)
        draw_rectangle(x - 30, 255, 60, 15, "yellow")


def draw_title():
    write_text(0, 195, "Fencing Final", 28, "navy")


def draw_piste():
    # the long fencing strip
    draw_rectangle(-350, -230, 700, 30, "dimgray")
    # white marking lines across the strip
    for x in range(-300, 301, 100):
        draw_line(x, -230, x, -200, "white", 3)
    write_text(0, -265, "Piste", 14, "black")


def draw_scoreboard():
    # black box
    draw_rectangle(-110, 20, 220, 120, "black")
    # hit lights on each side (red = left fencer, green = right fencer)
    draw_circle(-150, 80, 18, "red")
    draw_circle(150, 80, 18, "green")
    # text on the scoreboard
    write_text(0, 110, "EPEE", 14, "white")
    write_text(0, 62, "14 - 14", 32, "yellow")
    write_text(0, 30, "0:12", 18, "red")


def draw_flag(x, y):
    # small Indian flag, (x, y) is the bottom of the pole
    draw_line(x, y, x, y + 100, "saddlebrown", 4)
    draw_rectangle(x, y + 85, 60, 15, "orange")   # top stripe
    draw_rectangle(x, y + 70, 60, 15, "white")    # middle stripe
    draw_rectangle(x, y + 55, 60, 15, "green")    # bottom stripe
    # the blue wheel in the middle
    go_to(x + 30, y + 71.5)
    t.pencolor("navy")
    t.pensize(1)
    t.circle(6)


def draw_fencer(x, y, direction, shirt_color, stance, sword_length):
    # (x, y) is where the fencer stands (between the feet)
    # direction: 1 = facing right, -1 = facing left
    # stance: how far apart the feet are
    # sword_length: how long the epee is

    # two legs
    draw_line(x, y + 70, x + direction * stance, y, "white", 6)
    draw_line(x, y + 70, x - direction * stance, y, "white", 6)

    # shoes
    go_to(x + direction * stance, y)
    t.dot(10, "black")
    go_to(x - direction * stance, y)
    t.dot(10, "black")

    # body
    draw_line(x, y + 70, x, y + 128, shirt_color, 12)

    # weapon arm and epee
    hand_x = x + direction * 45
    hand_y = y + 105
    draw_line(x, y + 120, hand_x, hand_y, shirt_color, 6)
    draw_line(hand_x, hand_y, hand_x + direction * sword_length, hand_y + 8, "gray", 3)
    go_to(hand_x, hand_y)
    t.dot(10, "black")   # the handle/guard

    # head with a mask
    draw_circle(x, y + 150, 18, "lightgray")
    for i in range(3):
        line_y = y + 142 + i * 8
        draw_line(x - 14, line_y, x + 14, line_y, "black", 1)


# ---------- Main program ----------

draw_background()
draw_lights()
draw_title()
draw_piste()
draw_scoreboard()
draw_flag(340, -110)

# left fencer and right fencer (slightly different from each other)
draw_fencer(-130, -200, 1, "red", 35, 95)
draw_fencer(130, -200, -1, "green", 25, 85)

turtle.done()
