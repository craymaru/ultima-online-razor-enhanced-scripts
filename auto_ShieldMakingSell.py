from Scripts.glossary.crafting.blacksmithing import blacksmithTools, FindBlacksmithTool, blacksmithCraftables

ingot_id = 0x1BF2
gold_id = 0x0EED
tong_id = 0x0FBB
gump_id = 949095101
npc_serial = 0x00004AE4

itemToCraft = blacksmithCraftables["heater shield"]
itemToCraft.Hue = 0x0000

SellAgent.Enable()
BuyAgent.Enable()


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
    

def openBank():
    Misc.WaitForContext(0x0000673F, 10000)
    Misc.ContextReply(0x0000673F, 1)
    Gumps.WaitForGump(1173999599, 10000)
    if Gumps.CurrentGump() == 1173999599:
        Gumps.SendAction(1173999599, 0)
    Misc.Pause(100)
openBank()
    
def getContainerItem(item_id, less_amount, get_amount, container=Player.Bank.Serial):
    current_amount = Items.ContainerCount(Player.Backpack, item_id, 0x0000)
    if current_amount < less_amount:
        
        if not container:
            openBank()
            
        item = Items.FindByID(item_id, 0x0000, container)
        if item:
            while Timer.Check("MoveItem"):
                Misc.Pause(100)
            Items.Move(item, Player.Backpack, get_amount - current_amount)
            Misc.Pause(550)
            Timer.Create("MoveItem", 550)

def putItem(item_id, container=Player.Bank.Serial):
 
    openBank()
    
    while Items.FindByID(item_id, 0x0000, Player.Backpack.Serial):
        item = Items.FindByID(item_id, 0x0000, Player.Backpack.Serial)
        if item:
            while Timer.Check("MoveItem"):
                Misc.Pause(100)
            Items.Move(item, container, -1)
            Timer.Create("MoveItem", 550)
        
def sellItem(npc_serial, item_id):
    Misc.WaitForContext(npc_serial, 10000)
    Misc.ContextReply(npc_serial, 5)
    Misc.Pause(100)

    
def buyItem(npc_serial, tong_id, less_amount):
    if Items.ContainerCount(Player.Backpack.Serial, tong_id, -1) <= less_amount: 
        Misc.WaitForContext(npc_serial, 10000)
        Misc.ContextReply(npc_serial, 4)
        Misc.Pause(100)

def hiding():
    if not Player.BuffsExist("Hiding"):
        if not Timer.Check("Skill"):
            Player.UseSkill("Hiding")
            Timer.Create("Skill", 10000)
        
while True:
    hiding()
    sellItem(npc_serial, itemToCraft.itemID)
    buyItem(npc_serial, tong_id, 1)
    putItem(gold_id)
    getContainerItem(ingot_id, 900, 1000)
    
    while Player.Weight < Player.MaxWeight - 50:
        createItem(itemToCraft)
    else:
        Gumps.WaitForGump(gump_id, 2000)
        if Gumps.CurrentGump() == gump_id:
            Gumps.SendAction(gump_id, 0)

