from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app  import App
import sqlite3

class shoppingInv(Widget):
    pass

class Shopping_inv(App):
    def build(self):
        #Connect to Database
        conn = sqlite3.connect("inventory.db")

        #Create A Cursor
        cur = conn.cursor()

        #Create Table
        cur.execute("CREATE TABLE if not exists Shopping_List(Item, Quantity)")
        
        #Commit changes
        conn.commit()

        #Close our connection
        conn.close
        return shoppingInv

if __name__=="__main__":
    Shopping_inv().run()

