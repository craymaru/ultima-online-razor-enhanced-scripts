GumpId = 2066278152
ReCreateBtn = 21


def remake():
    Gumps.WaitForGump(GumpId, 3000)
    Gumps.SendAction(GumpId, ReCreateBtn)


def getCharges(tool):
    return int(str(tool.Properties[1]).split(": ")[1])


def main():
    
    firstTarget = Items.FindBySerial(Target.PromptTarget("Tool?", 68))
    
    while True:
        
        tool = Items.FindByID(firstTarget.ItemID, -1, Player.Backpack.Serial)
        
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
            Misc.Pause(100)
        
        Misc.Pause(100)
        


if __name__ == "__main__":
    main()