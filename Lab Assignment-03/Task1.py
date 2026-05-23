a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
c=int(input("Enter 3rd num:"))
largest=None
if(a>b and a>c):
    largest=a
elif(b>a and b>c):
    largest=b
else:
    largest=c

print("Largest number:",largest)