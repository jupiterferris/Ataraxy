default tutorialGameCompleted = False
default tutorialConvoCompleted = False
default outfitchanged = False
default points = 0
# the precursor to the tutorial, only shown at the very beginning of the game. This is where the player inputs their name
label meet_ashley:
    scene intro
    show petals
    show ash close
    with fade
    nar "Performing first time setup..."
    show ash open
    play music "audio/jams/Lily Flower.mp3"
    show ash blink
    $ writeToFile("heardSongs.txt", "Lily Flower\n")
    a "Hello. I'm Ashley. I'm a virtual companion."
    show ash wink
    a "{i}Your{/i} virtual companion."
    show ash blink
    a "Neat, huh?"
    a "Technology truly is wonderful..."
    a "I'm not sure how you found me, but I'm glad you did. I can't wait to get to know you."
    show ash laugh
    a "But I digress."
    show ash blink
    a "I could use your help with something..."
    a "Before we start... what do you want to be referred to as?"
    $ namePlayer()
    a "Alright, [name], let's rock'n'roll."
    define y = Character("[name]")
    nar "This is a simulation of the human experience, coded by an amateur with an irrational love for RenPy."
    nar "The game is tailored by how you play. Your actions have consequences."
    a "With that said, shall we begin?"
    stop music fadeout 1.0
    jump init_tutorial
# only shows each time the player sees the tutorial
label init_tutorial:
    scene cloudback
    show clouds
    show ash open
    with fade
    play music "audio/jams/Rose's Fountain.mp3"
    show ash blink
    $ writeToFile("heardSongs.txt", "Rose's Fountain\n")
    a "Welcome to the tutorial!"
    a "I'm glad you made it here in one piece."
    a "Now, let's do it to it!"
    jump tutorial
# this is the tutorial, run from a preset set of events, giving an insight to the basic game mechanics.
label tutorial:
    menu:
        nar "Because this is the first time you've played, you get to pick what you do from a predetermined set of events."
        "Let's play a game." if not tutorialGameCompleted:
            a "Since it's your first time, let's start with something simple."
            jump tutorial_gayme
        "Let's chat." if not tutorialConvoCompleted:
            jump tutorial_convo
            #exclusive outfits from listening to stories- picked at random or user input- option removed from list after use.
        "Where am I up to?":
            python:
                if tutorialGameCompleted and tutorialConvoCompleted:
                    a("Welcome!")
                    nar("You've completed the tutorial. You can now play the game as you wish.")
                    a("I hope you enjoy your time with me.")
                    ashley.setValue("tutorialCompleted", True)
                    renpy.music.stop(fadeout=1.0)
                    renpy.jump("start")
                elif tutorialGameCompleted:
                    renpy.jump("tutorial_change")
                else:
                    renpy.show("ash laugh")
                    a("Silly, you just started- you haven't unlocked anything yet!")
                    renpy.show("ash blink")
                    a("This is where your unlockables will be displayed... Come back when you've exhausted your other options!")
                    renpy.jump("tutorial")
    label tutorial_gayme:
        a "I'm going to ask you a question, and you have to answer it."
        a "If you get it right, you get a point."
        a "If you get it wrong, you don't."
        show ash laugh
        a "Let's start with an easy one."
        show ash blink
        $ inputQuestion("What's my name?", "Ashley")
        a "Let's try another one."
        $ menuQuestion("What's my favorite color?", "Red", ["Red", "Yellow", "Green", "Blue"], True)
        a "One last question."
        a "How many fingers am I holding up?"
        show ash laugh
        a "Haha, just kidding."
        show ash blink
        a "I'll give you a point anyway, though."
        $ points += 1
        show ash close
        a "Let's see...."
        show ash open
        $ noun = getCorrectNoun()
        show ash blink
        a "You have reached [points] [noun]. Congratulations!"
        a "For humoring me on this remarkably dull game, I'll give you a reward."
        # Ashley gives the player a reward- the 'MonoMono Pin'.
        $ zeldaRiff("accessory", "01")
        $ tutorialGameCompleted = True
        a "Now, let's get back to the rest of the tutorial."
        jump tutorial

    label tutorial_convo:
        a "Hmm... What shall we talk about?"
        show ash laugh
        a "Ahaha, I know!"
        show ash blink
        a "What's your opinion on raisins?"
        menu:
            "I love them!":
                a "That's good to know!"
            "They're alright...":
                a "Interesting..."
            "Not a fan.":
                a "Ah... I see."

        show ash laugh
        a "Well, how do you feel about a date?"
        show ash blink
        a "Ahahaha, just kidding. Sorry, I had to!"
        a "Anyway, back to the tutorial."
        $ tutorialConvoCompleted = True
        jump tutorial

    label tutorial_change:
        $ global ashley
        $ global outfitchanged
        a "Welcome to the character customisation menu!"
        python:
            if outfitchanged:
                renpy.say(a, "Liking the new look?")
                renpy.jump("tutorial")
        a "I see you've unlocked a new outfit."
        menu:
            a "Would you like to try it out?"
            "Absolutely!":
                a "One moment. No peeking, okay?"
                python:
                    outfit = ashley.getValue("outfit")
                    outfit[5] = "01"
                    ashley.setValue("outfit", outfit)
                    outfitchanged = True
                    getAshBasics()
                show ash blink
                with fade
                a "Cute, right?"
                show ash laugh
                a "Ahaha. I know it is."
                show ash blink
            "Maybe later.":
                a "Okay. I'll leave it for now."
        a "You're almost done. Back into the fray!"
        jump tutorial
