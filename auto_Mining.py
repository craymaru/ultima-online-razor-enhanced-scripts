# *-------------------------------*
#
#   Auto Mining v2
#
#   Created by Cray, MIT License.
#
# *-------------------------------*


### READ ME ######################

# 1. Agents > Organizer: Create list name "mining" then add ores.
# 2. Agents > Restock: Create list name "mining" then add shovels and irons.
# 3. Setting in the "Configuration" section below.
# 4. Save and Run!


# Configuration

# Tools
from System.Collections.Generic import List
MakeTools = True  # Need tinker skill and irons in restock container.

# Recalls
MiningRuneBookSerial = 0x4002EA47
MiningRunes = [2, 3, 4, 5, 6, 7, 8, 9, 10]

HomeRuneBookSerial = 0x4002EA47
HomeRune = 1

RecallDelay = 3000
UseSecretJorney = False

# Containers
OrganizeContainerSerial = 0x4002CEE4
OrganizeDelay = 2000

RestockContainerSerial = 0x4002CEED

# Digging
OffsetX = -1
OffsetY = 0
OffsetZ = 0
MaxDigCount = 10
DigGround = False
Tools = [
    0x0F39,  # shovel
    0x0E86,  # pickaxe
]

##################################


# Lazyload
Player.HeadMessage(51, "Loading...")
Misc.Pause(1000)
for i in range(3, 0, -1):
    Player.HeadMessage(51, i)
    Misc.Pause(1000)
Player.HeadMessage(63, "Start Mining!")

RuneBookGumpId = 89
LogColor = 55
MiningRuneBook = Items.FindBySerial(MiningRuneBookSerial)
HomeRuneBook = Items.FindBySerial(HomeRuneBookSerial)
ToolKitId = 0x1EB8
ShovelId = 0x0F39
ShovelBtn = 72
Shovels = 10
ToolKitBtn = 23
MultiSwing = True
GumpId = 2066278152


def organize():
    Misc.SendMessage("Organize", LogColor)

    Organizer.RunOnce("mining", Player.Backpack.Serial, OrganizeContainerSerial, 200)
    Misc.Pause(OrganizeDelay)


def restock():
    Misc.SendMessage("Restock", LogColor)

    Restock.RunOnce("mining", RestockContainerSerial,
                    Player.Backpack.Serial, 200)
    Misc.Pause(1000)


def getPos():
    return Player.Position.X, Player.Position.Y, Player.Position.Z


def sustainCreatbles(itemId, button, num):
    while True:
        if Gumps.LastGumpTextExist("You do not have sufficient metal to make that."):
            end()
        items = Items.FindAllByID(itemId, -1, Player.Backpack.Serial, 0)
        if num <= len(items):
            break
        if not Gumps.CurrentGump() == GumpId:
            Items.UseItem(Items.FindByID(
                ToolKitId, -1, Player.Backpack.Serial))
            Misc.Pause(1000)
        Gumps.WaitForGump(GumpId, 3000)
        Gumps.SendAction(GumpId, 15)  # Tool Category
        Gumps.WaitForGump(GumpId, 3000)
        Gumps.SendAction(GumpId, button)
        Misc.Pause(2000)
    Misc.Pause(2000)
    Gumps.CloseGump(GumpId)


def makeTinkerTools():
    Misc.SendMessage("Make tinker tool", 55)
    sustainCreatbles(ToolKitId, ToolKitBtn, 2)


def makeShovels():
    Misc.SendMessage("Make tool", 55)
    sustainCreatbles(ShovelId, ShovelBtn, Shovels)


def recall(runebook, rune, isJorney=False, disableLog=False):
    if not disableLog:
        Misc.SendMessage("Rune: {rune}".format(rune=rune), LogColor)

    if rune < 1 or 16 < rune:
        Misc.SendMessage("Invalid rune number!")
        return

    button = min(max(1, rune), 16)

    if isJorney:
        button += 74  # SecretJourney 75-90
    else:
        button += 49  # Recall 50-65

    beforePos = getPos()

    Journal.Clear()
    while True:
        Gumps.SendAction(89, 0)  # Close Runebook
        Misc.Pause(100)
        Items.UseItem(runebook)
        Gumps.WaitForGump(RuneBookGumpId, 1000)
        Gumps.SendAction(RuneBookGumpId, button)
        Misc.Pause(RecallDelay)

        if beforePos != getPos():
            break
        if Journal.Search("Something is blocking the location."):
            break


def goHome():
    Misc.SendMessage("Home", LogColor)
    recall(HomeRuneBook, HomeRune, disableLog=True)


def goMiningPoint(rune):
    recall(MiningRuneBook, rune)


def getFirstTile(x, y, map):
    for tile in Statics.GetStaticsTileInfo(x, y, map):
        return tile


def getTools():
    return Items.FindAllByID(Tools, -1, Player.Backpack.Serial, 0)


def mining():
    Misc.SendMessage("Mining", LogColor)

    Journal.Clear()

    digCount = MaxDigCount
    while Player.Weight < Player.MaxWeight - 150 and 0 < digCount:

        if Journal.Search("There is no metal here to mine."):
            break

        if Journal.Search("You have worn out your tool!"):
            break

        tools = getTools()

        if not tools:
            Player.HeadMessage(38, "Oops, I have no tools!")
            goHome()
            end()

        Player.HeadMessage(60, "*dig*")

        for tool in tools:
            Items.UseItem(tool)
            Misc.Pause(100)

            x, y, z = getPos()
            tile = getFirstTile(x, y, Player.Map)

            if DigGround and tile:
                Target.TargetExecute(x, y, z, tile.StaticId)
            else:
                Target.TargetExecute(x + OffsetX, y + OffsetY, z + OffsetZ)

            if not MultiSwing:
                break

        digCount -= 1
        Misc.Pause(1000)


def main():
    while True:
        for rune in MiningRunes:
            goHome()
            organize()
            restock()
            if MakeTools:
                makeTinkerTools()
                makeShovels()
            goMiningPoint(rune)
            mining()


if __name__ == "__main__":
    main()
