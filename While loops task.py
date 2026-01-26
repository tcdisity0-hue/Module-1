print("1")

number = 1

while number < 1000:
    if number % 3 == 0:
        print(number)
    number += 1

print("2")
inches = float(input("Enter your inches: "))

while inches >= 0:
    centimeters = inches * 2.54
    print(centimeters, "centimeters")

    inches = float(input("Enter your inches: "))


print("That's a negative number")

print("3")

Base = int(input("Enter Number"))

Max = None
Min = None

while True:
    Base = input("Enter Number: ")

    if Base == "":
        break

    Base2 = int(Base)

    if Min is None or Base2 < Min:
        Min = Base2

    if Max is None or Base2 > Max:
        Max = Base2

    if Min is not None:
        print("Smallest number:", Min)
        print("Largest number:", Max)

    else:
        print("No numbers to work with.")

print("4")

import random

Answer = random.randint(1,10)

while True:
    guess = int(input("Guess a number "))
    if guess < Answer:
        print("Too low")
    elif guess > Answer:
        print("Too high")
    else:

        print("Correct")

    print("5")

    Correct_user = "python"
    Correct_password = "rules"

    Guesses = 0
    Max_Guesses = 5

    while Guesses < Max_Guesses:
        User = input("Enter your Username: ")
        Password = input("Enter your Password: ")

        if User == Correct_user and Password == Correct_password:
            print("Welcome ", Correct_user)
            break
        else:
            Guesses += 1
            print(f"Incorrect Username or Password. Left with {Max_Guesses - Guesses} attempts")

    else:
        print("Too many Incorrect Attempts")

    print("6")
    import random

    Points = int(input("Enter number of points: "))

    Num_Points = 0

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        Num_Points += 1

    Pi = 4 * Num_Points / Points

    print("The approximation of pi is ", Pi)


