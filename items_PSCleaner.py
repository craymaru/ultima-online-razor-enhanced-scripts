trush_items = [
    {"ItemID": 0x14EF, "Hue": 0x0490, "Name": "pink skill scroll"},
    {"ItemID": 0x1E22, "Hue": 0x0000, "Name": "Mastery"},
    {"ItemID": 0x1AE1, "Hue": 0x01ee, "Name": "skull of greed"}
]


def getBook():
    Misc.SendMessage("Power Scroll Book?", 54)
    book_serial = Target.PromptTarget()
    book = Items.FindBySerial(book_serial)
    return book

def putPowerScrolls():
    book = getBook()
    if book.ItemID == 0x2259:

        containers = [book.Container, Player.Backpack.Serial]
        
        for container in containers:
            while Items.FindByID(0x14F0, 0x0481, container):
                item = Items.FindByID(0x14F0, 0x0481, container)
                if item:
                    Items.Move(item, book, -1)
                    Misc.Pause(500)
                Misc.Pause(50)
        
        Misc.SendMessage("All scrolls have entered the book.", 80)
            
    else:
        Misc.SendMessage("This item is not the book.", 54)

        
        
def findTrushPouch():
    trush_pouch = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
    return trush_pouch


def trushItems(trush_items):

    trush_pouch = findTrushPouch()
    
    for item in trush_items:
        
        while Items.FindByID(item["ItemID"], item["Hue"], Player.Backpack.Serial):
            del_item = Items.FindByID(item["ItemID"], item["Hue"], Player.Backpack.Serial)
            if del_item:
                Misc.SendMessage("DANGER: DO NOT DRAG ITEMS!", 33)
                Items.Move(del_item, trush_pouch, -1)
                Misc.Pause(550)
                    
            Misc.Pause(50)
        
    Misc.SendMessage("All items of targeted type wiped!", 80)


putPowerScrolls()
trushItems(trush_items)