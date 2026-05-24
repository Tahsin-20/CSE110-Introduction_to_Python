num=int(input("Enter a number:"))
if(num<0):
    print(2*num)
elif(num>=0 and num<2):
    print(num+1)
elif(num>=2 and num<5):
    print((num**2)-1)
else:
    print(3*(num**2)+2)