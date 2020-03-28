from System.Collections.Generic import List
from System import Byte

pet_serial = 0x000169D5
trush_poach_serial = 0x40051021

def Invisibility():
    if not Player.BuffsExist("Invisibility"):
        Target.Cancel()
        Spells.CastMagery("Invisibility")
        Target.WaitForTarget(3000, False)
        Target.Self()
    if Player.WarMode:
        Player.SetWarMode(False)
    Misc.Pause(100)

def PetFood(pet_serial, trush_poach_serial):
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
    
    if Timer.Check("PetFoodClock"):
        return
    else:
        Timer.Create("PetFoodClock", 60000)
    
    global ate_meat

    ate_meat = False

    Misc.SendMessage("PETFOOD", 1150)
    Misc.SendMessage("==============", 1150)
    
    while ate_meat == False:
        Spells.CastMagery("Create Food")
        Misc.Pause(1000)

        for food_k, food_v in foods.items():
            item = Items.FindByID(food_k, -1, Player.Backpack.Serial)
            if item is not None:
                if food_v["type"] == "meat":
                    Target.Cancel()
                    Misc.Pause(50)
                    Items.Move(item, pet_serial, 0)
                    ate_meat = True
                    Misc.Pause(500)
                
        for food in foods.keys():
            item = Items.FindByID(food, -1, Player.Backpack.Serial)
            if item is not None:
                Target.Cancel()
                Misc.Pause(50)
                Items.Move(item, trush_poach_serial, 0)
                Misc.Pause(500)
    Misc.Pause(1000)
    
    
def Exec():
    filter = Mobiles.Filter()
    filter.Enabled = True
    filter.RangeMax = 30
    filter.Notorieties = List[Byte](bytes([3,4]))
    enemies = Mobiles.ApplyFilter(filter)
    Mobiles.Select(enemies,'Nearest')

    for enemy in enemies:
        Misc.SendMessage("Hue: " + str(enemy.Hue), enemy.Hue)
        #2305 is black
        for string in enemy.Properties:
            Misc.SendMessage(string, enemy.Hue)
        if enemy.Hue == 0:
            Invisibility()
            Player.Attack(enemy)
            Target.ClearLast()
            Misc.Pause(2000)
            Player.SetWarMode(False)
        else:
            Misc.Beep()
            
while True:
    PetFood(pet_serial, trush_poach_serial)
    Exec()
    Misc.Pause(1000)