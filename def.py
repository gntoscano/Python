#REPEAT FUNCTIONS


# def happy_birthday(name, age):
#     print(f'Happy Birthday to {name}')
#     print(f'You are {age} years old')
#     print('Happy Birthday to you!')
#     print()

# happy_birthday('Gabriel', 17)
# happy_birthday('Gustavo', 16)
# happy_birthday('Fernando', 55)


#EXERCISE

# def display_invoice(username, amount, due_date):
#     print(f'Hello {username}!')
#     print(f'Your bill of ${amount} is due: {due_date}')

# display_invoice('Bro', 100.01, '01/04')






#RETURN

# def add(x, y):
#     w = x + y
#     return w

# def subtract(x, y):
#     w = x - y
#     return w

# def multiply(x, y):
#     w = x * y
#     return w

# def divide(x, y):
#     w = x / y
#     return w

# print(add(4, 2))
# print(subtract(4, 2))
# print(multiply(4, 2))
# print(divide(4, 2))






#EXERCISE 02

def create_name(first, last):
    first = first.capitalize() 
    last = last.capitalize() 
    return first + " " + last

full_name = create_name('spongebob', 'squarepants')

print(full_name)