import time
import random
creature = random.choice(["dragon", "troll", "gorgon", "witch"])


def print_pause(line):
    print(line)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a barren field, \
    just overgrown grass and flowers.\n")
    print_pause(f"There is a rumor going around that an \
    evil {creature} lives here.\n")
    print_pause("To your left there is a trecherous swamp.\n")
    print_pause("To your right there is an ominous forrest.\n")
    print_pause("In your hands you have your trusty (but very dull) knife.\n")


def forest_area(items):
    if "sword" in items:
        print_pause("There is nothing more for you in this \
        forest so you head back\n")
        field_area(items)
    else:
        print_pause("You enter the forrest and spot something \
        shiny in the distance.\n")
        print_pause("It's Orlagons sword, and ancient relic \
        that's super powerful.\n")
        print_pause("You pick it up and take it with you, as \
        you walk back to the field.\n")
        items.append("sword")
        field_area(items)


def swamp_area(items):
    print_pause("You have entered the swamp\n")
    print_pause(f"You see a looming shadow coming closer to \
    you, it's the {creature}!\n")
    print_pause(f"The {creature} is going to attack you\n")
    print_pause("Enter 1 to run away\n")
    print_pause("Enter 2 to fight\n")

    ans2 = input("Please enter 1 or 2\n")
    if ans2 == "1":
        print("You have escaped back out into the field\n")
        field_area(items)
    elif ans2 == "2":
        if "sword" in items:
            print_pause(f"The {creature} approaches you\n")
            print_pause(f"You unsheath your new sword and the very \
            sight of it petrifies the {creature}\n")
            print_pause("Congratulations you have freed the area of \
            it's threat!\n")
            answer = input("play again? y/n\n")
            if answer == "y":
                play_game()
            elif answer == "n":
                print("Okay,hope you had fun !")
            else:
                print("Sorry what?")
        else:
            print_pause(f"you wield your trusty knife, but its of no \
            use the {creature} strikes you down\n")
            print_pause("You breathe your last breath of air as you...\n")
            print_pause("YOU HAVE DIED\n")
            answer = input("play again? y/n\n")
            if answer == "y":
                play_game()
            elif answer == "n":
                print("Okay,hope you had fun !")
            else:
                print("Sorry what?")


def field_area(items):
    while True:
        print_pause("Enter 1 to wander through the swamp.\n")
        print_pause("Enter 2 to look into the ominous forrest.\n")
        ans1 = input("Please enter 1 or 2\n").lower()
        if ans1 == "1":
            swamp_area(items)
            break
        elif ans1 == "2":
            forest_area(items)
            break
        else:
            print("sorry,what?")


def play_game():
    items = []
    intro()
    field_area(items)


play_game()
