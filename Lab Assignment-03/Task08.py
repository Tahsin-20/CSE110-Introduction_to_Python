id=int(input("Enter student ID:"))
digits=id//100000
year=digits//10
session=digits%10
if(session==1):
    print("Student Joined BRAC in Spring", year)
elif(session==2):
    print("Student Joined BRAC in Fall", year)
else:
    print("Student Joined BRAC in Summer", year)
