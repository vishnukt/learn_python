import sqlite3

db = sqlite3.connect("contact.sqlite")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS phonebook(name TEXT,number INTEGER)")

choice = 1
while choice != 3:
    print("\n\nINSERT CONTACTS [1]")
    print("VIEW CONTACTS   [2]")
    print("EXIT            [3]")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        name = input("Enter Name : ")
        number = input("Enter Number : ")
        c.execute("INSERT INTO phonebook VALUES(?, ?)", (name, number))
        print("Contact Inserted Successfully")
    elif choice == 2:
        c.execute("SELECT * FROM phonebook")
        print("\nNAME\tNUMBER")
        for name, number in c:
            print(name, "\t", number)
    elif choice == 3:
        db.commit()
        db.close()
        exit()
    else:
        print("Invalid Option!!!")
db.commit()
db.close()
