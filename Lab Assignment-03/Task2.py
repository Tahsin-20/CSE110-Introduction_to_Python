marks=int(input("Enter your marks:"))
if(marks>=90 and marks<=100):
    print("Your grade is A")
elif(marks>=85 and marks<90):
    print("Your grade is A-")
elif(marks>=70 and marks<85):
    print("Your grade is B")
elif(marks>=57 and marks<70):
    print("Your grade is C")
elif(marks>=50 and marks<57):
    print("Your grade is D")
else:
    print("Your grade is F")