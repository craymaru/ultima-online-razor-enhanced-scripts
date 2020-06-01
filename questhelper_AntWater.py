from Scripts.glossary.items.pitchers import pitchers
from Scripts.utilities.items import FindItem
from Scripts.glossary.colors import colors

pitcher = FindItem(pitchers["pitcher of water"].itemID, Player.Backpack)

count = Items.BackpackCount(pitchers["pitcher of water"].itemID)

if pitcher:
    for i in range(7):
        Items.UseItem(pitcher)
else:
    Player.HeadMessage(colors["red"], "You don't have 8 %s!" % pitchers["pitcher of water"].name)

Misc.Pause(50)
