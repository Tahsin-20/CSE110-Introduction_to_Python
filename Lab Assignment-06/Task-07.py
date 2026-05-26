s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = ""

for ch in s1:
    if ch not in s2:
        result += ch

for ch in s2:
    if ch not in s1:
        result += ch

upper_result = ""

for ch in result:
    upper_result += chr(ord(ch) - 32)

print(upper_result)