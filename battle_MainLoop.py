from System.Collections.Generic import List
from System import Byte

LastSpmSecondary = False

def consecrateWeapon():
    if Timer.Check("ConsecDelay") or Player.BuffsExist('Consecrate Weapon'): return
        
    if Player.ManaMax * 0.5 < Player.Mana:
        Spells.CastChivalry('Consecrate Weapon')
        Timer.Create("ConsecDelay", 2000)


def divineFury():
    if Timer.Check("DivineDelay") or Player.BuffsExist('Divine Fury'): return
        
    if Player.ManaMax * 0.5 < Player.Mana:
        if Player.Stam < Player.StamMax * 0.90:
            Spells.CastChivalry("Divine Fury")
            Timer.Create("DivineDelay", 2000)


def evasion():
    if Timer.Check("EvasionDelay") or Player.BuffsExist('Evasion'): return
    
    if Player.Hits < Player.HitsMax * 0.5:
        if Player.ManaMax * 0.5 < Player.Mana:
            Spells.CastBushido("Evasion")
            Timer.Create("EvasionDelay", 21000)


def spm():
    isSpmSecondary = Misc.ReadSharedValue("UseSpmSecondary")
    
    global LastSpmSecondary
    
    if (LastSpmSecondary is not isSpmSecondary or not Player.HasSpecial) and Player.ManaMax * 0.5 < Player.Mana:
    
        if isSpmSecondary:
            Player.WeaponSecondarySA()
            LastSpmSecondary = True
        else: 
            Player.WeaponPrimarySA()
            LastSpmSecondary = False
        
    

def honor():
    if Player.BuffsExist('Honored'): return
    
    Target.ClearLast()
    Target.SetLastTargetFromList("honor")
    mob = Mobiles.FindBySerial(Target.GetLast())
    
    if not mob: return
    
    if mob.Hits == mob.HitsMax:
        Player.InvokeVirtue("Honor")
        Target.WaitForTarget(1000, False)
        Target.TargetExecute(mob.Serial)


def attack():
    Target.ClearLast()
    Target.SetLastTargetFromList("enemy_nearest")
    Player.Attack(Target.GetLast())

          

Player.HeadMessage(33, "[War Mode]")

while not Player.IsGhost and not Player.BuffsExist("Hiding"):

    Misc.Pause(100)
    
    honor()
    
    spm()
    
    divineFury()
    consecrateWeapon()
    
    attack()
    
    