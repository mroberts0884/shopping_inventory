import sqlite3


#Create inventory database
con = sqlite3.connect("inventory.db")
cur = con.cursor()

#Create Table in Database
#cur.execute("CREATE TABLE Shopping_List(Item, Quantity)")

