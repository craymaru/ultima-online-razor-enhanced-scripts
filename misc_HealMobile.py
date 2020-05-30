Misc.SendMessage("MOBILE?", 53)
target_serial = Target.PromptTarget()


def cure(target_serial):
    Spells.CastMagery("Cure")
    Target.WaitForTarget(5000, False)
    Target.TargetExecute(target_serial)


def heal(target_serial):
    mobile = Mobiles.FindBySerial(target_serial)
    while mobile.Poisoned:
        cure(target_serial)
    if mobile.Hits < mobile.HitsMax * 0.85 and not mobile.Poisoned:
        Spells.CastMagery("Greater Heal")
        Target.WaitForTarget(5000, False)
        Target.TargetExecute(target_serial)

while True:
    heal(target_serial)
    Misc.Pause(1000)