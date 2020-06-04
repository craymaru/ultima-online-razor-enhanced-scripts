from System.Collections.Generic import List
from System import Byte



def filterBarracoon():
    # FILTER BARRACOON
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 10
    filter.Name = "Barracoon"
    filter.Notorieties = List[Byte](bytes([6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    return filter
    

def findNearestMobile(filter):
    # FIND NEAREST MOBILE
    mobiles = Mobiles.ApplyFilter(filter)
    mobile = Mobiles.Select(mobiles, 'Nearest')
    return mobile


def castThunderStorm():
    # CAST THUNDERSTORM
    Spells.CastSpellweaving("Thunderstorm")
    Misc.Pause(100)

    
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
        Timer.Create("Corpse Skin", 20000)

    
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
    

def filterSkull():
    # FILTER SKULL
    filter = Items.Filter()
    filter.Graphics = List[int]([0x1F18])
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = 5
    return filter


def activateChampion(filter):
    # ACTIVATE IDOL OF CHAMPION
    skulls = Items.ApplyFilter(filter)
    skull = Items.Select(skulls, "Nearest")
    # Use Valor to Skull
    if skull:
        Player.InvokeVirtue("Valor")
        Misc.Pause(200)
        Target.TargetExecute(skull)

        
def filterPentagram():
    # FILTER PENTAGRAM
    filter = Items.Filter()
    filter.Graphics = List[int]([0x0FEA])
    filter.Hues = List[int]([0x0455])
    filter.OnGround = True
    filter.Movable = False
    filter.RangeMax = 10
    return filter


def isExistPentagram(filter):
    # FIND PENTAGRAM
    items = Items.ApplyFilter(filter)
    item = Items.Select(items, "Nearest")
    if item:
        return True
    else:
        return False

# FILTER INSTANCES
barracoonFilter = filterBarracoon()
skullFilter = filterSkull()
pentagramFilter = filterPentagram()

while True:
    
    castArcaneEmpowerment()
    
    barracoon = findNearestMobile(barracoonFilter)
    if barracoon:
        if barracoon.Hits <= barracoon.HitsMax * 0.3:
            castWordOfDeath(barracoon)
        else:
            castCorpseSkin(barracoon)
            castWildfire(barracoon)
    else:
        castThunderStorm()
        
    if isExistPentagram(pentagramFilter):
        activateChampion(skullFilter)