while True:
    Spells.CastLastSpell()
    Target.WaitForTarget(2000, False)
    Target.Last()