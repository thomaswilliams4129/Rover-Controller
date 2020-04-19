import sqlite3

with sqlite3.connect("Authenticate.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute("""
INSERT INTO users(username,password)
VALUES("admin", "P@ssw0rd1")
""")

db.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())
