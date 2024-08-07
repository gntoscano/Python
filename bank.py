#Create a program that simulates the operation of an ATM. At the beginning, ask the user for the amount to be withdrawn (integer), and the program will inform how many bills of each value will be dispensed.
#Note: consider that the ATM has bills of $50, $20, $10, and $1.

print('=' * 30)
print('{:^30}'.format('WELCOME TO ATM'))
print('=' * 30)

value = int(input("Enter the amount to be withdrawn: "))
total = value
cash = 50
bills = 0

while True:
    if total >= cash:
        total -= cash
        bills += 1
    else:
        if bills > 0:
            print(f"{bills} of ${cash}")
        if cash == 50:
            cash = 20
        elif cash == 20:
            cash = 10
        elif cash == 10:
            cash = 1
        bills = 0

        if total == 0:
            break


