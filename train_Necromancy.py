def getSkillValue():
    value = round(Player.GetSkillValue("Necromancy"), 2)
    Misc.SendMessage("Necromancy " + str(value), 10)
    return value


def heal():
    if Player.Hits < (Player.HitsMax * 0.85):
        while Player.Hits < (Player.HitsMax * 0.95):
            Spells.CastMagery("Greater Heal")
            Target.WaitForTarget(3000, False)
            Target.Self()
            Misc.Pause(1000)

def spin():
    for d in ["South", "Left", "West", "Up", "North", "Right", "East", "Down"]:
        Player.Walk(d)


def Meditation():
    if Player.Mana < (Player.ManaMax * 0.65):
        while Player.Mana < (Player.ManaMax * 0.90):
            spin()
            Spells.CastNecro("Poison Strike")
            Target.WaitForTarget(3000, False)
            Target.Self()
#            if not Player.BuffsExist("Meditation"):
#                success_rate = ((Player.GetSkillValue("Meditation") / 200) + (Player.Mana / Player.ManaMax)) * 100
#                Misc.SendMessage("Success Rate: %s" % success_rate, 40)
#                Player.UseSkill("Meditation")
#                Misc.Pause(10000)
#            Misc.Pause(50)


def trainNecromancy(skill_value):
    # NECROMANCY
    if (Player.ManaMax * 0.6) < Player.Mana:
        
        # VAMPIRIC EMBRACE
        if 99.0 <= skill_value:
            Spells.CastNecro("Vampiric Embrace")
            Misc.Pause(3000)
            
        # LICH FORM
        elif 70.0 <= skill_value:
            Spells.CastNecro("Lich Form")
            Misc.Pause(1000 - int(Player.FasterCasting * 0.25))
        
        # POISON STRIKE
        elif 60.0 <= skill_value:
            Spells.CastNecro("Poison Strike")
            Target.WaitForTarget(3000, False)
            Target.Self()
            
        # SUMMON FAMILIAR
        elif 30.0 <= skill_value:
            Spells.CastNecro("Summon Familiar")
#            if 50.0 < Player.GetSkillValue("Spirit Speak"):
#                Gumps.WaitForGump(545409390, 10000)
#                Gumps.SendAction(545409390, 2)
            Misc.Pause(2000)
            
        # CORPSE SKIN
        elif 20.0 <= skill_value:
            Spells.CastNecro("Corpse Skin")
            Target.WaitForTarget(3000, False)
            Target.Self()
            
        # CURSE WEAPON
        elif 0.0 <= skill_value:
            Spells.CastNecro("Curse Weapon")
            Misc.Pause(1000)
            
        Misc.Pause(10)

# RUN
while True:
    #heal()
    Meditation()
    trainNecromancy(getSkillValue())
