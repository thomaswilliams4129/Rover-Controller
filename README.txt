# HOW TO ADD USER A LOGIN #

1. Open Create_New_Database.py

2. Add another method like this one:
    cursor.execute("""
    INSERT INTO users(username,password)
    VALUES("username", "password")
    """)

3. replace the username and password in the VALUES with the credentials you want

4. Then run:
    python3 Create_New_Database.py
