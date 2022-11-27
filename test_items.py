import sys

import os

# Open Container
def setContainer():
    Player.HeadMessage(66, "Set Container")
    target = Target.PromptTarget()
    item = Items.FindBySerial(target)
    container = item
    Items.UseItem(container)
    Misc.Pause(250)
    return container


    
# Get Container items
def getContainerItems(container):
    filter = Items.Filter()
    filter.Enabled
    all_items = Items.ApplyFilter(filter)
    items = [item for item in all_items if item.Container == container.Serial]
    Player.HeadMessage(66, "{} items".format(len(items)))
    return items


# Describe Item Propaties
def describeItemProps(item):
    for prop in item.Properties:
        Misc.SendMessage(prop, 55)


# Get Propaties
def getItemsPropaties(items, seachword):
    for item in items:
        for prop in item.Properties:
            if seachword in str(prop):
                Misc.SendMessage(item, 56)
        


# Window
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Drawing import Point
from System.Windows.Forms import TextBox, Keys, KeyPressEventHandler

from System.Windows import Forms

class ItemSearchForm(Forms.Form):
    def __init__(self):
        self.Width = 600
        self.Height = 600
        self.Text = 'Item Search'
        
        # Button: Set Container
        set_container_button = Forms.Button(Text='Set Container')
        set_container_button.Width = 100
        set_container_button.Click += self.setContainerOnClick
        set_container_button.Location = Point(25, 25)
        self.Controls.Add(set_container_button)
        
        # Button: Search
        search_button = Forms.Button(Text='Search')
        search_button.Click += self.searchOnClick
        search_button.Location = Point(25, 95)
        self.Controls.Add(search_button)
        
        # Textbox: Search
        self.textbox = TextBox()
        self.textbox.Text = ""
        self.textbox.Location = Point(25, 75)
        self.textbox.Width = 150
        # self.textbox.KeyDown += self.OnEnter
        self.textbox.KeyPress += KeyPressEventHandler(self.OnEnter)
        self.Controls.Add(self.textbox)
        
        # Close Button
        close_button = Forms.Button(Text='Close')
        close_button.Click += self.closeOnClick
        close_button.Location = Point(25, 195)
        self.Controls.Add(close_button)


    def setContainerOnClick(self, *args):
        container = setContainer()
        self.items = getContainerItems(container)
        
    def searchOnClick(self, *args):
        self.search()
        
    def search(self):
        Misc.SendMessage("Search: {}".format(self.textbox.Text))
        getItemsPropaties(self.items, self.textbox.Text)
        
        
    def OnEnter(self, e, args):
        key = args.KeyChar
        if key == Keys.Enter:
            self.Finished()

    def closeOnClick(self,*args):
        self.Close()
        

app = ItemSearchForm()
Forms.Application.Run(app)