str=input("Enter a sentence: ")
result=""
bool=True

for ch in str:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        if bool==True:
            if(ch>='A' and ch<='Z'):
                result+=chr(ord(ch)+32)
            else:
                result+=ch

            bool=False

        else:
            if(ch>='a' and ch<='z'):
                result+=chr(ord(ch)-32)
            else:
                result+=ch
            bool=True
    else:
        result+=ch
print(result)