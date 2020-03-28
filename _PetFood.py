pet_serial = 0x184EF
trush_poach_serial = 0x4002FD51

# Foods
foods = {
    0x097B: {"name": "fish", "type": "etc"},
    0x097D: {"name": "cheese", "type": "etc"},
    0x09B7: {"name": "chicken", "type": "meat"},
    0x09C0: {"name": "sausage", "type": "meat"},
    0x09C9: {"name": "ham", "type": "meat"},
    0x09D1: {"name": "grape", "type": "fruit"},
    0x09D2: {"name": "peach", "type": "fruit"},
    0x09D0: {"name": "apple", "type": "fruit"},
    0x09EB: {"name": "muffins", "type": "etc"},
    0x09F2: {"name": "ribs", "type": "meat"}
}

def PetFood(pet_serial, trush_poach_serial):
    global ate_meat
    global ate_fruit

    ate_meat = False
    ate_fruit = False

    while ate_meat == False or ate_fruit == False:
        Spells.CastMagery("Create Food")
        Misc.Pause(1000)

        for food_k, food_v in foods.items():
            item = Items.FindByID(food_k, -1, Player.Backpack.Serial)
            if item is not None:
                if food_v["type"] == "meat":
                    Items.Move(item, pet_serial, 0)
                    ate_meat = True
                    Misc.Pause(500)
                elif food_v["type"] == "fruit":
                    Items.Move(item, pet_serial, 0)
                    ate_fruit = True
                    Misc.Pause(500)
                
        for food in foods.keys():
            item = Items.FindByID(food, -1, Player.Backpack.Serial)
            if item is not None:
                Items.Move(item, trush_poach_serial, 0)
                Misc.Pause(500)


PetFood(pet_serial, trush_poach_serial)