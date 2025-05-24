
menu = {
    "Pizza": 250,
    "Burger": 200,
    "Fries": 100,
    "Popcorn": 300,
    "Coffee": 100,
    "Tea": 50,
    "Soda": 150,
    "Nachos": 200,
}
order = []
price = 0
print("-------MENU-------")
for food, price in menu.items():
    print(f"{food:10} : Rs.{price:2f}")
print("------------------")

while True:
    food = input("What would you like to order?(q to quit): ").capitalize()
    if food == "Q":
        break
    elif(food in menu.keys()):
        order.append(food)
        price += menu[food]

print("\nYOUR ORDER IS:\n", order)
print(f"Total: Rs.{price:2f}")