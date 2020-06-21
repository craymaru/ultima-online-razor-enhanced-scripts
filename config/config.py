# Change depending on the latency to your UO shard
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200
dragDelayMilliseconds = 700

General = {
    "Stygian Lapis":{
        0x0000C8EC: {
            "tags": { "account": 1, "slot": 1, "name": "Cray"},
            "trush_pouch_serial": 0x4005DDD8
        },
        0x00017FAB: {
            "tags": { "account": 2, "slot": 2, "name": "Craymaru"},
            "trush_pouch_serial": 0x4002FD51
        },
        0x00001F80: {
            "tags": { "account": 4, "slot": 3, "name": "Serah"}
        },
        0x000088A2: {
            "tags": { "account": 5, "slot": 1, "name": "Cid"}
        },
        0x00009255: {
            "tags": { "account": 6, "slot": 1, "name": "Rogan"}
        },
        0x0000940A: {
            "tags": { "account": 7, "slot": 1, "name": "Raine"}
        },
        0x0000947F: {
            "tags": { "account": 8, "slot": 1, "name": "Serah"}
        }
    }
}

PetFood = {
    "Stygian Lapis":{
        0x00017FAB: {
            "tags": { "account": 1, "slot": 2, "name": "Craymaru"},
            "pet_serial": 0x00018ABF,
            "pet_food_habit": "meat"
        }
    }
}

Mining = {
    "Stygian Lapis":{
        0x00017FAB: {
            "tags": { "account": 2, "slot": 2, "name": "Craymaru"},
            "footing": False, # Digging underfoot in the mine
            "container_serial": 0x400CA97E,
            "mini_ore_organize_bag": 0x4002B142,
            "runic_atlas_serial": 0x400E6EB7,
            "bank_rune": 47,
            "runes": range(0, 46),
            "position_offset_x": -1,
            "position_offset_y": 0,
            "pet_serial": 0x00018ABF,
            "pet_food_habit": "meat"
        },
        0x000088A2: {
            "tags": { "account": 5, "slot": 1, "name": "Cid"},
            "footing": False, # Digging underfoot in the mine
            "container_serial": 0x400CA97E,
            "mini_ore_organize_bag": 0x4012E2FB,
            "runic_atlas_serial": 0x400E6E91,
            "bank_rune": 47,
            "runes": range(0, 46),
            "position_offset_x": -1,
            "position_offset_y": 0,
            "pet_serial": 0x00014FA8,
            "pet_food_habit": "meat"
        },
        0x00009255: {
            "tags": { "account": 6, "slot": 1, "name": "Rogan"},
            "footing": False, # Digging underfoot in the mine
            "container_serial": 0x400CA97E,
            "mini_ore_organize_bag": 0x40063F5A,
            "runic_atlas_serial": 0x40046B51,
            "bank_rune": 0,
            "runes": range(1, 47),
            "position_offset_x": 0,
            "position_offset_y": -1,
            "pet_serial": 0x00014FD2,
            "pet_food_habit": "meat"
        },
        0x0000940A: {
            "tags": { "account": 7, "slot": 1, "name": "Raine"},
            "footing": True, # Digging underfoot in the mine
            "container_serial": 0x400CA97E,
            "mini_ore_organize_bag": 0x401406ED,
            "runic_atlas_serial": 0x4017F7A6,
            "bank_rune": 47,
            "runes": range(0, 46),
            "position_offset_x": -1,
            "position_offset_y": 0,
            "pet_serial": 0x00014FE3,
            "pet_food_habit": "meat"
        }
    }
}

Lumberjacking = {
    "Stygian Lapis":{
        0x00011BF8: {
            "tags": { "account": 1, "slot": 2, "name": "Cray"},
            "container_serial": None,
            "atlas_serial": 0x405FCFCC, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 44), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        },
        0x0000139C: {
            "tags": { "account": 3, "slot": 2, "name": "Ray"},
            "container_serial": None,
            "atlas_serial": 0x405FFFB9, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 33), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        },
        0x00001F80: {
            "tags": { "account": 4, "slot": 3, "name": "Serah"},
            "container_serial": None,
            "atlas_serial": 0x405FADE0, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 47), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        },
        0x0000947F: {
            "tags": { "account": 8, "slot": 1, "name": "Serah"},
            "container_serial": 0x400CA9A3,
            "atlas_serial": 0x400E6ECA, # your Runic-Atlas
            "bank_rune": 47, # Bank rune should be first of the Runic-Atlas
            "runes": range(0, 46), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        }
    }
}