from AutoComplete import *


def meditation(start=0.5, end=0.9):
    if Player.Mana < Player.ManaMax * start:
        while True:
            if not Player.BuffsExist("Meditation"):
                Player.UseSkill("Meditation")
                Player.HeadMessage(111, "*Meditation*")
                Misc.Pause(1000)
            if Player.ManaMax * end < Player.Mana:
                break
            Misc.Pause(1000)


def main():
    meditation()


if __name__ == "__main__":
    main()
