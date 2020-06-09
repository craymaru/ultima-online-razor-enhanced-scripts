while True:
    if 10 < Player.Mana and not Player.BuffsExist("Momentum Strike"):
        Spells.CastBushido("Momentum Strike")
    Misc.Pause(100)