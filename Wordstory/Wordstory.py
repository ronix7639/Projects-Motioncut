import time

# Define the initial variables
name = ""
health = 100

# Function to display story and choices
def story(text, options):
    print(text)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

# Function to get user choice and validate input
def get_choice(options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(options):
                print("Invalid choice. Please try again.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

# Introduction
print("Welcome to the Text Adventure Game!")
name = input("What is your name? ")
print(f"Hello, {name}! Let's begin your adventure.")

# Start of the story
story("You find yourself in a dark forest. You hear a noise in the distance.", ["Investigate the noise", "Ignore the noise"])
choice = get_choice(["Investigate the noise", "Ignore the noise"])

if choice == 1:
    story("You cautiously approach the source of the noise and discover a friendly squirrel.", ["Offer some food", "Run away"])
    choice = get_choice(["Offer some food", "Run away"])
    
    if choice == 1:
        story("The squirrel happily accepts the food and leads you deeper into the forest.", ["Follow the squirrel", "Leave the squirrel and continue on your own"])
        choice = get_choice(["Follow the squirrel", "Leave the squirrel and continue on your own"])
        
        if choice == 1:
            story("The squirrel guides you to a hidden treasure chest! You gain 50 health points.", [])
            health += 50
        else:
            story("You continue on your own, but you feel lost and your health decreases by 20 points.", [])
            health -= 20
    else:
        story("You run away from the squirrel and find yourself at a dead-end.", ["Go back and offer food to the squirrel", "Try to find another path"])
        choice = get_choice(["Go back and offer food to the squirrel", "Try to find another path"])
        
        if choice == 1:
            story("You go back and offer food to the squirrel. It leads you to a hidden treasure chest! You gain 50 health points.", [])
            health += 50
        else:
            story("You can't find another path and get more lost. Your health decreases by 20 points.", [])
            health -= 20
else:
    story("You decide to ignore the noise and continue walking deeper into the forest.", [])
    time.sleep(2)
    story("As you walk further, you stumble upon a mysterious ancient temple.", ["Enter the temple", "Keep walking deeper into the forest"])
    choice = get_choice(["Enter the temple", "Keep walking deeper into the forest"])
    
    if choice == 1:
        story("You enter the temple and find yourself in a chamber with a glowing gem. Touching it restores your health to 100 points!", [])
        health = 100
    else:
        story("You continue walking deeper into the forest, but you encounter a dangerous animal. Your health decreases by 30 points.", [])
        health -= 30

# Final outcome
if health <= 0:
    story("Your health has fallen to 0. You have failed in your adventure. Game Over!", [])
else:
    story("You successfully completed your adventure! Congratulations!", [])

# End of the game
print("Thank you for playing the Text Adventure Game. Goodbye, adventurer!")
