print("1")

import random

def dice_roll():
    return random.randint(1, 6)

result = 0

while result != 6:
    result = dice_roll()
    print(result)

print("2")

def dice_roll2(sides):
    return random.randint(1, sides)

max_sides = int(input("Enter the number of sides on the dice: "))

result = 0

while result != max_sides:
    result = dice_roll2(max_sides)
    print(result)

print("3")

def gallon_convert(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons (negative value when done): "))

    if gallons < 0:
        break

    liters = gallon_convert(gallons)
    print(f"{gallons} gallons is {liters:.2f} liters")



print("4")

def sum_num(numbers3):
    total = 0
    for number in numbers3:
        total += number
    return total

Test = [99, 56, 21, 78, 9]

result = sum_num(Test)
print("The sum of the numbers is:", result)

print("5")

def rem_uneven(numbers4):
    even = []

    for number in numbers4:
        if number % 2 == 0:
            even.append(number)

    return even

OG = [7, 9, 12, 16, 28, 32, 34, 8, 19]

filter_num = rem_uneven(OG)

print("List without uneven numbers:", filter_num)

print("6")

def pizza_price(diameter_cm, price_euro):
    rad_pizza = (diameter_cm / 2) / 100
    area_pizza = 3.14159265359 * rad_pizza ** 2
    return price_euro/area_pizza


diameter1 = float(input("Enter the diameter of first pizza(cm): "))
price1 = float(input("Enter the price of first pizza(euros): "))

diameter2 = float(input("Enter the diameter of second pizza(cm): "))
price2 = float(input("Enter the price of second pizza(euros): "))

unit_per1 = pizza_price(diameter1, price1)
unit_per2 = pizza_price(diameter2, price2)

print(f"First pizza: {unit_per1:.2f} €/m²")
print(f"Second pizza: {unit_per2:.2f} €/m²")

if unit_per1 < unit_per2:
    print("First pizza is a better choice.")
elif unit_per2 < unit_per1:
    print("Second pizza is a better choice.")
else:
    print("It's about same.Choose either")
