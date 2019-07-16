from turtle import * 
shape("turtle")
left(90)
forward(10)
right(90)
for i in range(20):
    speed(100)
    forward(20*i)
    left(90)
    forward(20*i)
    left(90)
mainloop()