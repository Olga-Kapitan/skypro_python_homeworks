from turtle import *

my_turtle = Turtle()
my_turtle.speed(1)
my_turtle.screen.setup(1200, 800)

my_turtle.circle(100)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()