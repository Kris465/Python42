import os
# import sqlite3


# connection = sqlite3.connect('zoo.db')
# cursor = connection.cursor()

# cursor.execute("DROP TABLE animals")

# connection.commit()
# connection.close()

if os.path.exists('zoo.db'):
    os.remove('zoo.db')
