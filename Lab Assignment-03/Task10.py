a=float(input("Enter 1st num:"))
b=float(input("Enter 2nd num:"))
c=float(input("Enter 3rd num:"))
largest=a
smallest=a
if(b>largest):
    largest=b
if(c>largest):
    largest=c
if(smallest>b):
    smallest=b
if(smallest>c):
    smallest=c

print("Largest number:",largest)
print("Smallest number:", smallest)