a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))
if(a==b and b==c):
    print("This is an Equilateral triangle")
elif(a==b or b==c or a==c):
    print("This is an Isosceles triangle")
else:
    print("This is a Scalene triangle")