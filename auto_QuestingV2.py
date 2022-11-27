# QUESTING

# REQUIRED:
# * DO NOT HAVE BACKPACKS
# * PACK PET
# * TRUSH POUCH


import sys
import re

# SETTINGS
# ========================
QuestMobileSerial = 0x0000237A
QuestName = "Hâute Couture"
QuestAlreadyStartedDescription = "I will be in your debt if you bring me flower garlands"
QuestAlreadyDoneDescription = " I appreciate your service. Now, see what elven hands can create."

PackPetSerial = 0x0000A125
PackPetFoodType = "fruit"  # "meat" or "fruit"

TargetItemIds = {
    0x2831: "Recipe Scroll",
    0x2F58: "Talisman",
    0x2F59: "Talisman",
    0x2F5A: "Talisman",
    0x2F5B: "Talisman"
}

TargetPropertiesRegex = {
    "Recipe Scroll",
    "Slayer",
    "^(?=.*Bonus)(?=.*(2[5-9]|[3-9][0-9])).*$",  # Talisman Bonus and 25-99
    "Speed"
}

ToolKitId = 0x0F9D  # Tailoring Tool
ToolGumpId = 2066278152  # Tailoring Gump

CraftItemId = 0x2306
CraftAmount = 10

MaterialId = 0x1766  # Cloth
MaterialThreshold = 500
MaterialTakeAmount = 1000

# ========================


QuestGumpId = 269917563
QuestItemColorId = 0x04ea  # Orange
hasQuest = False


Fruits = [
    0x09D0,  # apple
    0x09D1,  # grape
    0x09D2  # peach
]

Meats = [
    0x09B7,  # chicken
    0x09C0,  # sausage
    0x09C9,  # ham
    0x09F2  # ribs
]

OtherFoods = [
    0x097B,  # fish
    0x097D,  # cheese
    0x09EB  # muffins
]


def Warning():
    Misc.SendMessage("WARNING:", 33)
    Misc.SendMessage("Backpacks will be DESTROYED!!", 33)
    Misc.SendMessage("Select your trash poach.", 53)

    global TrushPouch
    TrushPouch = Target.PromptTarget()
    if TrushPouch == -1:
        Misc.SendMessage("Cancelled!", 5)
        sys.exit()


def MoveItemToBackpack(item):
    Items.Move(item, Player.Backpack.Serial, 0)
    Misc.Pause(1000)


def MoveItemToTrush(item):
    Items.Move(item, TrushPouch, 0)
    Misc.Pause(1000)


def HasAllQuestItem():
    return CraftAmount <= Items.BackpackCount(CraftItemId, QuestItemColorId)


def GetItemFromPet(item, threshold_amount, take_amount):
    if Items.BackpackCount(item, -1) < threshold_amount:
        pet = Mobiles.FindBySerial(PackPetSerial)
        get_item = Items.FindByID(item, -1, pet.Backpack.Serial)
        Items.Move(get_item, Player.Backpack.Serial, take_amount)
        Misc.Pause(1000)


def OrganizeSubBackpackItems():

    Misc.SendMessage("ORGANIZE ITEMS", 1150)
    Misc.SendMessage("==============", 1150)

    BackpackId = 0x0E75
    while Items.FindByID(BackpackId, -1, Player.Backpack.Serial):
        sub_backpack = Items.FindByID(BackpackId, -1, Player.Backpack.Serial)
        if sub_backpack:

            for item_id in TargetItemIds:

                while Items.FindByID(item_id, -1, sub_backpack.Serial):
                    target_item = Items.FindByID(
                        item_id, -1, sub_backpack.Serial)

                    if target_item:
                        item_props = Items.GetPropStringList(target_item)
                        is_target = False

                        # PROPERTIES CHECK
                        for item_prop in item_props:
                            Misc.SendMessage(item_prop)
                            # EVAL TARGET PROPERTIES
                            for target_prop in TargetPropertiesRegex:
                                # REGEX
                                if re.search(target_prop, item_prop, flags=re.IGNORECASE):
                                    Misc.Beep()
                                    Misc.SendMessage("MATCH!", 50)
                                    Misc.SendMessage("REGEX:", 60)
                                    Misc.SendMessage(" => " + target_prop, 60)
                                    Misc.SendMessage("PROPS:", 80)
                                    Misc.SendMessage(" => " + item_prop, 80)
                                    is_target = True

                        # TARGET TO KEEP OR TRUSH
                        if is_target:
                            Misc.SendMessage(" => KEEP", 90)
                            MoveItemToBackpack(target_item)
                            is_target = False
                        else:
                            Misc.SendMessage(" => TRUSH")
                            MoveItemToTrush(target_item)

                        Misc.Pause(1000)

                    Misc.Pause(100)

        MoveItemToTrush(sub_backpack)
        Misc.Pause(1000)


