target = Target.PromptTarget("Eval Target?", 55)

while True:
    Player.UseSkill("Eval Int")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(target)
    Misc.Pause(1000)