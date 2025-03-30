import dice_roller

def main():
    print("🎲 Dice Roller CLI")
    while True:
        print("\nSelect an option:")
        print("1️⃣ Roll a single die")
        print("2️⃣ Roll multiple dice (e.g., 2d6)")
        print("3️⃣ Roll D&D Ability Scores (6x 4d6 drop lowest)")
        print("4️⃣ Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            sides = int(input("Enter the number of sides on the die (e.g., 6 for d6): "))
            rolls = int(input("Enter the number of rolls: "))
            advantage = input("Do you want Advantage? (y/n): ").lower() == 'y'
            disadvantage = input("Do you want Disadvantage? (y/n): ").lower() == 'y'
            drop_lowest = int(input("How many lowest dice to drop? (0 for none): "))
            drop_highest = int(input("How many highest dice to drop? (0 for none): "))
            result, total = dice_roller.roll_die(sides, rolls, advantage, disadvantage, drop_lowest, drop_highest)
            print(f"🌀 Rolled {rolls} {sides}-sided die(s): {result}")
            print(f"📊 Total: {total}")

        elif choice == "2":
            dice_input = input("Enter the dice notation (e.g., 2d6 for two 6-sided dice): ")
            advantage = input("Do you want Advantage? (y/n): ").lower() == 'y'
            disadvantage = input("Do you want Disadvantage? (y/n): ").lower() == 'y'
            drop_lowest = int(input("How many lowest dice to drop? (0 for none): "))
            drop_highest = int(input("How many highest dice to drop? (0 for none): "))
            result, total = dice_roller.roll_multiple_dice(dice_input, advantage, disadvantage, drop_lowest, drop_highest)
            print(f"🌀 Rolls for {dice_input}: {result}")
            print(f"📊 Total: {total}")

        elif choice == "3":
            print("\n🎯 Rolling D&D Ability Scores (6x 4d6 drop lowest)")
            ability_scores = dice_roller.roll_ability_scores()
            print("\n📊 Ability Scores:")
            for i, (rolls, total) in enumerate(ability_scores, 1):
                print(f"Score {i}: {rolls} = {total}")

        elif choice == "4":
            print("🎲 Exiting Dice Roller. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
