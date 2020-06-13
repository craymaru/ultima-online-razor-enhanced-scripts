from System.Collections.Generic import List
from System import Byte


def consecrateWep():
    if not Player.BuffsExist('Consecrate Weapon'):
        Spells.CastChivalry('Consecrate Weapon')
        Misc.Pause(500)
    
def attack(filter):
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 6
    filter.Notorieties = List[Byte](bytes([3,4,5,6])) #1:cyan 2:green 3:gray 4:criminal 5:orange 6:red 7:yellow
    enemies = Mobiles.ApplyFilter(filter)
    enemy = Mobiles.Select(enemies, "Nearest")
    if enemy:
        if not Player.HasSpecial and Player.ManaMax * 0.5 < Player.Mana:
            Player.WeaponPrimarySA()
            
        consecrateWep()
        
        Player.Attack(enemy)
        Target.ClearLast()

        
def honorNearest():
    if not Player.BuffsExist('Honored'):
        honfil = Mobiles.Filter()
        honfil.Enabled = True
        honfil.RangeMax = 8
        honfil.Notorieties = List[Byte](bytes([3,4,5,6]))
        enemies = Mobiles.ApplyFilter(honfil)
        Misc.Pause(200)
        enemy = Mobiles.Select(enemies,'Nearest')
        if enemy:
            if enemy.Hits == enemy.HitsMax:
                Player.InvokeVirtue("Honor")
                Target.WaitForTarget(1000, True)
                Target.TargetExecute(enemy.Serial)
        
        
Player.HeadMessage(33, "[War Mode]")

while not Player.IsGhost:
    honorNearest()
    attack(filter)
    
    Misc.Pause(200)