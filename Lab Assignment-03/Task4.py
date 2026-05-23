num=int(input("Enter a number:"))
if(num%5==0 and num%7==0):
    print("Divisible by Both")
elif(num%5==0):
    print("Invalid: Divisible by 5 only")
elif(num%7==0):
    print("Invalid: Divisible by 7 only")
else:
    print("NO")