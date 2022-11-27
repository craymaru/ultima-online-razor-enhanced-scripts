from System.Collections.Generic import List
from System import Byte

def attackAll(mobs):
    for mob in mobs:
        Player.Attack(mob)


def taming(mob):
    Player.UseSkill("Animal Taming")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(mob)
    

def findMobsByName(targetName):
    fil = Mobiles.Filter()
    fil.RangeMax = 10
    fil.Notorieties = List[Byte](bytes([3,4]))
    fil.Name = targetName
    mobs = Mobiles.ApplyFilter(fil)
    
    return mobs


def main():
    tick = 500
    target = Target.PromptTarget("Target?", 55)
    name = Mobiles.FindBySerial(target).Name
    
    Misc.SendMessage("Taming: " + name, 66)

    while True:
        mobs = findMobsByName(name)
        attackAll(mobs)
        
        mob = Mobiles.Select(mobs, "Nearest")
        taming(mob)
        
        Misc.Pause(tick)
        
        if Player.GetSkillCap("AnimalTaming") <= Player.GetRealSkillValue("AnimalTaming"):
            Misc.SendMessage(55, "SkillCap!")
            break

        
main()