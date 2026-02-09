print("1")

seasons = ("Winter","Spring","Summer","Autumn")

month = int(input("Enter the month: "))

season_check = (month % 12) // 3

print(seasons[season_check])

print("2")

names  = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Entered names: ")

for name in names:
    print(name)

print("3")

airport = {"FVRG":"FVRGRobert Mugabe Airport",
           "KJFK":"JFK Airport",
           "LUN":"Kenneth Kaunda Airport"
           }

while True:
    print("What would you like to do?")
    print("Enter - Enter a new airport")
    print("Fetch - Fetch airport information")
    print("Exit")

    choice = input("I want to: ")

    if choice == "Enter":
        icao = input("Enter ICAO: ")
        air_n = input("Enter airport name: ")
        airport[icao] = air_n
        print("Airport added")

    elif choice == "Fetch":
        icao = input("Enter ICAO: ")
        if icao in airport:
            print("The airport is", airport[icao])
        else:
            print("Airport not found")

    elif choice == "Exit":
        break

    else:
        print("Invalid choice")


