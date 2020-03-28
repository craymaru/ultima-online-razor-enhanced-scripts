targets = {
    "Goki_A" : 0x1740A,
    "Goki_B" : 0x17400,
    #"Goki_C" : 0xA990,
    #"Goki_D" : 0xA8D5,
}

for target in targets.values():
    Spells.CastMagery("Greater Heal")
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(target)
    Misc.Pause(4000)