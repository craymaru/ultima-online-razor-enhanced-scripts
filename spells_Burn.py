from System.Collections.Generic import List
from System import Byte


def findNearestMobile():
    # FIND NEAREST MOBILE
    
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 10
    filter.Notorieties = List[Byte](bytes([3,4,5,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    mobiles = Mobiles.ApplyFilter(filter)
    mobile = Mobiles.Select(mobiles, 'Nearest')
    return mobile

    
def castArcaneEmpowerment():
    # CAST ARCANE EMPOWERMENT
    if not Player.BuffsExist("Arcane Enpowerment"):
        Spells.CastSpellweaving("Arcane Empowerment")
        Misc.Pause(100)


def castCorpseSkin(mobile):
    # CAST CORPSE SKIN
    Misc.Pause(500)
    if not Timer.Check("Corpse Skin"):
        Spells.CastNecro("Corpse Skin")
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(mobile)
        Timer.Create("Corpse Skin", 10000)

    
def castWildfire(mobile):
    # CAST WILDFIRE
    Spells.CastSpellweaving("Wildfire")
    Target.WaitForTarget(3000, False)
    Target.TargetExecute(mobile)


def castWordOfDeath(mobile):
    # CAST WORD OF DEATH
    Spells.CastSpellweaving("Word Of Death")
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(mobile)
    
    
while True:
    
    if Player.ManaMax *0.35 <= Player.Mana:
        castArcaneEmpowerment()
        
        mobile = findNearestMobile()
        
        if mobile:
            if mobile.Hits <= mobile.HitsMax * 0.3:
                castWordOfDeath(mobile)
            else:
                castCorpseSkin(mobile)
                castWildfire(mobile)
        else:
            Misc.Pause(200)
    else:
        Misc.Pause(200)