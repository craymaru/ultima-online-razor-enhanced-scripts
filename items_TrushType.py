ignore_dic = {
    0x2259: "power scroll book"
}


def warnMessage():
    for i in range(10):
        Misc.SendMessage("WARNING: WIPE ITEMS!", 33)

        
def promptTrushItem():
    Misc.SendMessage("Trush Type?", 54)
    item_serial = Target.PromptTarget()
    item = Items.FindBySerial(item_serial)
    return item


def findTrushPouch():
    trush_pouch = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
    return trush_pouch


def trushItems():

    item = promptTrushItem()
    trush_pouch = findTrushPouch()
    
    while Items.FindByID(item.ItemID, item.Hue, Player.Backpack.Serial):
        del_item = Items.FindByID(item.ItemID, item.Hue, Player.Backpack.Serial)
        if del_item:
            if del_item.ItemID in ignore_dic:
                Misc.SendMessage("This item type in ignore list!", 54)
                break
            Misc.SendMessage("DANGER: DO NOT DRAG ITEMS!", 33)
            Items.Move(del_item, trush_pouch, -1)
            Misc.Pause(550)
                
        Misc.Pause(50)
    else:
        Misc.SendMessage("All items of targeted type wiped!", 80)


trushItems()