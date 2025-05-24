# this program converts temperature in celcius to farenheit and Vice versa
flag = 1
while(flag == 1):
    Temp = float(input("Enter the Temperature: "))
    unit = input("Enter 'C' for temperature entered in Celcius and 'F' for temperature entered in Farenheit: ")

    if( unit == "C" ):
        Temp = ((9/5) * Temp) + 32
        print(f"The Temperature in Farenheit is {Temp} F")
    elif( unit == "F" ):
        Temp = (Temp - 32) * (5/9)
        print(f"The Temperature in Celcius is {Temp} C")
    else:
        print(f"{unit} is not a valid unit")
    flag = int(input("Enter '1' to continue or '0' to exit : "))