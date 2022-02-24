#WAP to input two coordinates and find distance between two coordinates?
import math
print("enter first coordinate:\n")
x1=int(input("enter the coordinates of x: "))
y1=int(input("enter the coordinates of y: "))
x2=int(input("enter the coordinates of x: "))
y2=int(input("enter the coordinates of y: "))
D=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
print("The distance between two coordinates %0.1f"%D)
