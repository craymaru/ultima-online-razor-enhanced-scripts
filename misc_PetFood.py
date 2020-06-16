"""
PetFood

configuration/config.py
food_habit: (0: Carnivorous, 1: Herbivorous, 2: Omnivorous)
"""

from Scripts.config import config


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
    
    def __init__(self, pet_serial, food_habit):
        
        self.pet_serial = pet_serial
        self.foodHabit = food_habit
        self.trush_pouch_serial = None
        self.ate = []
    
        
    def __call__(self, Misc, Player, Mobiles, Items, Spells, Timer):
        

        def getTrushPouch():
            item = Items.FindByID(0x09B0, 0x09c4, Player.Backpack.Serial)
            return item

        def castCreateFood():
            if not Timer.Check("Casting"):
                Spells.CastMagery("Create Food")
                Timer.Create("Casting", 1000)
            
        def giveFood(food):
            if not Timer.Check("MoveItem"):
                Player.HeadMessage(80, "Here you are!")
                Mobiles.Message(self.pet_serial, 90, "yum-yum..")
                Items.Move(food, self.pet_serial, 1)
                Timer.Create("MoveItem", 650)
        
        def feed():
            for foodID, food in foods.items():
                item = Items.FindByID(foodID, 0x0000, Player.Backpack.Serial)
                if item:
                    if food["type"] == self.foodHabit:
                        giveFood(item)
                        self.ate.append(food["type"])
        
        def cleanFoods():
            for food in foods.keys():
                item = Items.FindByID(food, 0x0000, Player.Backpack.Serial)
                if item:
                    while Timer.Check("MoveItem"):
                        Misc.Pause(100)
                    Items.Move(item, self.trush_pouch_serial, 0)
                    Timer.Create("MoveItem", 650)


        if not self.trush_pouch_serial:
            self.trush_pouch_serial = getTrushPouch().Serial

        self.ate = []
        while not self.ate:
            castCreateFood()
            feed()           
            Misc.Pause(100)
        else:
            cleanFoods()
        

        
if __name__ == "<module>":
    #trush_pouch_serial = config.General[Misc.ShardName()][Player.Serial]["trush_pouch_serial"]
    pet_serial = config.PetFood[Misc.ShardName()][Player.Serial]["pet_serial"]
    pet_food_habit = config.PetFood[Misc.ShardName()][Player.Serial]["pet_food_habit"]
    petfood = PetFood(pet_serial, pet_food_habit)
    petfood(Misc, Player, Mobiles, Items, Spells, Timer)