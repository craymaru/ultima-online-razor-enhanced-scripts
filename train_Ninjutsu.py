from AutoComplete import *

from Scripts.lib.skills.meditation import *


def stealth():
    if not Player.BuffsExist("Hiding"):
        Player.UseSkill("Hiding")
        Player.Walk("Up")
        Player.Walk("Up")
        Player.Walk("Down")
        Player.Walk("Down")


def ninjutsu():
    X, Y, Z = Player.Position.X, Player.Position.Y, Player.Position.Z

    pos = Player.Position
    x = Player.Position


    if 50.0 <= Player.GetRealSkillValue("Ninjutsu"):
        Spells.CastNinjitsu("Shadowjump")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(X+1, Y+1, Z)
        Misc.Pause(250)
        Spells.CastNinjitsu("Shadowjump")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(X-1, Y-1, Z)
        Misc.Pause(250)
    elif 25.0 <= Player.GetRealSkillValue("Ninjutsu"):
        if Player.Followers < Player.FollowersMax:
            Spells.CastNinjitsu("Mirror Image")
            Misc.Pause(1000)
        Misc.Pause(100)


def main():
    while True:
        meditation(0.2, 0.9)
        stealth()
        ninjutsu()
        Misc.Pause(100)


main()
