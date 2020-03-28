smithshammer_item_id = 0x13E3
melt_items_id = {
    0x0F5C: "Mace",
    0x1401: "Kryss",
    0x1441: "Cutlass",
    0x13FF: "Katana",
    0x1413: "platemail gorget"
}

def UseItem(item_id):
    item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
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

def Melt(item):
    if UseItem(smithshammer_id):
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 14)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(item)
        Misc.Pause(200)
    
def Melting(items_id):
    for item_id in items_id:
        # ITEM EXIST CHECK
        while Items.FindByID(item_id, -1, Player.Backpack.Serial):
            item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
            if item:
                Melt(item)

while True:
    Remake(smithshammer_item_id)
    Melting(melt_items_id)

