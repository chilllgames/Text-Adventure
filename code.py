import time

def choose_story():
    print("Choose a story:")
    print("1. Mystery in the Haunted Mansion")
    print("2. Journey to the Lost Kingdom")
    print("3. Quest for the Magical Crystal")
    
    choice = input("Enter the number of the story you want to play (1-3): ")
    
    if choice == "1":
        mystery_in_haunted_mansion()
    elif choice == "2":
        journey_to_lost_kingdom()
    elif choice == "3":
        quest_for_magical_crystal()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        choose_story()

def print_scene(scene):
    print("\n" + "*" * 50)
    print(scene)
    print("*" * 50 + "\n")
    time.sleep(2)

def mystery_in_haunted_mansion():
    print_scene("You find yourself standing in front of a mysterious haunted mansion.")
    print_scene("Strange noises echo from within. Do you dare enter?")

    print("1. Enter the mansion")
    print("2. Run away")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print_scene("You enter the mansion and hear creaking floors.")
        print_scene("A ghostly figure appears. What do you do?")

        print("1. Ask the ghost for its name")
        print("2. Run away screaming")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print_scene("The ghost introduces itself as Casper and offers to show you around.")
            print_scene("Casper reveals a hidden library with ancient books.")
            print_scene("You can choose a book. Which one will it be?")

            print("1. Book of Spells")
            print("2. Book of Prophecies")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print_scene("You learn a simple spell that illuminates dark places.")
                ending("Congratulations! You leave the haunted mansion with a new ability.")
            elif choice == "2":
                print_scene("You read about a prophecy related to the mansion's secrets.")
                ending("Congratulations! You uncover the mystery of the haunted mansion.")
            else:
                print("Invalid choice. Game over.")

        elif choice == "2":
            print_scene("You run away, but the ghost doesn't seem to chase you.")
            ending("You safely escape the haunted mansion.")
        else:
            print("Invalid choice. Game over.")

    elif choice == "2":
        ending("You decide not to enter the haunted mansion. Game over.")
    else:
        print("Invalid choice. Game over.")

def journey_to_lost_kingdom():
    print_scene("You embark on a journey to a distant lost kingdom.")
    print_scene("Legends speak of hidden treasures and magical creatures.")

    print("1. Explore the enchanted forest")
    print("2. Climb the treacherous mountain")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print_scene("You enter the enchanted forest and encounter a mystical unicorn.")
        print_scene("The unicorn offers to guide you to the treasure. What do you do?")

        print("1. Ride the unicorn")
        print("2. Thank the unicorn and continue on foot")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print_scene("You ride the unicorn and discover a hidden village of friendly fairies.")
            print_scene("The fairies reward you with a magical amulet. What do you do?")

            print("1. Wear the amulet")
            print("2. Thank the fairies and continue your journey")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print_scene("The amulet grants you the ability to understand the language of animals.")
                ending("Congratulations! You continue your journey with a magical amulet.")
            elif choice == "2":
                print_scene("You thank the fairies and continue your journey through the enchanted forest.")
                ending("Your journey in the enchanted forest continues.")
            else:
                print("Invalid choice. Game over.")

        elif choice == "2":
            print_scene("You continue on foot and face more challenges in the forest.")
            ending("Your journey in the enchanted forest continues.")
        else:
            print("Invalid choice. Game over.")

    elif choice == "2":
        print_scene("You climb the treacherous mountain and face strong winds.")
        print_scene("A friendly dragon appears. What do you do?")

        print("1. Pet the dragon")
        print("2. Ask the dragon for directions to the treasure")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print_scene("The dragon enjoys being petted and becomes your ally.")
            ending("Congratulations! The dragon helps you find the lost kingdom's treasure!")
        elif choice == "2":
            print_scene("The dragon provides helpful directions, and you reach the treasure.")
            ending("Congratulations! You found the lost kingdom's treasure!")
        else:
            print("Invalid choice. Game over.")

    else:
        print("Invalid choice. Game over.")

def quest_for_magical_crystal():
    print_scene("Your quest is to find the legendary Magical Crystal.")
    print_scene("It is said to possess unimaginable powers. Will you succeed?")

    print("1. Journey through the mystical valley")
    print("2. Cross the perilous bridge")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print_scene("You journey through the mystical valley and encounter talking animals.")
        print_scene("The animals share their wisdom with you. What do you do?")

        print("1. Listen to the animals")
        print("2. Continue without paying attention")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print_scene("You listen to the animals and gain knowledge.")
            print_scene("They guide you to a hidden cave. Do you enter the cave?")

            print("1. Enter the cave")
            print("2. Continue your journey")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                print_scene("Inside the cave, you find the Magical Crystal!")
                ending("Congratulations! You successfully completed your quest.")
            elif choice == "2":
                print_scene("You decide to continue your journey without entering the cave.")
                ending("Your quest for the Magical Crystal continues.")
            else:
                print("Invalid choice. Game over.")

        elif choice == "2":
            print_scene("You continue without listening and face challenges in the valley.")
            ending("Your quest in the mystical valley continues.")
        else:
            print("Invalid choice. Game over.")

    elif choice == "2":
        print_scene("You cross the perilous bridge guarded by a friendly troll.")
        print_scene("The troll challenges you to a riddle. Can you solve it?")

        print("1. Attempt to solve the riddle")
        print("2. Run away")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print_scene("You successfully solve the riddle, and the troll lets you pass.")
            ending("Congratulations! You proceed towards the Magical Crystal.")
        elif choice == "2":
            print_scene("You run away from the troll, but it doesn't chase you.")
            ending("You safely escape the perilous bridge.")
        else:
            print("Invalid choice. Game over.")

    else:
        print("Invalid choice. Game over.")

def ending(message):
    print("\n*** Game Over ***")
    print(message)
    print("Thanks for playing!")

# Start the game by choosing a story
choose_story()

