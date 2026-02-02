class Polygon:
    def __init__(self, side):
        self.side = side

sides = int(input("Enter number of sides:"))
p = Polygon(sides)

if (sides==3):
    b=float(input("Enter base:"))
    h=float(input("Enter height:"))
    area = 0.5 * (b * h)
    print(f"The area of triangle is {area}.")

elif(sides==4):
    ch=int(input("Enter 1 for Square and 2 for Rectangle"))
    if(ch==1):
        s=float(input("Enter side:"))
        area = s * s
        print(f"The area of square is {area}.")
    elif(ch==2):
        l=float(input("Enter length:"))
        b=float(input("Enter breadth:"))
        area = l * b
        print(f"The area of rectangle is {area}.")

elif(sides==5):
    s=float(input("Enter side:"))
    a=1.72
    #a=apothem:distance from the center of a regular polygon to the middle of any side
    area = (5 * s * a)/2
    print(f"The area is {area}.")

elif(sides==6):
    s=float(input("Enter side:"))
    a=1.73
    area = (6 * s * a)/2
    print(f"The area is {area}.")

elif(sides==7):
    s=float(input("Enter side:"))
    a=2.08
    area = (7 * s * a)/2
    print(f"The area is {area}.")

elif(sides==8):
    s=float(input("Enter side:"))
    a=2.42
    area = (8 * s * a)/2
    print(f"The area is {area}.")

elif(sides==9):
    s=float(input("Enter side:"))
    a=2.75
    area = (9 * s * a)/2
    print(f"The area is {area}.")

elif(sides==10):
    s=float(input("Enter side:"))
    a=3.08
    area = (10 * s * a)/2
    print(f"The area is {area}.")

else:
    print(f"Enter valid number of sides!!!!")