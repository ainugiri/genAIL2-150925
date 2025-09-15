def carPrice(age):
    if age == 1:
        return 20000
    elif age == 2:
        return 19000
    elif age == 3:
        return 18000
    elif age == 4:
        return 17000
    elif age == 5:
        return 16000
    elif age == 6:
        return 15000
    elif age == 7:
        return 14000
    elif age == 8:
        return 13000
    elif age == 9:
        return 12000
    elif age == 10:
        return 11000
    else:
        return 10000

age = int(input("Enter the age of the car (in years): ").strip())
print("The estimated price of the car is:", carPrice(age))

