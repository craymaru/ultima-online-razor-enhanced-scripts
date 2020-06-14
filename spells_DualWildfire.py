
targets = []

for i in range(1,3):
    Misc.SendMessage("Target " + str(i), 54)
    targets.append(Target.PromptGroundTarget())


while True:
    for target in targets:
        Spells.CastSpellweaving("Wildfire")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(target.X, target.Y, target.Z)