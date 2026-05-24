payment=int(input("Enter payment:"))
age=int(input("Enter age:"))
if(payment<10000 or age<18):
    print("Your tax amounts in 0 Tk")
elif(payment>=10000 and payment<=20000):
    amount=(int)((5/100)*payment)
    print("Your tax amounts in", amount, "Tk")
else:
    amount=(int)((10/100)*payment)
    print("Your tax amounts in", amount, "Tk")