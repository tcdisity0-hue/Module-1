# age=int(input('Enter your age: '))
#
# if age <= 18:
#     print("Come right on in")
# else :
#     diff = age - 18
#     print(f"You're too old.You should've come {diff} years earlier")

print("1")

Length = int(input("How long is the Zander? "))
Size_limit = 42
Diff = Size_limit - Length

if Length >= Size_limit:
    print("Great catch! Take it home.")
else:
    print(f"The fish is too small by {Diff} cm. Release it.")

print("2")

Cabin = str(input("Welcome guest! What's your Cabin type? "))

if Cabin == "LUX":
    print("Your Cabin class includes an upper deck cabin with a window.")
elif Cabin == "A":
    print("Your Cabin class is above the car deck and is equipped is a window.")
elif Cabin == "B":
    print("Your Cabin class is a windowless cabin above the car deck.")
elif Cabin == "C":
    print("Your Cabin class is a windowless cabin below the car deck.")
else:
    print("Invalid Cabin class")

print("3")

Gender = str(input("What's your Gender? "))
H_value = int(input("What's your Hemoglobin value? "))

if Gender == "F" and 117 <= H_value <= 155:
    print("Your Hemoglobin value is normal")
elif Gender == "F" and H_value < 117 :
    print("Your Hemoglobin value is low")
elif Gender == "F" and 155 < H_value:
    print("Your Hemoglobin value is high")
elif Gender == "M" and 134 <= H_value <= 167 :
    print("Your Hemoglobin value is normal")
elif Gender == "M" and H_value < 134 :
    print("Your Hemoglobin value is low")
elif Gender == "M" and H_value > 167 :
    print("Your Hemoglobin value is high")

print("4")

Year = int(input("Enter your Year "))
if Year % 4 == 0:
    print("It's a Leap Year")
elif Year % 100 == 0 and Year % 400 == 0:
    print("It's a Leap Year")
else :
    print("It's not a Leap Year")


