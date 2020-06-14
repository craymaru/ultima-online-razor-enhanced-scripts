steal_item = Target.PromptTarget()
Misc.SendMessage("Which item to steal?")
target = Target.PromptTarget()
Misc.SendMessage("From who?")

while True:
    Items.Move(steal_item, target, 0)
    Misc.Pause(50)
    Player.UseSkill("Stealing")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(steal_item)

    Misc.Pause(10000)
