Misc.SendMessage("Power Scroll Book?", 54)
book_serial = Target.PromptTarget()
book = Items.FindBySerial(book_serial)


while Items.FindByID(0x14F0, 0x0481, book.Container):
    item = Items.FindByID(0x14F0, 0x0481, book.Container)
    if item:
        Items.Move(item, book, -1)
        Misc.Pause(500)
    Misc.Pause(50)