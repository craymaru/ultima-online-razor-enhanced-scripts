from System.Collections.Generic import List

axe_dic = {
    0x0F43: "hatchet",
    0x0F47: "battle axe",
    0x1443: "two handed axe"
}

def getAxe():
    # Find lefthand
    hand_item = Player.GetItemOnLayer("LeftHand")
    if hand_item:
        if hand_item.ItemID in axe_dic:
            return hand_item
    # Find backpack
    for axe_id in axe_dic:
        item = Items.FindByID(axe_id, -1, Player.Backpack.Serial)
        if item:
            return item


def equipAxe(axe):
    # Unequip
    for layer in ["RightHand", "LeftHand"]:
        if Player.CheckLayer(layer):
            if Player.GetItemOnLayer(layer).ItemID in axe_dic:
                return
            Player.UnEquipItemByLayer(layer)
            Misc.Pause(550)
    # Equip axe
    Player.EquipItem(axe)
    Misc.Pause(550)



target = Target.PromptGroundTarget("Tree?")
tiles = Statics.GetStaticsTileInfo(target.X, target.Y, Player.Map)
tree = tiles[1]
while True:
    axe = getAxe()
    if not axe:
        break
    equipAxe(axe)
    Items.UseItem(axe)
    Misc.Pause(100)
    Target.TargetExecute(target.X, target.Y, tree.StaticZ, tree.StaticID)
    Misc.Pause(1000)