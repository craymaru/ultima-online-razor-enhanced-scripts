from System.Collections.Generic import List

ToolId = 0x0FBB
GumpId = 2066278152
ReCreateBtn = 21
MeltBtn = 14
MeltItemIds = [
    0x0F4B, # double axe
    0x1441, # cutlass
]


def remake():
    Gumps.WaitForGump(GumpId, 3000)
    Gumps.SendAction(GumpId, ReCreateBtn)


def melt():
    items = Items.FindAllByID(MeltItemIds, -1, Player.Backpack.Serial, 0)
    
    for item in items:
        Gumps.WaitForGump(GumpId, 3000)
        Gumps.SendAction(GumpId, 14)
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(item)


def getCharges(tool):
    return int(str(tool.Properties[1]).split(": ")[1])


def main():
    
    while True:
        tool = Items.FindByID(ToolId, -1, Player.Backpack.Serial)
        
        if not tool:
            break
        
        Items.UseItem(tool)
        
        
        while True:
            tool = Items.FindBySerial(tool.Serial)
            if not tool:
                break

            charges = getCharges(tool)
            if not charges:
                break

            remake()
            melt()
            
            Misc.Pause(100)
            
            if Gumps.LastGumpTextExist("You do not have"):
                break
                
        
        Misc.Pause(100)
        


if __name__ == "__main__":
    main()
