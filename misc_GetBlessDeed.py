while True:
    Mobiles.UseMobile(0x00003329)
    Gumps.WaitForGump(696412382, 10000)
    Gumps.SendAction(696412382, 299)
    Misc.Pause(100)
    while Gumps.CurrentGump() == 339743370:
        Misc.Pause(100)