# SETTINGS

# ENABLE POSITION CHECK TOOL
enable_pos_checker = False # Default: False

# FISHING
fishing_pole_serial = 0x40114CB8
fishing_times_number = 8


# CLEANUP
enable_cleanup = True # Default: True
cleanup_pouch_serial = 0x4008F56E


pos_tuple = (
    (3499, 2619, -5),
    (3503, 2619, -5),
    (3506, 2619, -5),
)

trushes = {
    "boots": {"id": 0x170B, "color": 0x0000},
    "sandals": {"id": 0x170D, "color": 0x0000},
    "shoes": {"id": 0x170F, "color": 0x0000},
    "thigh boots": {"id": 0x1711, "color": 0x0000},
    "prized fish": {"id": 0x0DD6, "color": 0x0033},
    "highly peculiar fish": {"id": 0x0DD6, "color": 0x0042},
    "wondrous fish": {"id": 0x0DD6, "color": 0x004c},
    "truly rare fish": {"id": 0x0DD6, "color": 0x0056},
}


class Point3d():
    
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        
    def __call__(self):
        return (self.X, self.Y, self.Z)


def init_positions(pos_tuple):
    
    positions = []

    for pos in pos_tuple:
        positions.append(
            Point3d(pos[0], pos[1], pos[2])
        )
    
    return positions


def cleanup(trushes):
    for item_name, item in trushes.items():
        
        item = Items.FindByID(item["id"], item["color"], Player.Backpack.Serial)
        if item:
            Items.Move(item, cleanup_pouch_serial, -1)
            Misc.Pause(700)


def pos_checker():
    pos = Target.PromptGroundTarget()
    Misc.SendMessage(pos, 54)


while enable_pos_checker:
    if not count: count = 0
    Misc.SendMessage(count)
    pos_checker()
    count += 1


def fish(pos):
    Items.UseItem(fishing_pole_serial)
    Target.WaitForTarget(1000, True)
    Target.TargetExecute(pos.X, pos.Y ,pos.Z)
    Misc.Pause(8300)
    
    

positions = init_positions(pos_tuple)

while Player.Weight < Player.MaxWeight:
    
    for pos in positions:
        for i in range(fishing_times_number):
            fish(pos)
            if enable_cleanup: cleanup(trushes) 