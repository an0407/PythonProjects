# this program converts Weight in Kilograms to LBs and Vice versa
flag = 1
while(flag == 1):
    weight = float(input("Enter your weight: "))
    unit = input("Enter 'K' for weight entered in KGs and 'L' for weight entered in LBs: ")

    if( unit == "K" ):
        weight = weight * 2.02
        unit = ".Kgs"
        print(f"The Weight in LB(s) is {weight} {unit}")
    elif( unit == "L" ):
        weight = weight / 2.02
        unit = ".Lbs"
        print(f"The Weight in KG(s) is {weight} {unit}")
    else:
        print(f"{unit} is not a valid unit")
    flag = int(input("Enter '1' to continue or '0' to exit : "))