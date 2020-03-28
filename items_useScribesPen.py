scribespen_id = 0x0FBF

def UseItem(item_id):
    item = Items.FindByID(item_id, -1, Player.Backpack.Serial)
    if item:
        Items.UseItem(item)
        Misc.Pause(100)
        return True
    else:
        Misc.SendMessage(33, "You don\'t have %s!" % item.Name)
        Misc.Pause(100)
        return False

def Remake():
    if UseItem(scribespen_id):
        # REMAKE
        Gumps.WaitForGump(949095101, 10000)
        Gumps.SendAction(949095101, 21)
        Misc.Pause(1500)

def Meditation():
    if Player.Mana < (Player.ManaMax * 0.65):
        while Player.Mana < (Player.ManaMax * 0.90):
            if not Player.BuffsExist("Meditation"):
                Player.UseSkill("Meditation")
                Misc.Pause(10000)
            Misc.Pause(50)    
    
while True:
    Meditation()
    Remake()
    