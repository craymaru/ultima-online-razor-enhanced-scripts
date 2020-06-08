bulkgacha_button_number = 2

bulkgacha_serial = 0x40016844
bulkgacha_gump = 668631410

bulk_id = 0x2258
book_id = 0x2259

Misc.SendMessage("Bulk Orders Book CONTAINER?", 54)
container_serial = Target.PromptTarget()
Misc.SendMessage(container_serial, 80)
 
Misc.SendMessage("Finished CONTAINER?", 54)
finished_container_serial = Target.PromptTarget()
Misc.SendMessage(container_serial, 80)



def withdrawGold(lessThan=200, amount=5000):
    if Player.Gold <= lessThan:
        Player.ChatSay(33, "withdraw %i" % amount)
        Misc.Pause(200)
        


def buyBulkDeed(button_number):
    
    withdrawGold()
    
    if not Gumps.CurrentGump() == bulkgacha_gump:
        Items.UseItem(bulkgacha_serial)
        Gumps.WaitForGump(bulkgacha_gump, 1000)
    
    Gumps.SendAction(bulkgacha_gump, button_number)


def getBook():
    
    container = Items.FindBySerial(container_serial)

    if container.IsContainer:
        book = Items.FindByID(book_id, 0x0000, container_serial)
        if book:
            for prop in book.Properties:
                if "Deeds in book: 500" in str(prop):
                    while Timer.Check("MoveItem"):
                        Misc.Pause(100)
                    Items.Move(book, finished_container_serial, 1)
                    Timer.Create("MoveItem", 650)
                    Misc.Pause(200)
                    getBook()
            return book
                    
        else:
            Misc.SendMessage("There is not a bulk order book!", 33)
            end()
    else:
        Misc.SendMessage("This is not a container.", 33)
        end()
        

def putBulk():

    while Items.FindByID(bulk_id, -1, Player.Backpack.Serial):
        book = getBook()
        bulk = Items.FindByID(bulk_id, -1, Player.Backpack.Serial)
        if bulk:
            while Timer.Check("MoveItem"):
                Misc.Pause(10)
            Items.Move(bulk, book, 1)
            Timer.Create("MoveItem", 250)


        
while True:
    buyBulkDeed(bulkgacha_button_number)
    putBulk()
    




