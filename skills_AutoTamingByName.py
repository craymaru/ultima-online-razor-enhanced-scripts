from System.Collections.Generic import List
from System import Byte

def TamingByName(target_name):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = 10
    fil.Notorieties = List[Byte](bytes([3,4]))
    enemies = Mobiles.ApplyFilter(fil)
    Mobiles.Select(enemies,'Nearest')
    for enemy in enemies:
        if enemy.Name == target_name:
            Player.Attack(enemy)
            Player.UseSkill("Animal Taming")
            Target.WaitForTarget(3000, False)
            Target.TargetExecute(enemy)
            
while True:
    TamingByName("a Mustang")