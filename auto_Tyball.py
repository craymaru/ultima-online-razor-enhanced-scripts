from System.Collections.Generic import List
from System import Byte


def InvisiblePetAttak():
    
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 20
    fil.Notorieties = List[Byte](bytes([3,4,5,6]))
    #Notoriety 1: blue, 3: gray, 6: red, 7: yellow
    enemies = Mobiles.ApplyFilter(fil)
    Mobiles.Select(enemies, 'Nearest')
    
    for enemy in enemies:
        Misc.SendMessage(enemy.Name)
        if enemy.Name == "Lord Tyball's Shadow" or enemy.Name == "Lord Tyball's Shadow":
            if enemy.Hits == enemy.HitsMax:
                if not Player.BuffsExist("Invisibility"):
                    Target.Cancel()
                    Spells.CastMagery("Invisibility")
                    Target.WaitForTarget(3000, False)
                    Target.Self()
                    Misc.Pause(50)
            
                if Player.BuffsExist("Invisibility"):
                    Player.Attack(enemy)
                    Target.ClearLast()
                    Misc.Pause(1000)
                    PeaceMode()
    Misc.Pause(1000)
    
def PeaceMode():
    if Player.WarMode:
        Player.SetWarMode(False)
        
def IsPlayerHealthy():
    while Player.IsGhost:
        Misc.Beep()
        Misc.Pause(1000)
    if Player.Poisoned == True or Player.Hits <= Player.HitsMax * 0.80:
        return False
    else:
        return True
        
def CurePoison():
    while Player.Poisoned and not Player.IsGhost:
        cure_failed = False
        if cure_failed == True:
            Target.Cancel()
            Spells.CastMagery("Arch Cure")
            Target.WaitForTarget(1000, False)
            Target.Self()
        else:
            Target.Cancel()
            Spells.CastMagery("Cure")
            Target.WaitForTarget(1000, False)
            Target.Self()
            cure_failed = Player.Poisoned
        Misc.Pause(50)

def Heal():
    while Player.Hits <= Player.HitsMax * 0.80 and not Player.IsGhost:
        if Player.Hits <= Player.HitsMax * 0.60:
            Target.Cancel()
            Spells.CastMagery("Greater Heal")
            Target.WaitForTarget(3000, False)
            Target.Self()
        else:
            Target.Cancel()
            Spells.CastMagery("Heal")
            Target.WaitForTarget(1000, False)
            Target.Self()
        Misc.Pause(50)

def GiftOfLife():
    if 100 < Player.GetSkillValue("Spell Weaving") and not Player.BuffsExist("Gift Of Life"):
        Target.Cancel()
        Spells.CastSpellweaving("Gift Of Life")
        Target.WaitForTarget(3000, False)
        Target.Self()
        Misc.Pause(50)
        
while True:
    if IsPlayerHealthy():
        PeaceMode()
        GiftOfLife()
        InvisiblePetAttak()
    else:
        CurePoison()
        Heal()