def SubBackpackCleanup():
    bag = 0x0E75
    colors = {
        0x0003: "Blue",
        0x000d: "Purple",
        0x0021: "Red",
        0x001c: "Dark Pink",
        0x0037: "Frog Green",
        0x003a: "Uguisu Green",
        0x0044: "Green",
        0x0059: "Light Blue",
        0x0062: "Dark Blue",
        0x0071: "Dark Purple"
    }
    for color in colors:
        while Items.FindByID(bag, color, Player.Backpack.Serial):
            item = Items.FindByID(bag, color, Player.Backpack.Serial)
            MoveItemToTrush(item)


def Questing():

    global hasQuest

    if hasQuest:
        return

    if HasAllQuestItem():
        return

    Misc.SendMessage("QUESTING", 1150)

    while not hasQuest:

        # Talk
        Mobiles.UseMobile(QuestMobileSerial)
        Misc.Pause(100)

        isQuestStarted = Gumps.LastGumpTextExist(
            QuestAlreadyStartedDescription)
        if isQuestStarted:
            Misc.SendMessage("Already have a quest.", 55)
            Gumps.WaitForGump(QuestGumpId, 10000)
            Gumps.SendAction(QuestGumpId, 0)  # Close
            hasQuest = True
            Misc.Pause(500)
            return

        isExactQuest = Gumps.LastGumpTextExist(QuestName)
        Misc.SendMessage("Exact Quest?: %s" % isExactQuest, 55)

        if isExactQuest:
            Gumps.WaitForGump(QuestGumpId, 10000)
            Gumps.SendAction(QuestGumpId, 4)  # Accept
            hasQuest = True
        else:
            Gumps.WaitForGump(QuestGumpId, 10000)
            Gumps.SendAction(QuestGumpId, 2)  # Refuse
            Gumps.WaitForGump(QuestGumpId, 10000)
            Gumps.SendAction(QuestGumpId, 0)  # Close
            hasQuest = False

        Misc.Pause(500)


def Craft():

    global hasQuest

    if not hasQuest:
        return

    if HasAllQuestItem():
        return

    Misc.SendMessage("CRAFTING", 1150)

    count = 0
    while not HasAllQuestItem() and (count < 15):

        tool = Items.FindByID(ToolKitId, 0, Player.Backpack.Serial)
        if not tool:
            Misc.SendMessage("There is no tool!", 33)
            sys.exit()

        Items.UseItem(tool)
        Misc.Pause(1000)

        Gumps.WaitForGump(ToolGumpId, 10000)
        Gumps.SendAction(ToolGumpId, 21)  # Remake
        Misc.Pause(1500)

        count += 1

    Gumps.WaitForGump(ToolGumpId, 10000)
    Gumps.SendAction(ToolGumpId, 0)  # Close
    Misc.Pause(500)


def ReportQuest():

    global hasQuest

    Misc.SendMessage("REPORT QUEST", 1150)

    if HasAllQuestItem():

        Mobiles.UseMobile(QuestMobileSerial)  # Talk
        Misc.Pause(250)

        Gumps.WaitForGump(QuestGumpId, 10000)
        Gumps.SendAction(QuestGumpId, 8)  # Continue
        Gumps.WaitForGump(QuestGumpId, 10000)
        Gumps.SendAction(QuestGumpId, 5)  # Accept

        hasQuest = False
        Misc.Pause(250)


def GetFood(type):

    foods = None

    global Meats

    if type == "meat":
        foods = Meats
    elif type == "fruit":
        foods = Fruits
    else:
        Misc.SendMessage("Unknown food type!", 33)
        sys.exit()

    for food in foods:
        item = Items.FindByID(food, -1, Player.Backpack.Serial)
        if item:
            return item


def FeedPet(pet, type):

    Misc.SendMessage("FEED PET", 1150)

    while True:
        Spells.CastMagery("Create Food")
        Misc.Pause(1000)

        food = GetFood(type)
        if food:
            Items.Move(food, pet, 0)
            Player.HeadMessage(80, "Here you are!")
            Mobiles.Message(pet, 90, "yum-yum..")
            Misc.Pause(500)
            break

    Misc.Pause(500)


def CleanFoods(trush_poach_serial):
    for food in [*Fruits, *Meats, *OtherFoods]:
        item = Items.FindByID(food, -1, Player.Backpack.Serial)
        if item:
            Items.Move(item, trush_poach_serial, 0)
            Misc.Pause(500)


# RUN
# ========================
Warning()


pet = Mobiles.FindBySerial(PackPetSerial)

while True:

    FeedPet(pet, PackPetFoodType)
    CleanFoods(TrushPouch)

    for _ in range(10):

        OrganizeSubBackpackItems()
        SubBackpackCleanup()
        Questing()
        GetItemFromPet(MaterialId, MaterialThreshold, MaterialTakeAmount)
        Craft()
        ReportQuest()

        Misc.Pause(50)
