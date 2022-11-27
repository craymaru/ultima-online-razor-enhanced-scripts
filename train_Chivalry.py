CR = 6

from lib.skills import *


goal_skill_value = Player.GetSkillCap("Chivalry")



while True:
    
    if Player.GetRealSkillValue("Chivalry") == goal_skill_value:
        break
    
    meditation()
    
    if 55.0 < Player.GetRealSkillValue("Chivalry"):
        Spells.CastChivalry("Holy Light")
        Misc.Pause(2500 - (CR * 250))
    elif 45.0 < Player.GetRealSkillValue("Chivalry"):
        Spells.CastChivalry("Enemy Of One")
        Misc.Pause(2000 - (CR * 250))
    elif 25.0 < Player.GetRealSkillValue("Chivalry"):
        Spells.CastChivalry("Divine Fury")
        Misc.Pause(2000 - (CR * 250))