import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name text, phone integer, email text)")
db.execute("INSERT INTO contacts VALUES ('Yogi', 12345, 'yogi@email.com')")
db.execute("INSERT INTO contacts VALUES ('Om', 678910,'om@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print (cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for row in cursor:
    print(row)

cursor.close()
db.commit()
db.close()