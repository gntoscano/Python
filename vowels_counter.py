#This simple code counts the number of vowels in any string

vowels = ['a', 'e', 'i', 'o', 'u'] 

string = str(input("Type any string: ")).strip().lower()
words = string.split()
together = ''.join(words)

count = countA = countE = countI = countO = countU = countCon = 0

for i in together:
    if i in vowels:
        count += 1
        if i == 'a':
            countA += 1
        if i == 'e':
            countE += 1
        if i == 'i':
            countI += 1
        if i == 'o':
            countO += 1
        if i == 'u':
            countU += 1
    else: 
        countCon+= 1


print("\nThis string have:", count, "vowel(s)")
print("\nThis string have:", countCon, "consonant(s)")
print("A:", countA)
print("E:", countE)
print("I:", countI)
print("O:", countO)
print("U:", countU, "\n")
