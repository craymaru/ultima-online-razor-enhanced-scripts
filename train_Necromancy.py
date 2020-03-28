def IsSkillValue():
    global skill_value
    skill_value = Player.GetSkillValue("Necromancy")
    text = "Necromancy " + str(skill_value)
    Misc.SendMessage(text, 10)

def Meditation():
    if Player.Mana < (Player.ManaMax * 0.65):
        while Player.Mana < (Player.ManaMax * 0.90):
            if not Player.BuffsExist("Meditation"):
                success_rate = ((Player.GetSkillValue("Meditation") / 200) + (Player.Mana / Player.ManaMax)) * 100
                Misc.SendMessage("Success Rate: %s" % success_rate, 40)
                Player.UseSkill("Meditation")
                Misc.Pause(10000)
            Misc.Pause(50)

def TrainNecromancy():
    # NECROMANCY
    if (Player.ManaMax * 0.6) < Player.Mana:
        
        # VAMPIRIC EMBRACE
        if 99.0 <= skill_value:
            Spells.CastNecro("Vampiric Embrace")
            Misc.Pause(3000)
            
        # LICH FORM
        elif 70.0 <= skill_value:
            Spells.CastNecro("Lich Form")
            Misc.Pause(3000)
        
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
            
        Misc.Pause(50)

# RUN
while True:
    IsSkillValue()
    Meditation()
    TrainNecromancy()
