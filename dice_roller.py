import random

def roll_die(sides: int, rolls: int = 1, advantage: bool = False, disadvantage: bool = False, drop_lowest: int = 0, drop_highest: int = 0):
    """Rolls a die with a specified number of sides, rolls count, and Advantage/Disadvantage option."""
    results = []
    
    if advantage or disadvantage:
        # Roll twice and take higher or lower value depending on advantage/disadvantage
        for _ in range(rolls):
            roll1 = random.randint(1, sides)
            roll2 = random.randint(1, sides)
            if advantage:
                results.append(max(roll1, roll2))  # Advantage: take the higher roll
            elif disadvantage:
                results.append(min(roll1, roll2))  # Disadvantage: take the lower roll
    else:
        # Standard rolling without advantage/disadvantage
        results = [random.randint(1, sides) for _ in range(rolls)]
    
    # Handle dropping highest/lowest dice
    if drop_lowest > 0 or drop_highest > 0:
        results.sort()  # Sort the results
        if drop_lowest > 0:
            results = results[drop_lowest:]  # Remove lowest dice
        if drop_highest > 0:
            results = results[:-drop_highest]  # Remove highest dice
    
    return results, sum(results)

def roll_multiple_dice(dice: str, advantage: bool = False, disadvantage: bool = False, drop_lowest: int = 0, drop_highest: int = 0):
    """Parses a dice notation like '2d6' and returns the results, with advantage or disadvantage."""
    try:
        num, sides = map(int, dice.lower().split('d'))
        if num <= 0 or sides <= 0:
            raise ValueError("Both numbers must be greater than zero.")
        return roll_die(sides, num, advantage, disadvantage, drop_lowest, drop_highest)
    except ValueError:
        return "⚠️ Invalid dice format. Please use the format 'NdM' (e.g., '2d6')."

def roll_ability_scores():
    """Rolls 6 sets of 4d6, dropping the lowest die each time (standard D&D ability score generation)."""
    ability_scores = []
    for i in range(6):
        rolls, total = roll_die(6, 4, drop_lowest=1)
        ability_scores.append((rolls, total))
    return ability_scores
