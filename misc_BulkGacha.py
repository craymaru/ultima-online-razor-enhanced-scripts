import re

bulkgacha_button_number = 4

bulkgacha_serial = 0x40016844
bulkgacha_gump = 668631410

bulk_id = 0x2258
book_id = 0x2259

Misc.SendMessage("Bulk Orders Books CONTAINER?", 54)
container_serial = Target.PromptTarget()
Misc.SendMessage(container_serial, 80)
 
Misc.SendMessage("Finished CONTAINER?", 54)
finished_container_serial = Target.PromptTarget()
Misc.SendMessage(container_serial, 80)



def withdrawGold(lessThan=200, amount=20000):
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
            return book
                    
        else:
            Misc.SendMessage("There is not a bulk order book!", 33)
            end()
    else:
        Misc.SendMessage("This is not a container.", 33)
        end()

def evalBook(book):
    for prop in book.Properties:
        match = re.search("^Deeds in book: (\d+)$", str(prop))
        if match:
            Misc.SendMessage(match.groups()[0] + "/500", 80)
            space = 500 - int(match.groups()[0])
            if not space:
                Items.Move(book, finished_container_serial, 1)
                Misc.Pause(550)
            return space
            

def putBulk():

    while Items.FindByID(bulk_id, -1, Player.Backpack.Serial):
        book = getBook()
        evalBook(book)
        bulk = Items.FindByID(bulk_id, -1, Player.Backpack.Serial)
        if bulk and book:
            Items.Move(bulk, book, 1)
            Misc.Pause(610)
            
    Gumps.WaitForGump(1425364447, 10000)
    if Gumps.CurrentGump() == 1425364447:
        Gumps.SendAction(1425364447, 0)

        
while True:
    putBulk()
    
    book = getBook()
    if not book:
        break
    
    space = evalBook(book)
    if 50 <= space:
        space = 50
    
    for i in range(space):
        buyBulkDeed(bulkgacha_button_number)
    

