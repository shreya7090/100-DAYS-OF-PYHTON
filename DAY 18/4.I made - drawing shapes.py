from turtle import Turtle,Screen

tem = Turtle()
for _ in range(4):
    tem.forward(100)
    tem.color("red")
    tem.right(120)
    
tem.left(30)

for _ in range(4):
    tem.color("blue")
    tem.forward(100)
    tem.right(90)

tem.left(18)

for _ in range(5):
    tem.color("orange")
    tem.forward(100)
    tem.right(72)

tem.left(12)

for _ in range(6):
    tem.color("green")
    tem.forward(100)
    tem.right(60)

tem.left(8.57142857142857)

for _ in range(7):
    tem.color("yellow")
    tem.forward(100)
    tem.right(51.42857142857143)

tem.left(6.42857142857143)

for _ in range(8):
    tem.color("black")
    tem.forward(100)
    tem.right(45)

tem.left(5)

for _ in range(9):
    tem.color("pink")
    tem.forward(100)
    tem.right(40)

tem.left(4)

for _ in range(10):
    tem.color("brown")
    tem.forward(100)
    tem.right(36)

screen = Screen()
screen.exitonclick()

