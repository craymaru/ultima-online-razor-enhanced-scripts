goal_skill_value = Player.GetSkillCap("Chivalry")
goal_skill_value = 103

def meditation():
    
    while Player.Mana < Player.ManaMax *0.5 and not Player.BuffsExist("Meditation"):
        if not Timer.Check("Skill"):
            Player.UseSkill("Meditation")
            Timer.Create("Skill", 10000)
        Misc.Pause(200)
    
    while Player.Mana < Player.ManaMax * 0.9 and Player.BuffsExist("Meditation"):
        Misc.Pause(200)


while True:
    
    if Player.GetRealSkillValue("Chivalry") == goal_skill_value:
        break
    
    meditation()
    
    if 55.0 < Player.GetRealSkillValue("Chivalry"):
        Spells.CastChivalry("Holy Light")
        Misc.Pause(1000)
    elif 45.0 < Player.GetRealSkillValue("Chivalry"):
        Spells.CastChivalry("Enemy Of One")
        Misc.Pause(1000)