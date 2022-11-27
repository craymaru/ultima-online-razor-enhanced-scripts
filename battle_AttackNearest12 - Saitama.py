from System.Collections.Generic import List
from System import Byte

from Scripts.utils import Utils

def consecrateWeapon():
    #if not Player.BuffsExist("Consecrate Weapon"):
    if not Timer.Check("Consecrate Weapon"):
        Spells.CastChivalry("Consecrate Weapon")
        Timer.Create("Consecrate Weapon", 5000)

        
def divineFury():
    if Player.Stam < Player.StamMax * 0.95:
        Spells.CastChivalry("Divine Fury")

        
def enemyOfOne():
    if not Player.BuffsExist("Enemy Of One"):
        Spells.CastChivalry("Enemy Of One")
        
        
def bless():
    if not Player.BuffsExist("Bless") and not Timer.Check("Bless"):
        Timer.Create("Bless", 20000)
        for spell in ["Strength", "Agility", "Cunning", "Bless"]:
            Spells.CastMagery(spell)
            Target.WaitForTarget(2000, True)
            Target.Self()
            Misc.Pause(Utils.getCRDelayOfMagery(6))

        
def attackNearest():
    filter = Mobiles.Filter()
    filter.RangeMax = 16
    filter.Notorieties = List[Byte](bytes([3,4,5,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies, "Nearest")
    if enemy:
        if not Player.HasSpecial and Player.ManaMax * 0.5 < Player.Mana:
            Player.WeaponPrimarySA()
            
        consecrateWeapon()
        
        Player.Attack(enemy)
        Target.ClearLast()

        
def honorNearest():
    if not Player.BuffsExist('Honored'):
        filter = Mobiles.Filter()
        #filter.Enabled = True
        filter.RangeMax = 10
        filter.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemies = Mobiles.ApplyFilter(filter)
        enemy = Mobiles.Select(enemies,'Nearest')
        if enemy:
            if enemy.Hits == enemy.HitsMax:
                Player.InvokeVirtue("Honor")
                Target.WaitForTarget(1000, True)
                Target.TargetExecute(enemy.Serial)
        
# Run
Player.HeadMessage(33, "[War Mode]")
while not Player.IsGhost:
    bless()
    divineFury()
    #enemyOfOne()
    honorNearest()
    attackNearest()
    
    Misc.Pause(25)