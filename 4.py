__author__ = 'student'
import turtle as trt
trt.speed(150)
def draw(l, n):
    if n==0:
        trt.forward(l)
        return
    draw(l/4, n-1)
    trt.left(90)
    draw(l/4, n-1)
    trt.right(90)
    draw(l/4, n-1)
    trt.right(90)
    draw(l/4, n-1)
    draw(l/4, n-1)
    trt.left(90)
    draw(l/4, n-1)
    trt.left(90)
    draw(l/4, n-1)
    trt.right(90)
    draw(l/4, n-1)
trt.penup()
trt.left(180)
trt.forward(400)
trt.left(180)
trt.pendown()
draw (120000,8)
input()
