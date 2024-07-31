#This code gets a string as a input and use the 'reversed' function to revert the string
#Example: people - elpoep

phrase = str(input("Write a phrase: "))

reversed_string = ''.join(reversed(phrase))

print(f"The reversed phrase is: '{reversed_string}'")


