def GetItemAmount():
    Misc.SendMessage("SELECT ITEM", 55)
    item_serial = Target.PromptTarget()
    item = Items.FindBySerial(item_serial)
    container = Items.FindBySerial(item.Container)
    contains_amount = Items.ContainerCount(item.Container, item.ItemID, item.Hue)

    Misc.SendMessage(item.Name + "(" + str(item.Hue) + ")" + " in the " + container.Name, item.Hue)
    Misc.SendMessage(" >> " + str(contains_amount), 60)

GetItemAmount()