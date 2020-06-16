
targets = []

for i in range(1,3):
    Player.HeadMessage(54, "Target " + str(i))
    targets.append(Target.PromptGroundTarget())
    Player.HeadMessage(90, str(targets[i-1]))


while True:
    for target in targets:
        Spells.CastSpellweaving("Wildfire")
        Target.WaitForTarget(3000, False)
        Target.TargetExecute(target.X, target.Y, target.Z)