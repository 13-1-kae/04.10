__author__ = 'student'
import turtle as trt
trt.speed(20)

def draw(l,n):
    if n==0:
        trt.forward(l)
        return
    draw(l/3,n-1)
    trt.left(60)
    draw(l / 3, n - 1)
    trt.right(120)
    draw(l / 3, n - 1)
    trt.left(60)
    draw(l / 3, n - 1)

def draw2(l, n):
    for i in range(3):
        draw(l, n)
        trt.right(120)

draw2(360, 4)
trt.done()
input()