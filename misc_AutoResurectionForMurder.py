
while True:
    if Player.IsGhost:
        Items.UseItem(0x400313D1)
        Misc.Pause(200)
        Gumps.WaitForGump(2957810225, 10000)
        Gumps.SendAction(2957810225, 1)
    else:
        Player.UseSkill("Spirit Speak")
        Misc.Pause(1000)