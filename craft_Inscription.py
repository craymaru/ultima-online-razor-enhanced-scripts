from AutoComplete import *
from AutoComplete import *

InscriptionGump = 2066278152
ReCreate = 21
ScribesPen = 0x0FBF


def checkNotHaveEnough():
    if Gumps.LastGumpTextExist("You do not have enough"):
        Misc.SendMessage("Item not enough!")
        end()


def getPenCharges(pen):
    return int(str(pen.Properties[1]).split(": ")[1])


def meditation():
    if Player.Mana < Player.ManaMax * 0.5:
        while True:
            if not Player.BuffsExist("Meditation"):
                Player.UseSkill("Meditation")
                Player.HeadMessage(111, "*Meditation*")
                Misc.Pause(1000)
            if Player.ManaMax * 0.9 < Player.Mana:
                break
            Misc.Pause(1000)


def main():
    while True:

        pen = Items.FindByID(ScribesPen, 0, Player.Backpack.Serial)

        if not pen:
            break

        Items.UseItem(pen)

        while True:

            pen = Items.FindBySerial(pen.Serial)
            if not pen:
                break

            charges = getPenCharges(pen)
            if not charges:
                break

            Gumps.WaitForGump(InscriptionGump, 3000)
            checkNotHaveEnough()
            meditation()

            Gumps.SendAction(InscriptionGump, ReCreate)

            Misc.Pause(100)

        Misc.Pause(100)

    Misc.SendMessage("Done!")


main()
