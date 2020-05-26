import re
import time

#linelist = Gumps.LastGumpGetLineList()

#for index, line in enumerate(linelist):
#    if index in range(55,80):
#        Misc.SendMessage(str(index)+ ": " + line)

class SuperMobile:
    def __init__(self, mobile):
        self.mobile = mobile
        self.Name = mobile.Name
        self.Body = mobile.Body
        self.Color = mobile.Color
        self.Notoriety = mobile.Notoriety
    
    def get_registances(self):
        linelist = Gumps.LastGumpGetLineList()
        regex = re.compile(r"\d+%")
        for index, line in enumerate(linelist):
            if index == 70:
                match_obj = regex.search(line)
                self.Physical = match_obj.group()
            if index == 71:
                match_obj = regex.search(line)
                self.Fire = match_obj.group()
            if index == 72:
                match_obj = regex.search(line)
                self.Cold = match_obj.group()
            if index == 73:
                match_obj = regex.search(line)
                self.Poison = match_obj.group()
            if index == 74:
                match_obj = regex.search(line)
                self.Energy = match_obj.group()

mobile_serial = Target.PromptTarget()
mobile = Mobiles.FindBySerial(mobile_serial)
Player.UseSkill("Animal Lore")
Target.WaitForTarget(500, False)
Target.TargetExecute(mobile)
Misc.Pause(1500)
mobile = SuperMobile(mobile)
mobile.get_registances()


Misc.SendMessage("--- Propaties ----------")
Misc.SendMessage("  <Name> " + mobile.Name)
Misc.SendMessage("　   <Body> " + str(mobile.Body))
Misc.SendMessage("　   <Color> " + str(mobile.Color), mobile.Color)

Misc.SendMessage("--- Registances --------")
Misc.SendMessage(" <Physical> " + mobile.Physical, 0)
Misc.SendMessage("    <Fire> " + mobile.Fire, 38)
Misc.SendMessage("    <Cold> " + mobile.Cold, 89)
Misc.SendMessage("  <Poison> " + mobile.Poison, 63)
Misc.SendMessage("  <Energy> " + mobile.Energy, 14)