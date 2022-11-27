from Scripts.glossary.crafting.tailoring import tailoringTools, FindTailoringTool, tailoringCraftables

gump_id = 949095101

# itemToCraft = tailoringCraftables["fur boots"]
# itemToCraft = tailoringCraftables["ninja tabi"]
itemToCraft = tailoringCraftables["cloth ninja hood"]


def useToolFirst(tool_gump):
    Gumps.WaitForGump(tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!") \
    or not Gumps.CurrentGump() == tool_gump:
        item = FindTailoringTool(Player.Backpack)
        if item:
            Items.UseItem(item)
        else:
            end()


def createItem(itemToCraft):
    
    useToolFirst(gump_id)
    
    for path in itemToCraft.gumpPath:
        Gumps.WaitForGump( path.gumpID, 2000 )
        if Gumps.CurrentGump() == path.gumpID and not Gumps.LastGumpTextExist(itemToCraft.name):
            Gumps.SendAction( path.gumpID, path.buttonID )
        if Gumps.CurrentGump() == path.gumpID and Gumps.LastGumpTextExist(itemToCraft.name):
            Gumps.SendAction( path.gumpID, path.buttonID )
        

def clean(item_id):
    
    def getCleanupPouch():
        cleanup_pouch = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
        return cleanup_pouch
    
    while Items.FindByID(item_id, 0x0000, Player.Backpack.Serial):
        item = Items.FindByID(item_id, 0x0000, Player.Backpack.Serial)
        if item:
            if not Timer.Check("MoveItem"):
                Items.Move(item, getCleanupPouch(), 1)
                Timer.Create("MoveItem", 550)
        Misc.Pause(100)
        
        
def getBankItem(item, less_amount, get_amount):
    if Items.BackpackCount(item, 0x0000) < less_amount:
        if not Player.Bank:
            Player.ChatSay(80, "bank")
        Misc.Pause(100)
        item = Items.FindByID(item, 0x0000, Player.Bank.Serial)
        Items.Move(item, Player.Backpack.Serial, get_amount)
        Misc.Pause(550)


while True:
    # getBankItem(ingot_id, 100, 400)
    createItem(itemToCraft)
    clean(itemToCraft.itemID)