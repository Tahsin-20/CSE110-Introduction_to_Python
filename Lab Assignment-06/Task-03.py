str=input("Enter string: ")
split=input("Enter splitter: ")
result=""
for ch in str:
    if(ch!=split):
        result+=ch
    else:
        print(result)
        result=""
print(result)