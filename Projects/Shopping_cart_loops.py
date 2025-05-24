# Python program for ,anaging shopping cart
foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("What food do you want to buy? (press 'q' to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"What is the price of {food}? $"))
        prices.append(price)
        quantity = int(input(f"How many {food}(s) do you want to buy? "))
        quantities.append(quantity)

print(" ------ SHOPPING CART ------ \n")
for i,j in zip(foods,quantities):
    print(f"{i} : {j}")
for i,j in zip(prices, quantities):
    total += i*j
print(f"\nBill: ${total}")