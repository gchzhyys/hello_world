def fangxing(a,n):
    import turtle
    for i in range(n-1):
        b = 1
        le = a + b * (i * 10)
        turtle.fd(le)
        turtle.left(90)
        turtle.fd(le)
        turtle.left(90)

fangxing(20,50)
done()
