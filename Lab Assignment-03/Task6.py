num=int(input("Enter a number:"))
if(num>0 and num%2==0):
    print("Number is postive and even")
elif(num>0 and num%2!=0):
    print("Number is positive and odd")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")