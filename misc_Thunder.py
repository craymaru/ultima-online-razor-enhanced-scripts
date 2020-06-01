from System.Collections.Generic import List
from System import Byte


filter = Mobiles.Filter()
filter.Enabled = True
filter.RangeMax = 10
filter.Name = "Barracoon"
filter.Notorieties = List[Byte](bytes([6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow

    

def findNearestMobile(filter):
    
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies, 'Nearest')
    return enemy


def castThunderStorm():
    Spells.CastSpellweaving("Thunderstorm")
    Misc.Pause(100)

    
def castArcaneEmpowerment():
    if not Player.BuffsExist("Arcane Enpowerment"):
        Spells.CastSpellweaving("Arcane Empowerment")
        Misc.Pause(100)


def castCorpseSkin(mobile):
    Misc.Pause(500)
    if not Timer.Check("Corpse Skin"):
        Spells.CastNecro("Corpse Skin")
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(mobile)
        Timer.Create("Corpse Skin", 20000)

    
def castWildfire(mobile):
    Spells.CastSpellweaving("Wildfire")
    Target.WaitForTarget(3000, False)
    Target.TargetExecute(mobile)


def castWordOfDeath(mobile):
    Spells.CastSpellweaving("Word Of Death")
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(mobile)
    
##TEST
#target = Target.PromptTarget()
#mobile = Mobiles.FindBySerial(target)
#Misc.SendMessage(mobile.Hits)
##
    
while True:
    
    castArcaneEmpowerment()
    
    mobile = findNearestMobile(filter)
    if mobile:
        if mobile.Hits <= mobile.HitsMax * 0.4:
            castWordOfDeath(mobile)
        else:
            castCorpseSkin(mobile)
            castWildfire(mobile)
    else:
        castThunderStorm()
