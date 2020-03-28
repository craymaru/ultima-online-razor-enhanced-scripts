'''
Author: TheWarDoctor95
Other Contributors:
Last Contribution By: TheWarDoctor95 - March 23, 2019

Description: Uses the recommended spells from the UO Forever Wiki (https://www.uoforum.com/wiki/index.php/Magery)
    to level Magery to GM. Will also increase Meditation if the skill is set to Up and not maxed out while running
'''

# Change this to False if you want to use all of the reagents in your backpack
saveReagentsForRecall = False
# Change this to the number of recall spells you want to be able to cast
numberOfRecallsToSaveFor = 1
# Change this to the number of extra milliseconds to delay between casts
# This will vary depending on which shard you are on
additionalShardCooldown = 500

from Scripts.glossary.spells import reagents, spells
from Scripts.utilities.items import FindNumberOfItems
from Scripts.glossary.colors import colors

mageryTimerMilliseconds = 6500
meditationTimerMilliseconds = 8200

def FindReagents():
    '''
    Uses FindNumberOfItems to find an the reagents in the player's backpack
    Returns a dictionary of the reagents found
    '''
    global reagents
    reagentItemIDs = []
    for reagent in reagents:
        reagentItemIDs.append( reagents[ reagent ].itemID )
    numberOfReagentsFound = FindNumberOfItems( reagentItemIDs, Player.Backpack )
    return numberOfReagentsFound


def CheckReagents( spellName, numberOfCasts = 1 ):
    '''
    Checks if the necessary reagents are available in the player's backpack to use a spell
    '''
    global spellInfo
    reagentsInBackpack = FindReagents()
    reagentsNeeded = spells[ spellName ].reagents
    for reagent in reagentsNeeded:
        if reagentsInBackpack[ reagent.itemID ] < numberOfCasts:
            return False
    return True


def TrainMagery():
    '''
    Trains Magery by casting spells on the player
    Stops training if the player runs out of the necessary reagents
    '''
    
    global mageryTimerMilliseconds
    global meditationTimerMilliseconds

    Timer.Create( 'mageryTimer', 1 )

    while not Player.IsGhost and Player.GetRealSkillValue( 'Magery' ) < Player.GetSkillCap( 'Magery' ):
        if saveReagentsForRecall and not CheckReagents( 'Recall', numberOfRecallsToSaveFor + 1 ):
            Misc.SendMessage( 'Need to save reagents for recall!', colors[ 'red' ] )
            return

        if not Timer.Check( 'mageryTimer' ):
            if Player.GetSkillValue( 'Magery' ) < 62.8:
                spell = spells[ 'Mana Drain' ]
            elif Player.GetSkillValue( 'Magery' ) < 75.5:
                spell = spells[ 'Invisibility' ]
            else:
                spell = spells[ 'Mana Vampire' ]

#            if not CheckReagents( spell.name ):
#                reagentsNeeded = spell.reagents
#                reagentsNeededAsString = ''
#                for reagent in reagentsNeeded:
#                    reagentsNeededAsString += reagent.name + ','
#                # Remove the extra comma from the string
#                reagentsNeededAsString[ : -1 ]
#                Misc.SendMessage( 'Ran out of regs for %s! These regs are needed: %s' % ( spell.name, reagentsNeededAsString ), colors[ 'red' ] )
#                break

            if Player.Mana > spell.manaCost:
                Spells.CastMagery( spell.name )
                
                # Wait an extra 100 ms in case of latency
                Timer.Create( 'mageryTimer', spell.delayInMs + additionalShardCooldown )

                # Target the cast spell on the player
                Target.WaitForTarget( 2000, True )
                Target.TargetExecute( Player.Serial )
            else:
                Player.UseSkill( 'Meditation' )
                Timer.Create( 'meditationTimer', meditationTimerMilliseconds )
                Misc.Pause( 200 )
                while Player.Mana < spell.manaCost + 1:
                    if not Player.BuffsExist( 'Meditation' ) and not Timer.Check( 'meditationTimer' ):
                        Player.UseSkill( 'Meditation' )
                        Timer.Create( 'meditationTimer', meditationTimerMilliseconds )
                    Misc.Pause( 200 )

        # Wait a little bit so that the while loop doesn't consume as much CPU
        Misc.Pause( 50 )

# Start the training
TrainMagery()
