hurb_cutter_serial = 0x401F1507

plants = [
    3204, 3205,
    3211, 3212,
    3230, 3239,
    3244, 3245, 3246, 3247, 3248, 3249,
    3250, 3251, 3252, 3253, 3254, 
    3269,
    3271, 3277, 3278,
    3280, 3281, 3283, 3284, 3286, 3287, 3288, 3289,
    3290, 3291, 3293, 3294, 3296, 3297, 3299,
    3300, 3302, 3303, 3304, 3305, 3306, 3315, 3316, 3317, 3318, 3319,
    3391, 3392
]

ignore = [
    3343, 3345, 3347, 3348, 3349, 3373,
    3370, 3373,
    6003, 6004, 6007, 6008,
]

def equipHurbCutter():
    if not Player.CheckLayer("LeftHand"):
        Player.EquipItem(hurb_cutter_serial)
        Misc.Pause(1000)

        
class Tile:
    def __init__(self, x, y, z, map_id, tile):
        self.X = x
        self.Y = y
        self.Z = z
        self.Map = map_id
        self.StaticID = tile.StaticID
        self.StaticHue = tile.StaticHue
        self.StaticZ = tile.StaticZ

while True:
    
    x = Player.Position.X
    y = Player.Position.Y
    z = Player.Position.Z
    map_id = Player.Map
    
    tile_list = []
  
    for tile in Statics.GetStaticsTileInfo(x-1, y-1, map_id):
        tile_list.append(Tile(x-1, y-1, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x-1, y, map_id):
        tile_list.append(Tile(x-1, y, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x-1, y+1, map_id):
        tile_list.append(Tile(x-1, y+1, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x, y-1, map_id):
        tile_list.append(Tile(x, y-1, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x, y, map_id):
        tile_list.append(Tile(x, y, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x, y+1, map_id):
        tile_list.append(Tile(x, y+1, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x+1, y-1, map_id):
        tile_list.append(Tile(x+1, y-1, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x+1, y, map_id):
        tile_list.append(Tile(x+1, y, z, map_id, tile))
    for tile in Statics.GetStaticsTileInfo(x+1, y+1, map_id):
        tile_list.append(Tile(x+1, y+1, z, map_id, tile))
        
 
    for tile in tile_list:
        
        if not x == Player.Position.X and not y == Player.Position.Y:
            break
            
        if tile.StaticID in ignore:
            Misc.SendMessage(tile.StaticID, 3)
            continue
            
        if tile.StaticID in plants:
            Misc.SendMessage(tile.StaticID, 80)
        else:
            Misc.SendMessage(tile.StaticID)
        
        Items.UseItem(hurb_cutter_serial)
        Misc.Pause(200)
        Target.TargetExecute(tile.X, tile.Y ,tile.Z ,tile.StaticID)
        Misc.Pause(1000)

        
    Misc.SendMessage("End")
    Misc.Pause(100)