Misc.SendMessage("PROVPKE_1?", 53)
mobile_serial_1 = Target.PromptTarget()
Misc.SendMessage("PROVPKE_2?", 53)
mobile_serial_2 = Target.PromptTarget()

while True:
    item = Items.FindByID(0x0E9D, -1, Player.Backpack.Serial)
    Items.UseItem(item)
    Misc.Pause(100)
    Player.UseSkill("Provocation")
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(mobile_serial_1)
    Target.WaitForTarget(1000, False)
    Target.TargetExecute(mobile_serial_2)
    for i in range(10):
        Items.UseItem(item)
        Misc.Pause(1000)