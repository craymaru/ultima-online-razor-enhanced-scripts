items = {
    "Arrow Fletching": {"id": 0x1022, "hue": 0x0000},
    "Magical Residue": {"id": 0x2DB1, "hue": 0x0000},
    "Ork Board": {"id": 0x1BD7, "hue": 0x07da}
}

container_serial = 0x4002B0B5


def CloseGamp():
    Gumps.WaitForGump(949095101, 1000)
    Gumps.SendAction(949095101, 0)

    
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

        
def ImbuingExtractAll(container_serial):
    CloseGamp()
    Player.UseSkill("Imbuing")
    Gumps.WaitForGump(1697188745, 10000)
    Gumps.SendAction(1697188745, 10011)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(container_serial)
    Gumps.WaitForGump(3074326971, 10000)
    Gumps.SendAction(3074326971, 1)
    Misc.Pause(1000)
    
    
def PutItemToBank(item_id, item_hue, amount):
    item = Items.FindByID(item_id, item_hue, Player.Backpack.Serial)
    if item:
        Items.Move(item, Player.Bank.Serial, amount)
        Misc.Pause(700)

        
def GetItemFromBank(item_id, item_hue, amount):
    now_amount = Items.BackpackCount(item_id, item_hue)
    if amount > now_amount:
        need_amount = amount - now_amount
        item = Items.FindByID(item_id, item_hue, Player.Bank.Serial)
        if item:
            Items.Move(item, Player.Backpack.Serial, need_amount)
            Misc.Pause(500)
  
    
while True:
    ImbuingExtractAll(container_serial)
    PutItemToBank(items["Magical Residue"]["id"], items["Magical Residue"]["hue"], -1)
    GetItemFromBank(items["Ork Board"]["id"], items["Ork Board"]["hue"], 140)
    for i in range(20):
        Remake(items["Arrow Fletching"]["id"])
        
    
