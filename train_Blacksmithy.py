from Scripts.glossary.crafting.blacksmithing import blacksmithTools, FindBlacksmithTool, blacksmithCraftables

ingot_id = 0x1BF2
gump_id = 949095101


# itemToCraft = blacksmithCraftables["cutlass"]
# itemToCraft = blacksmithCraftables["short spear"] #74-95
# itemToCraft = blacksmithCraftables["dagger"]
# itemToCraft = blacksmithCraftables["platemail gorget"]
itemToCraft = blacksmithCraftables["no-dachi"]

def useToolFirst(tool_gump):
    Gumps.WaitForGump(tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!") \
    or not Gumps.CurrentGump() == tool_gump:
        item = FindBlacksmithTool( Player.Backpack )
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
    

        
def cleanItem(item_id):
    
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
        

def extractItem(item_id):
    Misc.Pause(1000)
    while Items.FindByID(item_id, 0x0000, Player.Backpack.Serial):
        item = Items.FindByID(item_id, 0x0000, Player.Backpack.Serial)
        if item:
            Player.UseSkill("Imbuing")
            
            Gumps.WaitForGump(1697188745, 1000)
            if Gumps.CurrentGump() == 1697188745:
                Gumps.SendAction(1697188745, 10010)
            Misc.Pause(200)
            Target.TargetExecute(item)
            Gumps.WaitForGump(2381473795, 1000)
            if Gumps.CurrentGump() == 2381473795:
                Gumps.SendAction(2381473795, 1)
            
            Misc.Pause(1000)
        
        
def getContainerItem(item_id, less_amount, get_amount, container=Player.Bank):
    if Items.ContainerCount(Player.Backpack, item_id, 0x0000) < less_amount:
        if not container:
            Player.ChatSay(80, "bank")
            Misc.Pause(100)
        item = Items.FindByID(item_id, 0x0000, container)
        if item:
            Items.Move(item, Player.Backpack, get_amount)
            Misc.Pause(550)


        
while True:
    cleanItem(itemToCraft.itemID)
    # extractItem(itemToCraft.itemID)
    getContainerItem(ingot_id, 100, 400, 0x400CA97E)
    createItem(itemToCraft)

