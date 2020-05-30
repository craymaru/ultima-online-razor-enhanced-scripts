from Scripts.glossary.items.tools import tools
from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors

scissors = FindItem( tools["scissors"].itemID, Player.Backpack )

if scissors:
    Items.UseItem(scissors)
else:
    Player.HeadMessage(colors["red"], "You don't have %s!" % tools["scissors"].name)

Misc.Pause(50)
