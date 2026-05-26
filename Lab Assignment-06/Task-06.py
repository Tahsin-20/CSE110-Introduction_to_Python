s = input("Enter a string: ")

words = s.split()

result = ""

for i in range(len(words) - 1, -1, -1):
    result += words[i] + " "

print(result)