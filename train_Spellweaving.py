# IMPORT
from System.Collections.Generic import List
from System import Byte

def IsSkillValue():
    global skill_value
    skill_value = Player.GetSkillValue("Spell Weaving")
    text = "Spellweaving " + str(skill_value)
    Misc.SendMessage(text)
    

def Meditation():
    if Player.Mana < (Player.ManaMax * 0.65):
        while Player.Mana < (Player.ManaMax * 0.90):
            if not Player.BuffsExist("Meditation"):
                Player.UseSkill("Meditation")
                Misc.Pause(10000)
            Misc.Pause(50)

            
def TrainSpellweaving():
    
    # WORD OF DEATH
    if 97 <= skill_value:
        filter = Mobiles.Filter()
        filter.Enabled = True
        filter.RangeMax = 3
        filter.Notorieties = List[Byte](bytes([3,4]))

        Player.SetWarMode(False)
        enemies = Mobiles.ApplyFilter(filter)
        Mobiles.Select(enemies, 'Nearest')
        target = enemies[0]
        Spells.CastSpellweaving("Word Of Death")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(target)
        
    # WILDFIRE
    elif 66 <= skill_value:
        Spells.CastSpellweaving("Wildfire")
        Target.WaitForTarget(3000, False)
        Target.Self()
    
    # ESSENCE OF WIND
    elif 52 <= skill_value:
        Spells.CastSpellweaving("Essence Of Wind")
        Misc.Pause(2500)
    # REAPER FORM
    elif 45 <= skill_value:
        Spells.CastSpellweaving("Reaper Form")
        Misc.Pause(2000)
        
    # THUNDERSTORM
    elif 10 <= skill_value:
        Spells.CastSpellweaving("Thunderstorm")
        Misc.Pause(1000)
        
    # NATURE'S FURY
    elif 0 <= skill_value:
        x = Player.Position.X + 1
        y = Player.Position.Y + 1
        z = Player.Position.Z
        Spells.CastSpellweaving("Natures Fury")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(x, y, z)
    
    Misc.Pause(50)

while True:
    IsSkillValue()
    Meditation()
    TrainSpellweaving()
