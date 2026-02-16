print("1")

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Alyx",
    password="Pillow45",
    autocommit=True)

cursor = connection.cursor()

icao = input("Enter ICAO: ")
sql = """ select name, municipality from airport WHERE ident = %s"""

cursor.execute(sql, (icao,))

result = cursor.fetchone()

if result:
    name, town = result
    print("Airport name:", name)
    print("Town:", town)
else:
    print("Airport not found.")

cursor.close()
connection.close()

print("2")

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Alyx",
    password="Pillow45",
    autocommit=True
)

cursor = connection.cursor()

country = input("Enter country code (e.g. FI): ").strip().upper()

sql = """select type, count(*) from airport where iso_country = %s group by type order by type"""

cursor.execute(sql, (country,))

results = cursor.fetchall()

if results:
    print(f"Airports in {country}:")
    for airport_type, amount in results:
        print(f"{airport_type}: {amount}")
else:
    print("No airports.")

cursor.close()
connection.close()
