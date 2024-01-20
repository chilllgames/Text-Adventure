import time

def intro():
    print("Welcome to the Adventure Story Game!")
    print("You find yourself in a magical forest. There are two paths ahead.")
    time.sleep(1)
    print("You can either go left into the Enchanted Garden or right towards the Whispering Woods.")

def enchanted_garden():
    print("\n   /\\_/\\ ")
    print("  ( o.o )")
    print("   > ^ < ")
    print("You enter the Enchanted Garden.")
    time.sleep(1)
    print("You see a talking unicorn! It offers to take you on a magical ride.")
    choice = input("Do you want to ride the unicorn? (yes/no): ").lower()
    
    if choice == "yes":
        print("\nThe unicorn takes you on a magical journey across the clouds!")
        time.sleep(1)
        print("You discover a hidden treasure chest.")
        ending("Congratulations! You found the treasure!")
    else:
        print("\nThe unicorn nods and disappears into the forest.")
        time.sleep(1)
        print("You continue your adventure.")
        time.sleep(1)
        forest()

def whispering_woods():
    print("\n  /~\ ")
    print(" (o.o) ")
    print("  > ^ < ")
    print("You enter the Whispering Woods.")
    time.sleep(1)
    print("The trees in this woods seem to whisper secrets.")
    choice = input("Do you want to listen to the whispers? (yes/no): ").lower()
    
    if choice == "yes":
        print("\nYou listen carefully and learn a magical spell.")
        time.sleep(1)
        print("The spell allows you to talk to animals.")
        time.sleep(1)
        ending("Congratulations! You gained a magical ability!")
    else:
        print("\nYou decide to move on without listening to the whispers.")
        time.sleep(1)
        forest()

def forest():
    print("\n  _-^-_ ")
    print(" /     \\ ")
    print("|       |")
    print("|       |")
    print("|_______|")
    print("You continue through the forest.")
    time.sleep(1)
    print("Ahead, you see a bridge guarded by a friendly troll.")
    choice = input("Do you want to cross the bridge? (yes/no): ").lower()

    if choice == "yes":
        print("\nThe troll smiles and lets you pass.")
        time.sleep(1)
        enchanted_garden()
    else:
        print("\nYou decide to take a different path.")
        time.sleep(1)
        whispering_woods()

def ending(message):
    print("\n*** Game Over ***")
    print(message)
    print("Thanks for playing!")

# Start the game
intro()
time.sleep(1)
forest()
