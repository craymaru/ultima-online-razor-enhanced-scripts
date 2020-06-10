# Change depending on the latency to your UO shard
journalEntryDelayMilliseconds = 200
targetClearDelayMilliseconds = 200
dragDelayMilliseconds = 700

General = {
    "Stygian Lapis":{
        0x0000C8EC: {
            "tags": "1-1_Craymaru",
            "trush_pouch_serial": 0x4005DDD8
        },
        0x00017FAB: {
            "tag": "1-2_Craymaru",
            "trush_pouch_serial": 0x4002FD51
        },
        0x00001F80: {
            "tag": "4-3_Serah",
            "trush_pouch_serial": None
        }
    }
}

PetFood = {
    "Stygian Lapis":{
        0x00017FAB: {
            "tag": "1-2_Craymaru",
            "pet_serial": 0x00018ABF,
            "pet_food_habit": "meat"
        }
    }
}

Mining = {
    "Stygian Lapis":{
        0x00017FAB: {
            "tag": "1-2_Craymaru",
            "pet_serial": 0x00018ABF,
            "pet_food_habit": "meat"
        }
    }
}

Lumberjacking = {
    "Stygian Lapis":{
        0x0000139C: {
            "tag": "3-2 Ray",
            "atlas_serial": 0x405FFFB9, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 33), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        },
        0x00001F80: {
            "tag": "4-3_Serah",
            "atlas_serial": 0x405FADE0, # your Runic-Atlas
            "bank_rune": 0, # Bank rune should be first of the Runic-Atlas
            "runes": range(1, 47), # How many runes are in the Runic-Atlas
            "position_offset_x": -1, # Tree pos from the your character pos
            "position_offset_y":  0
        }
    }
}