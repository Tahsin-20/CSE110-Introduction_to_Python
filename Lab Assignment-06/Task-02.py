str=input("Enter a string: ")
i=0
j=len(str)-1
isPalindrome=True
while i<j:
    if(str[i]!=str[j]):
        isPalindrome=False
        break
    i+=1
    j-=1
print(isPalindrome)