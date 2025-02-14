print("""choose the polygon based on your need
1 - Square
2 - Rectangle
3 - circle
4 - triangle""")
choice = int(input("choose the shape"))

if (choice == 1):
    a = int(input ("enter the side"))
    area1 = a*a
    print("area :", area1)

if (choice == 2):
    l = int(input ("enter the length"))
    b = int(input("enter the breadth"))
    area2 = l*b
    print("area :", area2)

if (choice == 3):
    r = int(input ("enter the radius"))
    area3 = 3.14*r*r
    print("area :", area3)

if (choice == 4):
    b1 = int(input ("enter the base"))
    h = int(input("enter the height"))
    area4 = 0.5*b1*h
    print("area :", area4)