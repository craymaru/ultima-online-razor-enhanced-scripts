# IMPORTS
# ========================

import re


# SETTINGS
# ========================

regex_list = {
    ""
}


# DEFINES
# ========================

def TargeContainer():
    global container
    Misc.SendMessage("TARGET EXTRACT CONTAINER", 53)
    container_serial = Target.PromptTarget()
    container = Items.FindBySerial(container_serial)
    return container


def Extract(item):
    Player.UseSkill("Imbuing")
    Gumps.WaitForGump(1697188745, 1000)
    Gumps.SendAction(1697188745, 10010)
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(item)
    Gumps.WaitForGump(2381473795, 1000)
    Gumps.SendAction(2381473795, 1)

def EvalItemProps(item):
    item_props = Items.GetPropStringList(item)
    
    for item_prop in item_props:
        for regex in regex_list:
            if re.search(regex, item_prop, flags=re.IGNORECASE):
                Misc.SendMessage(item_prop, 53)
                return True
    
def Extraction():
    for item in container.Contains:
        if item:
            if EvalItemProps(item):
                Extract(item)
                Misc.Pause(1000)

# RUN
# ========================  

TargeContainer()

while True:
    Extraction()
    Misc.Pause(1000)