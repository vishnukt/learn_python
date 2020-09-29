import sqlite3

db = sqlite3.connect("contact.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS phonebook(name TEXT,number INTEGER)")

choice = 1
while choice != 3:
    print("\n\nINSERT CONTACTS [1]")
    print("VIEW CONTACTS   [2]")
    print("EXIT            [3]")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        number = input("Enter Number : ")
        db.execute("INSERT INTO phonebook VALUES(?, ?)", (name, number))
        print("Contact Inserted Successfully")
    elif choice == 2:
        curs = db.cursor()
        curs.execute("SELECT * FROM phonebook")
        print("\nNAME\tNUMBER")
        for name, number in curs:
            print(name, "\t", number)
db.close()
