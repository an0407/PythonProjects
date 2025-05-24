# Compound Interest Calculator Program

(Principle,rate,time) = (0,0,0)

while Principle <= 0:
    Principle = float(input("Enter the Principle amount: "))
    if(Principle <= 0):
        print("Principle amount cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the Interest Rate: "))
    if(rate <= 0):
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time period: "))
    if(Principle <= 0):
        print("Time period cannot be less than or equal to zero")

print(f"Principle amount is ${Principle}")
print(f"Interest rate is {rate}")
print(f"Time period is {time} years\n")
amount = Principle * pow((1 + (rate/100)), time)
print(f"The amount after {time} years is ${amount}")