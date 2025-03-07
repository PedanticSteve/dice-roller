import random

def roll_die(sides: int, rolls: int = 1, advantage: bool = False, disadvantage: bool = False):
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
    
    return results

def roll_multiple_dice(dice: str, advantage: bool = False, disadvantage: bool = False):
    """Parses a dice notation like '2d6' and returns the results, with advantage or disadvantage."""
    try:
        num, sides = map(int, dice.lower().split('d'))
        if num <= 0 or sides <= 0:
            raise ValueError("Both numbers must be greater than zero.")
        return roll_die(sides, num, advantage, disadvantage)
    except ValueError:
        return "⚠️ Invalid dice format. Please use the format 'NdM' (e.g., '2d6')."
