import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def print_suspense(message_to_print):
    print(message_to_print)
    time.sleep(4)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("I'm sorry, I don't understand\n")
    return response


def intro():
    print_pause("You open your eyes and feel a confusing sense of urgency.")
    print_pause("You realize you had been sleeping on the couch, "
                "though you're not sure for how long.")
    print_pause("You sit up and look at your phone, noticing there's no "
                "signal.")
    print_pause("You're currently on the upper level of your house in the "
                "loft area.\n")


def bedroom(inventory):
    print_pause("You walk into your bedroom.")
    if "shed key" in inventory:
        print_pause("You were just in here, there isn't anything else to do "
                    "here right now.\n")
        where_to_go(inventory)
    elif "letter" in inventory:
        print_pause("You grab the key from your dresser.")
        print_pause("Your room is lit up insanely bright, you notice the "
                    "light is coming from the backyard.")
        print_pause("It must be coming from the shed, you think to yourself "
                    "'This must be what the letter is talking about.'\n")
        inventory.append("shed key")
        where_to_go(inventory)
    elif "back door" in inventory:
        print_pause("The light from the shed out back is so bright that it "
                    "lights up your entire bedroom.")
        print_pause("You grab the shed key from your dresser.\n")
        inventory.append("shed key")
        where_to_go(inventory)
    elif "bedroom" in inventory:
        print_pause("You were just here. Everything is as you left it.\n")
        where_to_go(inventory)
    else:
        print_pause("You go to the window holding your phone to the glass...")
        print_pause("You notice there is an intense bright light coming from "
                    "the shed out in the back yard")
        print_pause("The light is so bright, you can't figure out what it "
                    "might be.")
        print_pause("There's still no signal on your phone.\n")
        inventory.append("bedroom")
        where_to_go(inventory)


def front_door(inventory):
    print_pause("You walk through the house to the front door.")
    if "letter" in inventory:
        print_pause("You know your truck is gone, this is where you found a "
                    "strange letter.\n")
        search_bushes(inventory)
        where_to_go(inventory)
    else:
        print_pause("Walking out the front door you notice your truck isn't "
                    "in the driveway.")
        print_pause("Looking down you notice a letter tucked under the "
                    "'Welcome' mat.")
        print_pause("It reads, 'Dude! I had to leave it in the shed, couldn't "
                    "just leave it out in the open! Don't worry I locked it, "
                    "key is on your dresser.'")
        print_pause("The writing looks familiar but you can't quite "
                    "place it.\n")
        print_suspense("Wait, there's writing on the back.")
        print_pause("'I left that shiny object in the bushes, didn't want to "
                    "leave that in the open either.'")
        print_pause("'Can't be too careful, this is weird man.'\n")
        inventory.append("letter")
        search_bushes(inventory)
        where_to_go(inventory)


def back_door(inventory):
    print_pause("You pass through the dining room out the patio door.")
    print_pause("There's an intense bright light coming from the shed.")
    if "shed key" in inventory:
        print_pause("You walk up to the shed door, pull out the key from your "
                    "pocket.")
        print_pause("It sounds like something mechanical inside... and then "
                    "you hear a loud crash!")
        print_pause("You unlock the lock and open the door.")
        print_suspense("Everything goes dark.\n")
        print_suspense("A being steps out from the darkness of the shed.")
        print_pause("It's very apparent that it isn't human.")
        print_pause("It reaches it's hand out, as if it's asking for "
                    "something.")
        print_suspense("You search your pockets...")
        print_pause("...")
        if "shiny object" in inventory:
            print_suspense("You pull out the shiny object your friend told "
                           "you to search for.")
            print_pause("The being appears to smile.")
            print_pause("You win!\n")
            print_pause("GAME OVER.\n")
        elif "shiny object" not in inventory:
            if "letter" in inventory:
                print_suspense("After searching your pockets, you find only "
                               "your phone, shed key and the letter you found")
                print_pause("The being doesn't look very happy.")
                print_suspense("You're dead.\n")
                print_pause("GAME OVER.\n")
            elif "letter" not in inventory:
                print_suspense("After searching your pockets, you find only "
                               "your phone and the shed key.")
                print_pause("The being doesn't look very happy.")
                print_suspense("You're dead.\n")
                print_pause("GAME OVER.\n")
        play_again()
    elif "back door" in inventory:
        print_pause("You try the shed door again. It's locked, what did "
                    "you expect?")
        print_pause("You were just here and need to find the shed key.\n")
        where_to_go(inventory)
    else:
        print_pause("You hear a strange mechanical noise.")
        print_pause("As you approach the door of the shed, the sound goes "
                    "quiet.")
        print_pause("Trying the door, you discover that it is locked, "
                    "you'll need your key but you can't remember where "
                    "you left it.\n")
        inventory.append("back door")
        if "letter" in inventory:
            print_pause("This is what the letter was referring to.")
            if "shed key" not in inventory:
                print_pause("You remember the letter said the key was on "
                            "your dresser.\n")
        where_to_go(inventory)


def where_to_go(inventory):
    print_pause("Please enter a number for "
                "where you want to go next.")
    response = input("1. Go to the bedroom\n"
                     "2. Go out the front door\n"
                     "3. Go out the back door\n")
    if response == '1':
        bedroom(inventory)
    elif response == '2':
        front_door(inventory)
    elif response == '3':
        back_door(inventory)
    else:
        print_suspense("Did you hit your head? You know you can't go there.")
        print_pause("Where would you like to go next?\n")
        where_to_go(inventory)


def search_bushes(inventory):
    response = valid_input("Would you like to search nearby bushes for the "
                           "object? "
                           "Type 'Yes' to search or 'No' to move on.\n",
                           "yes", "no")
    if "yes" in response:
        if "shiny object" in inventory:
            print_pause("You must of really hit your head, the shiny object "
                        "is in your hands!")
            print_pause("Where do you want to go next?\n")
            where_to_go(inventory)
        else:
            c = random.choice(['You find nothing but rubbish.', 'You found '
                               'the shiny object!'])
            print_pause(c)
            if c == 'You found the shiny object!':
                inventory.append("shiny object")
        search_again(inventory)
    elif "no" in response:
        print_pause("Okay, where to next?")


def search_again(inventory):
    response = valid_input("Would you like to search again or move on? "
                           "Type 'Yes' to search again or 'No' to move on.\n",
                           "yes", "no")
    if "yes" in response:
        if "shiny object" in inventory:
            print_pause("You must of really hit your head, the shiny object "
                        "is in your hands!")
            print_pause("Where do you want to go next?\n")
        else:
            c = random.choice(['You find nothing but rubbish.', 'You found '
                               'the shiny object!'])
            print_pause(c)
            if c == 'You found the shiny object!':
                inventory.append("shiny object")
            search_again(inventory)
    if "no" in response:
        where_to_go(inventory)


def play_again():
    response = valid_input("Would you like to play again? "
                           "Type 'Yes' to play again or 'No' to finish and "
                           "move on.\n",
                           "yes", "no")
    if "yes" in response:
        play_game()
    elif "no" in response:
        print_pause("Thank you for playing!")


def play_game():
    inventory = []
    intro()
    where_to_go(inventory)


play_game()
