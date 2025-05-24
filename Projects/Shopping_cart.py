item = input("What Item would u like to purchase? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many items would u like to purchase? "))
total = price * quantity
print(f"you hav bought quantity {quantity} x {item}/s")
print(f"your total is: Rs.{total}")