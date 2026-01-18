print('1')

name = input('Enter your name: ')
print(('Hello there ' + name))

print('2')

rad = int(input('Enter your radius: '))
Pi = 3.14159265359
AreaC = int(Pi) * int(rad**2)

(print('Area of circle is ' + str(AreaC)))

print('3')

length = int(input('Enter your length: '))
width = int(input('Enter your width: '))
Area = length * width
Perimeter = length + length + width + width

(print('The Area of the rectangle is ' + str(Area)))

(print('The perimeter of the rectangle is ' + str(Perimeter)))

(print('4'))

Num1 = int(input('Enter your number: '))
Num2 = int(input('Enter your number: '))
Num3 = int(input('Enter your number: '))

Sum = Num1 + Num2 + Num3
Product = Num1 * Num2 * Num3
Average = Sum / 3

(print('The sum of the numbers is ' + str(Sum)))
(print('The product is ' + str(Product)))
(print('The average of the numbers is ' + str(Average)))

(print('5'))

Talent = int(input('Enter Talents: '))
Pounds = int(input('Enter Pounds: '))
Lots = int(input('Enter Lots: '))

T = Talent * 20 * 32
P = Pounds * 32
Total = Lots + T + P
Grams = Total * 13.3

Kilograms = Grams // 1000
Rgrams = Grams % 1000

print(f'{int(Kilograms)} kilograms and {int(Rgrams)} grams ')

(print('6'))

import random

Rand = random.randint(0,9)
Rand2 = random.randint(0,9)
Rand3 = random.randint(0,9)

print('Your 3 digit code is ' + str(Rand) + str(Rand2) +str(Rand3))

Rand4 = random.randint(0,6)
Rand5 = random.randint(0,6)
Rand6 = random.randint(0,6)
Rand7 = random.randint(0,6)

print('Your 4 digit code is ' + str(Rand4) + str(Rand5) + str(Rand6) + str(Rand7))







