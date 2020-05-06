def fangxing(a,n,ps,pc):
    import turtle
    turtle.pensize(ps)
    turtle.pencolor(pc)
    for i in range(n-1):
        b = 1
        le = a + b * (i * 10)
        turtle.fd(le)
        turtle.left(90)
        turtle.fd(le)
        turtle.left(90)

fangxing(20,50,5,"red")
done()
