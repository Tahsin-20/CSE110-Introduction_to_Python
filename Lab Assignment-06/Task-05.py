str=input("Enter a line: ")
vowel=0
conso=0
for ch in str:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=="I" or ch=='O' or ch=='U'):
            vowel+=1
        else:
            conso+=1
if(vowel>0 and conso>0):
    if(vowel%3==0 and conso%5==0):
        print("Aaarr!Me Plunder!!")
    else:
        print("Blimey!No Plunder!!")
else:
    print("Blimey!No Plunder!!")

