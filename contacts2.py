import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@rmail.com' WHERE contacts.phone = 12345"
update_cursor =db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.close()
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print( phone)
    print( email)
    print("__" * 20)
db.close()