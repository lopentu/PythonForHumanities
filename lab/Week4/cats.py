## An interactive story telling about Cats, the musical.
## All texts were adapted from https://www.catsthemusical.com/

scenes = {
    "prelude": {
        "story": (
            "Tonight is when the tribe of Jellicle Cats "
            "reunites to celebrate who they are."),
    },
    "intro": {
        "story": (
            "You are the wise Old Deuteronomy, "
            "who will choose which of the Jellicle Cats "
            "will journey tonight to the Heaviside layer "
            "to be reborn into a new life.")
    },
    "skimbleshanks": {
        "story": (
            "You chose Skimbleshanks, the railway cat, whose main role "
            "is to work on the mail trains travelling at ..., Wait!"),
        "link": "https://www.catsthemusical.com/characters/skimbleshanks"
    },
    "grizabella": {
        "story": (
            "You chose Grizabella, a sad and lonely cat. "
            "After leaving the Jellicle Tribe many years ago, "
            "Other Jellicle Cats refuse to accept her back into the fold. "
            "They eye her with suspicion."),
        "link": "https://www.catsthemusical.com/characters/grizabella"
    },
    "memory": {
        "story": (
            "All alone in the moonlight, Grizabella contemplates "
            "her \"Memory\" of a happier time, before she left the tribe. "
            "Led by memory, open up, enter in, they find where hapiness is. "
            "This time the tribe accept her back."
        ),
        "link": "https://www.youtube.com/watch?v=8gd_ohoPzYc"
    },
    "kidnap": {
        "story": (
            "Macavity with two of his henchmen invaded "
            "the proceedings and kidnap you !!"),
        "link": "https://www.youtube.com/watch?v=pai0GctB2XU"
    },
    "macavity": {
        "story": (
            "Macavity the Mystery Cat is a master criminal. "
            "He has an evil personality and is rarely seen behaving himself. "),
        "link": "https://www.catsthemusical.com/characters/macavity"
    },
    "mistoffelees": {
        "story": (
            "Mr Mistoffelees, the conjuring cat, use his magical "
            "powers to bring you back to the tribe."),
        "link": "https://www.youtube.com/watch?v=BV8pkcZUXAg"
    },
    "address": {
        "story": (
            "The Jellicle Ball has come to a conclusion. "
            "You, Old Deuteronomy, instructs the human spectators of "
            "how to address a cat, which begins with, "
            "'A cat is not a dog'..."),
        "link": "https://www.youtube.com/watch?v=0UaVMk4hXGo"
    }
}

print("")
print("{:^80}".format("Cats, the musical"))
print("{:^80}".format("===================="))
print("")

## Prelude
print("{:^80}".format("Prelude"))
print("{:^80}".format("---------"))
print(scenes["prelude"]["story"])
print("")
input("... (Enter to continue) ...")

## Introduction
print("{:^80}".format("Introduction"))
print("{:^80}".format("--------------"))
print(scenes["intro"]["story"])
print("")
input("... (Enter to continue) ...")

## Scene Choice
print("{:^80}".format("Choice"))
print("{:^80}".format("---------"))
print("Which Jellicle Cat would you choose?")
print("1. Skimbleshanks")
print("2. Grizabella")
x_scene1 = input("(1 or 2) >> ")
print("")

## Choice Conditions
if x_scene1 == "1":
    ## Skimbleshanks
    print(scenes["skimbleshanks"]["story"])
    print("Character: " + scenes["skimbleshanks"]["link"])
    print("")
    input("... (Enter to continue) ...")

    ## Kidnap
    print("{:^80}".format("Kidnap"))
    print("{:^80}".format("--------"))
    print(scenes["kidnap"]["story"])
    print("Stage: " + scenes["kidnap"]["link"])
    input("... (Enter to continue) ...")
    print("")

    ## Find Old Deuteronomy
    print("You are kidnapped, what could Jellicle Cats do to find you?")
    print("1. Ask Mistoffelees")
    print("2. I cannot be found. Who is Macavity anyway?")
    x_findme = input("(1 or 2) >> ")
    print("")

    if x_findme == "1":
        print(scenes["mistoffelees"]["story"])
        print("Character: " + scenes["mistoffelees"]["link"])
        print("")
        input("... (Enter to continue) ...")
        print("")

        ## Choose Again
        print("{:^80}".format("Choose Again, wisely"))
        print("{:^80}".format("----------------------"))
        print("Which Jellicle Cat would you choose?")
        print("1. Grizabella")
        x_scene1 = input("(1) >> ")
        print("")
        if x_scene1 != "1":
            print("It's OK, I know it's a typo. You meant "
                  "to choose Grizabella.")
            input("... (Enter to continue) ...")
            print("")        

    elif x_findme == "2":
        print(scenes["macavity"]["story"])
        print("Character: " + scenes["macavity"]["link"])
        print("")
        input("... (Enter to continue) ...")
        print("")

        print("{:^80}".format("Ending"))
        print("{:^80}".format("--------"))
        print("Macavity wins. It's not how Cats suppose to end though.")
        exit()
    else:
        print("Unknown story line. Please consult Author.")
        exit()
elif x_scene1 == "2":
    ## Continue to Grizabella Scene
    print("")
else:
    print("There is no such cat. Please consult Thomas S. Eliot.")
    exit()

## Grizabella Scene
print(scenes["grizabella"]["story"])
print("Character: " + scenes["grizabella"]["link"])
print("")
input("... (Enter to continue) ...")
print("")

## Memory Scene
print("{:^80}".format("Memory"))
print("{:^80}".format("--------"))
print(scenes["memory"]["story"])
print("Stage: " + scenes["memory"]["link"])
print("")
input("... (Enter to continue) ...")
print("")

## Address Ending
print("{:^80}".format("Ending"))
print("{:^80}".format("--------"))
print(scenes["address"]["story"])
print("")
print("Stage: " + scenes["address"]["link"])
print("")

## The End
print("")
print("{:^80}".format(" --  The End  --"))
