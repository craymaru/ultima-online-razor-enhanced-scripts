from AutoComplete import *

#CutItemId = 0x1EFD # fancy shirt
CutItemId = 0x1515 # cloak

SewingKitId = 0x0F9D
SewingKitGumpId = 2066278152
ReCreateButton = 21
Scissors = Items.FindByID(0x0F9F, -1, Player.Backpack.Serial)

def checkNotHaveEnough():
    if Gumps.LastGumpTextExist("You do not have"):
        Misc.SendMessage("Item not enough!")
        end()

def getCharges(tool):
    return int(str(tool.Properties[1]).split(": ")[1])
        

def cut(item):
    Items.UseItem(Scissors)
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(item)


def clean():
    while True:
        item = Items.FindByID(CutItemId, -1, Player.Backpack.Serial)
        if item == None:
            break

        cut(item)
        Misc.Pause(100)


def main():
    while True:
        clean()
        
        tool = Items.FindByID(SewingKitId, 0, Player.Backpack.Serial)
        if not tool:
            break
        Items.UseItem(tool)
        
        while True:
            tool = Items.FindBySerial(tool.Serial)
            if not tool:
                break

            if not getCharges(tool):
                break
                
            Gumps.WaitForGump(SewingKitGumpId, 1000)
            checkNotHaveEnough()
            Gumps.SendAction(SewingKitGumpId, ReCreateButton)


if __name__ == "__main__":
    main()
