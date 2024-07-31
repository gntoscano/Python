#This program check the price and the name of an item and returns: *Total price, *Number of itens that costs more than 1000, *The cheapest item

sum = count1000 = cont = cheap = 0
name_cheap = ''

while True:
    name = str(input("Write the name of the product: "))
    price = float(input("Write the pruce of the product: "))

    if price > 1000:
        count1000 += 1

    cont += 1
    sum += price

    if cont == 1 or price < cheap:
        cheap = price
        name_cheap = name

    print("-=" * 20)
    continue_yn = str(input("Do you want to continue? [Y]/[N]: ")).upper().strip()[0]
    if continue_yn == 'N':
        break


print(f"Total: ${sum:.2f}")
print(f"{count1000} product(s) cost(s) more than $1000")
print(f"The cheapest product was {name_cheap} and costs ${cheap:.2f}")

