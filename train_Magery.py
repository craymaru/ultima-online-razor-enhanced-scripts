def getSkillValue():
    value = round(Player.GetSkillValue("Magery"), 2)
    Misc.SendMessage("Magery: " + str(value), 55)
    return value

    
def meditation():
    if Player.Mana < (Player.ManaMax * 0.65):
        while Player.Mana < (Player.ManaMax * 0.90):
            if not Player.BuffsExist("Meditation"):
                Player.UseSkill("Meditation")
                Misc.Pause(10000)
            Misc.Pause(50)

def trainMagery(skill_value):
    
    # 8th EARTHQUAKE
    if 80.1 <= skill_value:
        Spells.CastMagery("Earthquake")
        Misc.Pause(3000 - Player.FasterCasting * 250)
    # 7th MANA VAMPIRE
    elif 65.8 <= skill_value:
        Spells.CastMagery("Mana Vampire")
        Target.WaitForTarget(2000, False)
        Target.Self()
    # 6th REVEAL
    elif 51.5 <= skill_value:
        Spells.CastMagery("Reveal")
        Target.WaitForTarget(3000, False)
        Target.Self()
    # 5th MARIC REFLECTION
    elif 37.2 <= skill_value:
        Spells.CastMagery("Magic Reflection")
        Misc.Pause(2000)
    # 4th ARCH CURE
    elif 22.9 <= skill_value:
        Spells.CastMagery("Arch Cure")
        Target.WaitForTarget(2000, False)
        Target.Self()
    # 3th BLESS
    elif 8.6 <= skill_value:
        Spells.CastMagery("Bless")
        Target.WaitForTarget(2000, False)
        Target.Self()
    # 2th STRENGHT
    elif 0.0 <= skill_value:
        Spells.CastMagery("Strength")
        Target.WaitForTarget(2000, False)
        Target.Self()
        
        
    Misc.Pause(50)


while True:
    meditation()
    trainMagery(getSkillValue())
