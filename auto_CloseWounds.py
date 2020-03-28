while True:
    # Close Wounds
    if Player.Hits < Player.HitsMax * 0.9:
        Spells.CastChivalry("Close Wounds")
        Target.WaitForTarget(2000, False)
        Target.Self()
        
    if not Player.BuffsExist("Momentum Strike") and Player.ManaMax * 0.45 < Player.Mana:
        Spells.CastBushido("Momentum Strike")
        
#    if not Player.BuffsExist("Lightning Strike") and Player.ManaMax * 0.45 < Player.Mana:
#        Spells.CastBushido("Lightning Strike")
        
    
    Misc.Pause(100)
Spells.CastBushido("Momentum Strike")