tinker_tool_id = 0x1EB8
bracelet_id = 0x1086
ingot_id = 0x1BF2
tinker_tool_gump = 949095101


def useItem(tinker_tool_id):
    item = Items.FindByID(tinker_tool_id, 0x0000, Player.Backpack.Serial)
    if item:
        Items.UseItem(item)


def makeTool(amount):
    if Items.ContainerCount(Player.Backpack, tinker_tool_id) < amount:
        Gumps.WaitForGump(tinker_tool_gump, 10000)
        if Gumps.LastGumpTextExist("You have worn out your tool!"):
            useItem(tinker_tool_id)
        
        if not Gumps.CurrentGump() == tinker_tool_gump:
            useItem(tinker_tool_id)
        
        Gumps.WaitForGump(tinker_tool_gump, 10000)
        if Gumps.CurrentGump() == tinker_tool_gump:
            Gumps.SendAction(tinker_tool_gump, 15) # Button: Tools

        Gumps.WaitForGump(tinker_tool_gump, 10000)
        if Gumps.CurrentGump() == tinker_tool_gump:
            Gumps.SendAction(tinker_tool_gump, 23) # button: Tinkertool


def clean():
    
    def getCleanupPouch():
        cleanup_pouch = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
        return cleanup_pouch
    
    while Items.FindByID(bracelet_id, 0x0000, Player.Backpack.Serial):
        item = Items.FindByID(bracelet_id, 0x0000, Player.Backpack.Serial)
        if item:
            if not Timer.Check("MoveItem"):
                Items.Move(item, getCleanupPouch(), 1)
                Timer.Create("MoveItem", 550)
                
def makeBracelet():
    
    Gumps.WaitForGump(tinker_tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!"):
        useItem(tinker_tool_id)
        
    if not Gumps.CurrentGump() == tinker_tool_gump:
        useItem(tinker_tool_id)
    
    Gumps.WaitForGump(tinker_tool_gump, 10000)
    if Gumps.CurrentGump() == tinker_tool_gump:
        Gumps.SendAction(tinker_tool_gump, 1) # Button: Tools

    Gumps.WaitForGump(tinker_tool_gump, 10000)
    if Gumps.CurrentGump() == tinker_tool_gump:
        Gumps.SendAction(tinker_tool_gump, 9) # Button: Bracelet
    

def getBankItem(item, less_amount, get_amount):
    if Items.BackpackCount(item, -1) < less_amount:
        if Player.Bank.Serial:
            Player.ChatSay(80, "bank")
        Misc.Pause(100)
        item = Items.FindByID(item, -1, Player.Bank.Serial)
        Items.Move(item, Player.Backpack.Serial, get_amount)
        Misc.Pause(550)
    
while True:
    makeTool(2)
    makeBracelet()
    clean()
    getBankItem(ingot_id, 100, 400)
