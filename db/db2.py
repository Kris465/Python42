import sqlite3


connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM animals WHERE name = 'Попугай'")

connection.commit()

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
