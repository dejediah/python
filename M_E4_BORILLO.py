# no param, no return
def triangle():
    print("Area of Triangle")
    trib = int(input("Base: "))
    trih = int(input("Height: "))
    triarea = float((1 / 2) * trib * trih)
    print("The area of the triangle is: " + str(triarea))
    print()


# param, no return
def rectangle(recw, rech):
    recarea = float((recw * rech))
    print("The area of the rectangle is: " + str(recarea))


# param, return
def square(a):
    squarea = a ** 2
    return squarea


# default, return
def circle(r=5.0, pi=3.1416):
    print("Area of Circle")
    cirarea = float(pi * (r ** 2))
    return cirarea

#tri
triangle()

#rec
print("Area of Rectangle")
recw = int(input("Width: "))
rech = int(input("Height: "))
rectangle(recw, rech)
print()

#squ
print("Area of Square:")
a = int(input("Length of Side: "))
square(a)
print(f"The area of the square is: {square(a)}")
print()

#cir
cirarea = circle()
print(f"The area of the circle is: {str(cirarea)}")
