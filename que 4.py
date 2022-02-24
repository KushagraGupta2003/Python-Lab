#WAP to find whether the number is even or odd using bitwise operator only?
A=int(input("enter the number: "))
N= A & 1
if(N==1):
    print("number is odd")
else:
    print("number is even")
