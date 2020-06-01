Misc.SendMessage("DANGER: WIPE ITEMS!", 33)
Misc.SendMessage("Trush Type?", 54)
item_serial = Target.PromptTarget()
item = Items.FindBySerial(item_serial)

trush_poach = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)


while Items.FindByID(item.ItemID, item.Hue, item.Container):
    item = Items.FindByID(item.ItemID, item.Hue, item.Container)
    if item:
        Items.Move(item, trush_poach, -1)
        Misc.Pause(500)
    Misc.Pause(50)
else:
    Misc.SendMessage("All items of type wiped!", 54)