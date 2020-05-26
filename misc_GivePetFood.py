"""
GivePetFood

configuration/config.py
food_habit: (0: Carnivorous, 1: Herbivorous, 2: Omnivorous)
"""

from Scripts.configuration import config

trush_poach_serial = config.General[Player.Serial]["trush_poach_serial"]


# ITEM_ID: Foods
# ===============================
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


class PetFood:
    
    def __init__(self, pet_serial, food_habit, trush_poach_serial):
        
        self.pet_serial = pet_serial
        self.food_habit = food_habit
        self.trush_poach_serial = trush_poach_serial
    
    def __call__(self):
        
        ate_meat = False
        ate_fruit = False
        
        if self.food_habit == 0:
            ate_fruit = True
            
        if self.food_habit == 1:
            ate_meat = True
            

        while ate_meat == False or ate_fruit == False:
            Spells.CastMagery("Create Food")
            Misc.Pause(1000)

            for food_k, food_v in foods.items():
                item = Items.FindByID(food_k, -1, Player.Backpack.Serial)
                if item:
                    if food_v["type"] == "meat" or food_v["type"] == "fruit":
                        Target.Cancel()
                        Misc.Pause(50)
                        Items.Move(item, self.pet_serial, 0)
                        if food_v["type"] == "meat":
                            ate_meat = True
                            Misc.SendMessage()
                        if food_v["type"] == "fruit":
                            ate_fruit = True
                        Misc.Pause(500)
                    
            for food in foods.keys():
                item = Items.FindByID(food, -1, Player.Backpack.Serial)
                if item:
                    Target.Cancel()
                    Misc.Pause(50)
                    Items.Move(item, self.trush_poach_serial, 0)
                    Misc.Pause(500)
                    
        Misc.Pause(1000)


        
if __name__ == "<module>":
    Misc.SendMessage(__name__)
    pet_serial = config.SomeExecute[Player.Serial]["pet_serial"]
    petfood = PetFood(pet_serial, "test", trush_poach_serial)
    petfood()