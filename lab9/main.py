# Import the random library to use for the dice later
import random

# Import function module
import function

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))  # Max combat strength is 6
big_dice_options = list(range(1, 21))  # Max health points is 20

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero Combat Strength
i = 0
input_valid = False

while not input_valid and i < 5:
    try:
        combat_strength = input("Enter your combat Strength (1-6): ")
        if not combat_strength.isnumeric():
            raise ValueError("Invalid input. Please enter an integer between 1 and 6.")

        combat_strength = int(combat_strength)
        if combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only.")

        input_valid = True

    except ValueError as e:
        print(e)
        i += 1

# Loop to get valid input for Monster Combat Strength
i = 0
m_input_valid = False

while not m_input_valid and i < 5:
    try:
        m_combat_strength = input("Enter the monster's combat Strength (1-6): ")
        if not m_combat_strength.isnumeric():
            raise ValueError("Invalid input. Please enter an integer between 1 and 6.")

        m_combat_strength = int(m_combat_strength)
        if m_combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only.")

        m_input_valid = True

    except ValueError as e:
        print(e)
        i += 1

# Proceed only if both inputs are valid
if input_valid and m_input_valid:
    # Roll for player health points
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("Player rolled", health_points, "health points")

    # Roll for monster combat strength
    input("Roll the dice for the monster's combat strength (Press enter)")
    m_combat_strength = random.choice(small_dice_options)
    print("Monster's combat strength:", m_combat_strength)

    # Roll for monster health points
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("Monster rolled", m_health_points, "health points")

    # Loop while both the monster and the player are alive
    while m_health_points > 0 and health_points > 0:
        # Determine attack order
        input("Roll to see who attacks first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:
            input("You strike (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)
            if m_health_points > 0:
                try:
                    input("The monster strikes (Press enter)!!!")
                    health_points = function.monster_attacks(m_combat_strength, health_points)
                except Exception as e:
                    print("Error in monster attack:", e)

        else:
            input("The Monster strikes (Press enter)")
            try:
                health_points = function.monster_attacks(m_combat_strength, health_points)
            except Exception as e:
                print("Error in monster attack:", e)

            if health_points > 0:
                input("The hero strikes!! (Press enter)")
                m_health_points = function.hero_attacks(combat_strength, m_health_points)


# health_points = function.monster_attacks("Somestring1", "Somestring2")
