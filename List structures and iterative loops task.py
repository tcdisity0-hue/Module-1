print("1")

import random

dice_roll = int(input("How many dice do you want to roll? "))

total = 0

for i in range(dice_roll):
    roll = random.randint(1, 6)
    total += roll

print("The sum of the dice is:", total)

print("2")

numbers = []

while True:
    user_num = input("Enter a number (Leave blank to finish): ")

    if user_num == "":
        break

    numbers.append(float(user_num))

numbers.sort(reverse=True)

print("The top five numbers are: ")
for number in numbers[:5]:
    print(number)

print("3")

prime_ask = int(input("Enter an number that you think is a prime number: "))

if prime_ask < 2:
    print(f"{prime_ask} is not a prime number")
else:
    for i in range(2, prime_ask):
        if prime_ask % i == 0:
            print(f"{prime_ask} is not a prime number")
            break
    else:
        print(f"You're correct {prime_ask} is a prime number")

print("4")

cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("The cities you entered are: ")
for city in cities:
    print(city)
