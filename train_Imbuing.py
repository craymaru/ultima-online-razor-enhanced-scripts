import re

from Scripts.glossary.crafting.blacksmithing import blacksmithTools, FindBlacksmithTool, blacksmithCraftables

gump_id = 949095101
ingot_id = 0x1BF2
ingot_hue = 0x0973
citrine_id = 0x0F15
amber_id = 0x0F25
ruby_id = 0x0F13
diamond_id = 0x0F26
magical_residue_id = 0x2DB1


itemToCraft = blacksmithCraftables["dagger"]
itemToCraft.Hue = 0x0973

def useToolFirst(tool_gump):
    Gumps.WaitForGump(tool_gump, 2000)
    if Gumps.LastGumpTextExist("You have worn out your tool!") \
    or not Gumps.CurrentGump() == tool_gump:
        item = FindBlacksmithTool( Player.Backpack )
        if item:
            Items.UseItem(item)
        else:
            Player.HeadMessage("You have not a blacksmith tool!")
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
    
    while Items.FindByID(item_id, ingot_hue, Player.Backpack.Serial):
        item = Items.FindByID(item_id, ingot_hue, Player.Backpack.Serial)
        if item:
            if not Timer.Check("MoveItem"):
                Items.Move(item, getCleanupPouch(), 1)
                Timer.Create("MoveItem", 550)
        Misc.Pause(100)
        

def extractItem(item):
    
    Misc.Pause(1000)
    
    if not Gumps.CurrentGump() == 1697188745:
        Player.UseSkill("Imbuing")
        Gumps.WaitForGump(1697188745, 10000)
        Gumps.SendAction(1697188745, 10010)
    else:
        Gumps.SendAction(1697188745, 10010) # 1: imbuing
    
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(item)
    Gumps.WaitForGump(2381473795, 10000)
    if Gumps.CurrentGump() == 2381473795:
        Gumps.SendAction(2381473795, 1)
    
    Misc.Pause(1000)

    
def getContainerItem(item_id, item_hue, less_amount, get_amount, container=Player.Bank):
    if Items.ContainerCount(Player.Backpack, item_id, item_hue) < less_amount:
        if container:
            Items.UseItem(container)
            Misc.Pause(300)
        else:
            Player.ChatSay(80, "bank")
            Misc.Pause(100)
        item = Items.FindByID(item_id, item_hue, container)
        if item:
            Items.Move(item, Player.Backpack, get_amount)
            Misc.Pause(550)

            
def imbuingItem(itemToCraft):
    Misc.Pause(1000)
    
    def lineMatch():
        linelist = Gumps.LastGumpGetLineList()
        
        strength_num = None
        for line in linelist:
            strength = re.search("^(\d+)/20$", str(line))
            if strength:
                Player.HeadMessage(54, strength.groups()[0] + "/20")
                strength_num = int(strength.groups()[0])
            probability = re.search("^(\d+.\d)%$", str(line))
            if probability:
                Player.HeadMessage(54, probability.groups()[0] + "%")
        return strength_num
    
    def propMatch(item, regex):
        for prop in item.Properties:
            match = re.search(regex, str(prop))
            if match:
                return match
        
        
    while Items.FindByID(itemToCraft.itemID, itemToCraft.Hue, Player.Backpack.Serial):
         
        getContainerItem(citrine_id, 0x0000, 100, 100, 0x400CA97E)
        getContainerItem(amber_id, 0x0000, 100, 100, 0x400CA97E)
        getContainerItem(ruby_id, 0x0000, 100, 100, 0x400CA97E)
        getContainerItem(diamond_id, 0x0000, 100, 100, 0x400CA97E)
        getContainerItem(magical_residue_id, 0x0000, 100, 100, 0x400D3E1F)
        
        item = Items.FindByID(itemToCraft.itemID, itemToCraft.Hue, Player.Backpack.Serial)
        
        if item:
            if not Gumps.CurrentGump() == 1697188745:
                Player.UseSkill("Imbuing")
                Gumps.WaitForGump(1697188745, 10000)
                Gumps.SendAction(1697188745, 10005)
            else:
                Gumps.SendAction(1697188745, 10005) # 1: imbuing

            Target.WaitForTarget(10000, False)
            Target.TargetExecute(item)
            
            
            # DISPEL
            if not propMatch(item, "^hit fire area \d+%$"):
                Player.HeadMessage(77, "Fire Area!")
                
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10006) # 3: Area
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10131) # 3: Fire
                Gumps.WaitForGump(2270339787, 10000)
                strength_num = lineMatch()
                Gumps.WaitForGump(2270339788, 10000) 
                Gumps.SendAction(2270339788, 10053)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054) # value 45
                
            elif not propMatch(item, "^hit dispel \d+%$"):
                Player.HeadMessage(77, "Dispel!")
            
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10007) # 4: additional
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10139) # 10: dispel
                Gumps.WaitForGump(2270339787, 10000)
                strength_num = lineMatch()
                Gumps.WaitForGump(2270339788, 10000) 
                Gumps.SendAction(2270339788, 10053)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054) # value 45
                
            elif not propMatch(item, "^hit stamina leech \d+%$"):
                Player.HeadMessage(77, "StaminaLeech!")
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10007) # 4: additional
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10126) # 1: stamina leech
                strength_num = lineMatch()
                Gumps.WaitForGump(2270339788, 10000) 
                Gumps.SendAction(2270339788, 10053)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10055)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10054) # value 45
                
            else:
                # LUCK
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10003) # 5: other
                Gumps.WaitForGump(2270339787, 10000)
                Gumps.SendAction(2270339787, 10121) # 1: luck
                Gumps.WaitForGump(2270339787, 10000)
                strength_num = lineMatch()
                
                #Gumps.WaitForGump(2270339788, 10000)
                #Gumps.SendAction(2270339788, 10054) # value +1
                #Gumps.WaitForGump(2270339788, 10000)
                #Gumps.SendAction(2270339788, 10055) # value +10
                #Gumps.WaitForGump(2270339788, 10000)
                #Gumps.SendAction(2270339788, 10055) # value +10
                #Gumps.WaitForGump(2270339788, 10000)
                #Gumps.SendAction(2270339788, 10056) # value Max
                
                
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10056)
                Gumps.WaitForGump(2270339788, 10000)
                Gumps.SendAction(2270339788, 10052) # value 90

            Gumps.WaitForGump(2270339788, 10000)
            Gumps.SendAction(2270339788, 10100) # Imbuing!
            
            Misc.Pause(1000)
            
            if 19 <= strength_num:
                Player.HeadMessage(55, "Extract!")
                extractItem(item)
        
while True:
    # cleanItem(itemToCraft.itemID)
    # extractItem(itemToCraft.itemID)
    
    getContainerItem(ingot_id, ingot_hue, 100, 100, 0x400CA97E)
    
    
    while Items.ContainerCount(Player.Backpack.Serial, itemToCraft.itemID, itemToCraft.Hue) < 5:
        createItem(itemToCraft)
    else:
        # Close
        Gumps.WaitForGump(gump_id, 2000)
        if Gumps.CurrentGump() == gump_id:
            Gumps.SendAction(gump_id, 0)

    imbuingItem(itemToCraft)





