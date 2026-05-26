str=input("Enter a string: ")
result=""
for i in str:
    if(i>='a' and i<='z'):
        result+=chr(ord(i)-32)
    else:
        result+=i
print(result)