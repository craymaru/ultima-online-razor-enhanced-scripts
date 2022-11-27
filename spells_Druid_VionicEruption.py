
pos = Target.PromptGroundTarget("Vionic Eruption")
while True:
    Player.ChatSay(28, "[D8")
    Target.WaitForTarget(1000, True)
    Target.TargetExecute(pos.X, pos.Y, pos.Z)