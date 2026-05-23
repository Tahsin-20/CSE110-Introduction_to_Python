a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a==b and b==c):
    print("All numbers are equal")
elif(a==b or b==c or a==c):
    print("Neither all are equal or different")
else:
    print("All numbers are different")