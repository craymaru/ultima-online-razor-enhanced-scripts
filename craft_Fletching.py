tool_item_id = 0x1022

def UseItem(item_id):
    item = Items.FindByID(item_id, -1, -1)
    if item:
        Items.UseItem(item)
        Misc.Pause(100)
        return True
    else:
        Misc.SendMessage("You don\'t have Item!", 33)
        Misc.Pause(1000)
        return False

def Remake(tool_item_id):
    if UseItem(tool_item_id):
        # REMAKE
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 21)
        Misc.Pause(1500)

while True:
    Remake(tool_item_id)
