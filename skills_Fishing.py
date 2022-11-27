from Scripts.utils import UItems

RE = {
    "Misc": Misc,
    "Player": Player,
    "Items": Items
}

garbage_list = [
    {"id": 0x09CC, "color": 0x0000, "name": "fish"},
    {"id": 0x09CD, "color": 0x0000, "name": "fish"},
    {"id": 0x09CE, "color": 0x0000, "name": "fish"},
    {"id": 0x09CF, "color": 0x0000, "name": "fish"},
    {"id": 0x0DD6, "color": 0x0033, "name": "prized fish"},
    {"id": 0x0DD6, "color": 0x0042, "name": "highly peculiar fish"},
    {"id": 0x0DD6, "color": 0x004c, "name": "truly rare fish"},
    {"id": 0x0DD6, "color": 0x0056, "name": "wondrous fish"},
    {"id": 0x0D06, "color": 0x0000, "name": "lilypad"},
    {"id": 0x0D07, "color": 0x0000, "name": "lilypad"},
    {"id": 0x0D08, "color": 0x0000, "name": "lilypad"},
    {"id": 0x0D09, "color": 0x0000, "name": "lilypad"},
    {"id": 0x0D0A, "color": 0x0000, "name": "lilypad"},
    {"id": 0x0D0B, "color": 0x0000, "name": "lilypads"},
    {"id": 0x170B, "color": 0x0000, "name": "boots"},
    {"id": 0x170D, "color": 0x0000, "name": "sandals"},
    {"id": 0x170F, "color": 0x0000, "name": "shoes"},
    {"id": 0x1711, "color": 0x0000, "name": "thigh boots"},
    {"id": 0x0DD6, "color": 0x0000, "name": "prize fish"}
]


def getFishingPole():
    item = Items.FindByID(0x0DC0, 0x0000, Player.Backpack.Serial)
    if not item:
        Player.HeadMessage(55, "There is no Fishing Pole!")
    return item


def fishing(pole, point):
    Items.UseItem(pole)
    Misc.Pause(100)
    Target.TargetExecute(point.X, point.Y, point.Z)
    Misc.Pause(9000)
    
    
def trashItems(garbage_list, af_bag):
    for i in garbage_list:
        UItems.moveAllItems(i["id"], i["color"], af_bag, **RE)

# RUN
af_bag = Target.PromptTarget("Trash Bag?")
point = Target.PromptGroundTarget("Fishing?")
pole = getFishingPole()
while True:
    trashItems(garbage_list, af_bag)
    fishing(pole, point)
    