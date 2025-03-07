import dice_roller

def main():
    print("🎲 Dice Roller CLI")
    while True:
        print("\nSelect an option:")
        print("1️⃣ Roll a single die")
        print("2️⃣ Roll multiple dice (e.g., 2d6)")
        print("3️⃣ Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            sides = int(input("Enter the number of sides on the die (e.g., 6 for d6): "))
            rolls = int(input("Enter the number of rolls: "))
            advantage = input("Do you want Advantage? (y/n): ").lower() == 'y'
            disadvantage = input("Do you want Disadvantage? (y/n): ").lower() == 'y'
            result = dice_roller.roll_die(sides, rolls, advantage, disadvantage)
            print(f"🌀 Rolled {rolls} {sides}-sided die(s): {result}")

        elif choice == "2":
            dice_input = input("Enter the dice notation (e.g., 2d6 for two 6-sided dice): ")
            advantage = input("Do you want Advantage? (y/n): ").lower() == 'y'
            disadvantage = input("Do you want Disadvantage? (y/n): ").lower() == 'y'
            result = dice_roller.roll_multiple_dice(dice_input, advantage, disadvantage)
            print(f"🌀 Rolls for {dice_input}: {result}")

        elif choice == "3":
            print("🎲 Exiting Dice Roller. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
