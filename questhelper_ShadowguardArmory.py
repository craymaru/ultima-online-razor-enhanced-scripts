from System.Collections.Generic import List
import re


flames_serial = 0x400A1A43

flame = Items.FindBySerial(flames_serial)

phylactery_id = 0x42B4
phylactery_hue = 0x081b



def flameCorrupt(item):
    Items.UseItem(item)
    Misc.Pause(200)
    Target.TargetExecute(flame)
    Misc.Pause(200)

filter = Items.Filter()
filter.Graphics = List[int]((0x42B4))
filter.Hues = 0x081b
filter.OnGround = 0
filter.IsContainer = 1

items = Items.ApplyFilter(filter)

for item in items:
    Misc.SendMessage(item.Name)

#while True:
#    phylactery = Items.FindByID(0x42B4, 0x081b, Player.Backpack.Serial)
#    if phylactery:
#        for prop in phylactery.Properties:
#            Misc.SendMessage(prop)
#            if re.search("Corrupt", str(prop), flags=re.IGNORECASE):
#                Misc.SendMessage(prop)
#                flameCorrupt(phylactery)
#            if re.search("Purified", str(prop), flags=re.IGNORECASE):
#                Misc.SendMessage(prop)
#    Misc.Pause(1000)