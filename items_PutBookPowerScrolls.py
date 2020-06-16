
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
        
putPowerScrolls()