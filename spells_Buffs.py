from Scripts.utils import Utils

def buffs(target=Player.Serial):
    
    for spell in ["Strength", "Agility", "Cunning", "Bless"]:
        Spells.CastMagery(spell)
        Target.WaitForTarget(2000, False)
        Target.TargetExecute(target)
        Misc.Pause(Utils.getCRDelayOfMagery(6))

        
buffs(Target.PromptTarget(""))