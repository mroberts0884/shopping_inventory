from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app  import App
import sqlite3
from kivy.uix.screenmanager import ScreenManager, Screen


class shoppingInv(Widget):
    pass

class Shoppinginv(App):
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

        def add(self):
            
            item = self.root.ids.item_input
            quantity = self.root.ids.quantity_input
               #Connect to Database
            conn = sqlite3.connect("inventory.db")

            #Create A Cursor
            cur = conn.cursor()

           
            #Add Item and Quantity
            cur.execute("INSERT INTO Shopping_List(Item, Quantity) VALUES(?,?)", item, quantity)

            #clear input
            self.root.ids.item_input = ''
            self.root.ids.quantity_input = ''

            #Commit changes
            conn.commit()

            #Close our connection
            conn.close

        return shoppingInv()

if __name__=="__main__":
    Shoppinginv().run()

