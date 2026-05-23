bill=int(input("Enter the amount the customer need to pay(Taka):"))
paid=int(input("Enter the amount, customer gave(Taka):"))
if(paid<bill):
    print("Please pay",(bill-paid),"taka more.")
else:
    change=paid-bill
    print("The returned amount is", change)

    if(change>0):
        hun=change//100
        change=change%100

        fift=change//50
        change=change%50

        twe=change//20
        change=change%20

        ten=change//10
        change=change%10

        fif=change//5
        change=change%5

        two=change//2
        change=change%2

        one=change

        print("100 taka note:", hun)
        print("50 taka note:", fift)
        print("20 taka note:", twe)
        print("10 taka note:", ten)
        print("5 taka coin:", fif)
        print("2 taka coin:", two)
        print("1 taka coin:", one)

