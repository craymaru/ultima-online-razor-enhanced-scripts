Misc.SendMessage("Power Scroll Book?", 54)
book_serial = Target.PromptTarget()
book = Items.FindBySerial(book_serial)

if book.ItemID == 0x2259:

    while Items.FindByID(0x14F0, 0x0481, book.Container):
        item = Items.FindByID(0x14F0, 0x0481, book.Container)
        if item:
            Items.Move(item, book, -1)
            Misc.Pause(500)
        Misc.Pause(50)
    else:
        Misc.SendMessage("All scrolls have entered the book.")
        
else:
    Misc.SendMessage("This item is not the book.")