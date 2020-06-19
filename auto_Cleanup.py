tinker_tool_id = 0x1EB8
bracelet_id = 0x1086
ingot_id = 0x1BF2
tinker_tool_gump = 949095101



def useItem(tinker_tool_id):
    item = Items.FindByID(tinker_tool_id, 0x0000, Player.Backpack.Serial)
    if item:
        Items.UseItem(item)

        
def useToolFirst():
    Gumps.WaitForGump(tinker_tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!") \
    or not Gumps.CurrentGump() == tinker_tool_gump:
        useItem(tinker_tool_id)
        
        
def selectGumpMenu(requiredText, button):
    Gumps.WaitForGump(tinker_tool_gump, 10000)
    if not Gumps.LastGumpTextExist(requiredText) \
    and Gumps.CurrentGump() == tinker_tool_gump:
        Gumps.SendAction(tinker_tool_gump, button)

        
def selectGumpItem(requiredText, button):
    Gumps.WaitForGump(tinker_tool_gump, 10000)
    if Gumps.LastGumpTextExist(requiredText) \
    and Gumps.CurrentGump() == tinker_tool_gump:
        Gumps.SendAction(tinker_tool_gump, button)
        
        
def makeTool(amount):
    if Items.ContainerCount(Player.Backpack, tinker_tool_id) < amount:

        useToolFirst()
        selectGumpMenu("tinker's tools", 15) # Button: Tools
        selectGumpItem("tinker's tools", 23) # Button: Tinkertool


def makeBracelet():
    useToolFirst()
    selectGumpMenu("bracelet", 1) # Button: Jewelry
    selectGumpItem("bracelet", 9) # Button: Bracelet
    

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
        Misc.Pause(100)
        
        
def getBankItem(item, less_amount, get_amount):
    if Items.BackpackCount(item, -1) < less_amount:
        item = Items.FindByID(item, -1, Player.Bank.Serial)
        Items.Move(item, Player.Backpack.Serial, get_amount)
        Misc.Pause(550)
        
def hiding():
    if not Player.BuffsExist("Hiding"):
        if not Timer.Check("Skill"):
            Player.UseSkill("Hiding")
            Timer.Create("Skill", 10000)
            
Player.ChatSay(80, "bank")
while True:
    hiding()
    getBankItem(ingot_id, 100, 400)
    makeTool(2)
    makeBracelet()
    clean()
