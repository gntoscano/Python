#This simple code counts the number of vowels in any string

vowels = ['a', 'e', 'i', 'o', 'u'] 

string = str(input("Type any string: ")).lower()

count = countA = countE = countI = countO = countU = 0

for i in string:
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


print("\nThis string have:", count, "vowel(s)")
print("A:", countA)
print("E:", countE)
print("I:", countI)
print("O:", countO)
print("U:", countU, "\n")
