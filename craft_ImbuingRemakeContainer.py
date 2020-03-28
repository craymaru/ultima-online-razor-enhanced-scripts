def TargeContainer():
    global container
    Misc.SendMessage("TARGET IMBUING CONTAINER", 53)
    container_serial = Target.PromptTarget()
    container = Items.FindBySerial(container_serial)
    return container

def Imbuing(item, number):
    # ANOTHER TARGET
    Player.UseSkill("Imbuing")
    Misc.Pause(200)
    Gumps.WaitForGump(1697188745, 1000)
    Gumps.SendAction(1697188745, 10008)
    Misc.Pause(200)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(item)
    for i in range(number - 1):
        # REMAKE
        Gumps.WaitForGump(1697188745, 1000)
        Gumps.SendAction(1697188745, 10006)
    
def ImbuingContainer(number):
    for item in container.Contains:
        if item:
            Imbuing(item, number)
            Misc.Pause(1000)

TargeContainer()
ImbuingContainer(1)