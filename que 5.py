"""WAP to input three number and sorted it....
eg....8 3 7
output:----8 7 3"""
X=int(input("enter the number 1: "))
Y=int(input("enter the number 2: "))
Z=int(input("enter the number 3: "))
d2=max(X,Y,Z)
d1=min(X,Y,Z)
M=(X+Y+Z)-d1-d2
print(d2,M,d1)
