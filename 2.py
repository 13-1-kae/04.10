import turtle as trt
trt.speed(15)

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
draw(360,5)
trt.done()
input()