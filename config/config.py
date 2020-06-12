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
            "tags": { "account": 1, "slot": 2, "name": "Craymaru"},
            "trush_pouch_serial": 0x4002FD51
        },
        0x00001F80: {
            "tags": { "account": 4, "slot": 3, "name": "Serah"},
            "trush_pouch_serial": None
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
            "tags": { "account": 1, "slot": 2, "name": "Craymaru"},
            "pet_serial": 0x00018ABF,
            "pet_food_habit": "meat"
        }
    }
}

Lumberjacking = {
    "Stygian Lapis":{
        0x0000139C: {
            "tags": { "account": 3, "slot": 2, "name": "Ray"},
            "atlas_serial": 0x405FFFB9, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 33), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        },
        0x00001F80: {
            "tags": { "account": 4, "slot": 3, "name": "Serah"},
            "atlas_serial": 0x405FADE0, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 47), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        }
    }
}