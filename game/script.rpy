# The script of the game goes in this file.
# cummies :heart_eyes:
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ashley")
define y = Character("You")
define nar = Character(what_italic=True)


##### TO DO #####

# Add more outfits (EFFORT)- unlockedOutfits list and select outfit from menu in there?

# figure out how to import time- add to greeting messages on boot (been a while, good morning etc)
# relationship progress- list of low-relationship startup messages
# player input option(?)
# use seasonal music/skins- check on start to use diff text file
# which song is playing quiz- part of the random questions/ do you remember who wrote this/ what album?
# Enjoyer Of Things on youtube- Waiting on Screensaver- add grapes as secret?
# random event on startup - how was your day? long time no see?
# pick from a menu option of games- hangman, dice game, sudoku, card games/21? jump to python subroutine- you can choose from unlocked games?
# winning games gives you relationship points- points can be used on unlockables at threshold. unlockable outfits based on criteria met?
# text-based adventure game? - choose your own adventure
# add a day structure? 3 conversations and she asks you to do something etc
# get different colour hair ashley based on favourite colour
# have main menu be overlay over ashley periodically opening her eyes and looking at you
# add an option for random outfit on startup?

# when you bi

####################


init:
    image ash:
        f"ashley{outfit} open"
        pause 8.0
        f"ashley{outfit} laugh"
        pause 0.1
        f"ashley{outfit} close"
        pause 0.5
        f"ashley{outfit} laugh"
        pause 0.1
        repeat
    image ash wink:
        f"ashley{outfit} winkr1"
        pause 0.1
        f"ashley{outfit} winkr2"
        pause 0.5
        f"ashley{outfit} winkr1"
        pause 0.1
        f"ashley{outfit} open"
    image ash close:
        f"ashley{outfit} open"
        pause 0.1
        f"ashley{outfit} laugh"
        pause 0.1
        f"ashley{outfit} close"
    image ash open:
        f"ashley{outfit} close"
        pause 0.5
        f"ashley{outfit} laugh"
        pause 0.1
        f"ashley{outfit} open"
    image ash laugh:
        f"ashley{outfit} laugh"

init python:

    def jams(name, **kwargs):
        global ashley
        global chosentrack
        global ATP_played
        import random
        global albumname
        global trackno
        global artist
        egirltrilogy = ["I'm In Love With An E-Girl", "Internet Ruined Me", "Your New Boyfriend"]
        ycgma = ["Jubilee Line", "Saline Solution", "Your Sister Was Right", "Losing Face", "Since I Saw Vienna", "La Jolla", "I'm Sorry Boris"]
        areyoualright = ["Taunt", "One Day", "Sex Sells", "Cause For Concern"]
        pebblebrain = ["Oh Yeah, You Gonna Cry", "Model Buses", "Concrete", "Perfume", "You'll Understand When You're Older", "The Fall", "It's All Futile! It's All Pointless!"]
        maybeiwasboring =["Maybe I Was Boring", "For Memories", "White Wine In A Wetherspoons"]
        covers = ["Knee Deep At ATP", "Privately Owned Spiral Galaxy"]
        unlisted = ["Soft Boy", "The Nice Guy Ballad"]
        secret = ["Grapes"]
        renpy.music.stop(fadeout=3.0)
        file = renpy.open_file("tunes.txt")
        songs = file.readlines()
        numofjams = len(songs)
        a(f"Number of songs available: {numofjams}")
        randomsong = random.choice(songs).decode()
        chosentrack = randomsong.replace("\r\n","")
        a(f"Track chosen: {chosentrack}")
        renpy.music.play(f"audio/jams/{chosentrack}.mp3")
        if chosentrack == "Knee Deep At ATP":
            renpy.show("ash laugh")
            renpy.say(a, "You lucky thing, that's my creator's favourite song!")
            ashley.setValue("ATP_played", True)
            renpy.show("ash")
        elif chosentrack == "Soft Boy":
            renpy.say(a, "Fun fact- this is actually the main menu song!")
            ashley.setValue("SoftBoy_played", True)
            #wait what's a main menu
        if chosentrack in egirltrilogy:
            albumname = "The E-Girl Trilogy"
            trackno = egirltrilogy.index(chosentrack)
            trackno += 1
            artist = "Wilbur Soot"
        elif chosentrack in ycgma:
            albumname = "Your City Gave Me Asthma"
            trackno = ycgma.index(chosentrack)
            trackno += 1
            artist = "Wilbur Soot"
        elif chosentrack in areyoualright:
            albumname = "Are You Alright?"
            trackno = areyoualright.index(chosentrack)
            trackno += 1
            artist = "Lovejoy"
        elif chosentrack in pebblebrain:
            albumname = "Pebblebrain"
            trackno = pebblebrain.index(chosentrack)
            trackno += 1
            artist = "Lovejoy"
        elif chosentrack in maybeiwasboring:
            albumname = "Maybe I Was Boring"
            trackno = maybeiwasboring.index(chosentrack)
            trackno += 1
            artist = "Wilbur Soot"
        elif chosentrack in covers:
            albumname = "Covers"
            trackno = covers.index(chosentrack)
            trackno += 1
            artist = "Lovejoy"
        elif chosentrack in unlisted:
            albumname = "the collection of unlisted songs"
            trackno = unlisted.index(chosentrack)
            trackno += 1
            artist = "Wilbur Soot"
        elif chosentrack in secret:
            albumname = "the secret tracks"
            trackno = secret.index(chosentrack)
            trackno += 1
            artist = "James Marriott"
        else:
            albumname = "Unknown"
            trackno = "Unknown"
            artist = "either Wilbur Soot or Lovejoy"

    def writeToFile(filename, text):
        with open(config.gamedir + "/" + filename, "a") as f:
            f.write(text)
        return
    
    global wilburtext
    global outfit
    wilburtext = False
    tutorialGameCompleted = False
    tutorialConvoCompleted = False
    import json
    import os

    # have another json for quiz topics? only true ones in a list can be asked?
    class CharacterManager:
        def __init__(self):
            self.filename = f"{os.path.join(os.path.dirname(__file__), '..')}\characters\Player.json"
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)

            self.open()
            # Player Name
            name = self.json.get("name")
            if name is None:
                self.setValue("name", "")

            # Ashley's current outfit
            outfit = self.json.get("outfit")
            if outfit is None:
                self.setValue("outfit", "00")

            # Tutorial completed
            tutorialcompleted = self.json.get("tutorialcompleted")
            if tutorialcompleted is None:
                self.setValue("tutorialcompleted", False)

            # Relationship with Ashley
            relationship = self.json.get("relationship")
            if relationship is None:
                self.setValue("relationship", 0)

            # Secret track "Grapes" unlocked
            grapes = self.json.get("grapes")
            if grapes is None:
                self.setValue("grapes", False)

            # Player knows ATP is my favourite song
            ATP_played = self.json.get("ATP_played")
            if ATP_played is None:
                self.setValue("ATP_played", False)

            # Player know Soft Boy is the main menu song
            SoftBoy_played = self.json.get("SoftBoy_played")
            if SoftBoy_played is None:
                self.setValue("SoftBoy_played", False)

            # Player knows extra Wilbur lore
            wilburtextheard = self.json.get("wilburtextheard")
            if wilburtextheard is None:
                self.setValue("wilburtextheard", False)

            # Player knows Ashley's surname
            surname = self.json.get("surname")
            if surname is None:
                self.setValue("surname", False)

            # Player knows Ashley's favourite colour
            colour = self.json.get("colour")
            if colour is None:
                self.setValue("colour", False)

            # Player knows Ashley's favourite food
            food = self.json.get("food")
            if food is None:
                self.setValue("food", False)

            # Player knows Ashley's favourite dessert
            dessert = self.json.get("dessert")
            if dessert is None:
                self.setValue("dessert", False)

            # Player knows Ashley's favourite animal
            animal = self.json.get("animal")
            if animal is None:
                self.setValue("animal", False)

            # Player knows Ashley's favourite thing to do
            thing = self.json.get("thing")
            if thing is None:
                self.setValue("thing", False)

            # Player knows Ashley's favourite genre
            genre = self.json.get("genre")
            if genre is None:
                self.setValue("genre", False)

            # Player knows Ashley's height
            tall = self.json.get("tall")
            if tall is None:
                self.setValue("tall", False)
            
            unlockedOutfits = self.json.get("unlockedOutfits")
            if unlockedOutfits is None:
                self.setValue("unlockedOutfits", ["00"])
        def open(self):
            try:
                with open(self.filename, "r") as f:
                    try:
                        self.json = json.load(f)
                    except:
                        self.json = {}
            except:
                self.json = {}

        def getValue(self, keymies):
            return self.json.get(keymies)

        def setValue(self, keymies, value):
            self.json[keymies] = value
            dump = json.dumps(self.json)
            with open(self.filename, "w+") as f:
                f.write(dump)

# The game starts here.

label start:
    # this is the intro- also serves as initial loading progress.
    python:
        global ashley
        ashley = CharacterManager()
        outfit = ashley.getValue("outfit")
        tutorialcompleted = ashley.getValue("tutorialcompleted")
        name = ashley.getValue("name")
        relationship = ashley.getValue("relationship")

    stop music fadeout 1.0
    scene bg room

    show ash
    with fade

    show ash close

    a "Initialising..."

    $ jams("")

    show ash open

    a "Name in file = [name], relationship = [relationship], tutorialcomplete = [tutorialcompleted]."

    python:
        if tutorialcompleted and name != "":
            renpy.jump("launch")
        elif not tutorialcompleted and name != "":
            renpy.jump("tutorial")
        else:
            renpy.jump("meet_ashley")

label meet_ashley:
    # this is the first time you meet Ashley, and you set your name.
    a "Hello. I'm Ashley. I'm a virtual girlfriend."
    show ash wink
    a "{i}Your{/i} virtual girlfriend."
    show ash
    a "Neat, huh?"
    a "Technology truly is wonderful..."
    a "I'm not sure how you found me, but I'm glad you did. I can't wait to get to know you."
    show ash laugh
    a "But I digress."
    show ash

    a "I could use your help with something..."
    a "Before we start... what do you want to be referred to as?"
    python:
        name = renpy.input(_("Enter your name."))
        name = name.strip() or __("Babes")
        if name.lower() == "daddy":
            name = "Master Hardwick"
        elif name.lower() == "cum":
            renpy.show("ash laugh")
            renpy.say(a, "You disgust me.")
            renpy.show("ash")
        elif name.lower() == "raffi" or name.lower() == "raf" or name.lower() == "gearloe":
            renpy.say(a, "Well, well, well... I knew this day would come.")
            renpy.say(a, "Finally, a worthy adversary. Our battle will be legendary!")
            renpy.show("ash laugh")
            renpy.say(a, "...love you xx :)")
            renpy.show("ash")
        elif name.lower() == "bibblyboy":
            renpy.show("ash laugh")
            renpy.say(a, "I love men.")
            renpy.show("ash")
        ashley.setValue("name", name)
    a "Alright, [name], let's rock'n'roll."
    define y = Character("[name]")
    nar "This is a simulation of the human experience, coded by an amateur with an irrational love for RenPy."
    nar "The game is tailored by how you play. Your actions have consequences."
    a "With that said, shall we begin?"
    jump tutorial

label tutorial:
    # this is the tutorial run from a preset set of events
    python:
        global ashley
        global tutorialGameCompleted
        global tutorialConvoCompleted
    menu:
        nar "Because this is the first time you've played, you get to pick what you do from a predetermined set of events."
        "Let's play a game." if not tutorialGameCompleted:
            a "Since it's your first time, let's start with something simple."
            jump tutorial_gayme
        "Let's chat." if not tutorialConvoCompleted:
            jump tutorial_pick_convo
            #exclusive outfits from listening to stories- picked at random or user input- option removed from list after use.
        "Where am I up to?":
            python:
                if tutorialGameCompleted and tutorialConvoCompleted:
                    renpy.say(a, "Welcome back!")
                    renpy.say(nar, "You've completed the tutorial. You can now play the game as you wish.")
                    renpy.say(a, "I hope you enjoy your time with me.")
                    ashley.setValue("tutorialcompleted", True)
                    renpy.jump("launch")
                elif tutorialGameCompleted or tutorialConvoCompleted:
                    renpy.jump("tutorial_change")
                else:
                    renpy.show("ash laugh")
                    renpy.say(a, "Silly, you just started- you haven't unlocked anything yet!")
                    renpy.show("ash")
                    renpy.say(a, "This is where your unlockables will be displayed... Come back when you've exhausted your other options!")
                    renpy.jump("tutorial")
    label tutorial_gayme:
        # this is the tutorial game
        python:
            def correctNoun(points, noun):
                if points == 1:
                    return "point"
                else:
                    return "points"
        $ global ashley
        $ global tutorialGameCompleted
        $ points = 0
        $ noun = "points"
        a "I'm going to ask you a question, and you have to answer it."
        a "If you get it right, you get a point."
        a "If you get it wrong, you don't."
        show ash laugh
        a "Let's start with an easy one."
        show ash
        a "What's my name?"
        python:
            answer = renpy.input(_("Enter your answer."))
            if answer.lower() == "ashley":
                renpy.say(a, "Correct!")
                renpy.say(a, "You get a point.")
                points += 1
            else:
                renpy.say(a, "Incorrect.")
                renpy.say(a, "You don't get a point.")
        $ noun = correctNoun(points, noun)
        a "You now have [points] [noun]."
        a "Let's try another one."
        menu:
            a "What's my favourite colour? Hint- look at my hair!"
            "Red":
                a "Correct! That may have been too easy..."
                a "You get a point."
                $ points += 1
            "Blue":
                a "Incorrect."
                a "You don't get a point."
            "Green":
                a "Incorrect."
                a "You don't get a point."
            "Yellow":
                a "Incorrect."
                a "You don't get a point."
        $ noun = correctNoun(points, noun)
        a "You now have [points] [noun]."
        a "One last question."
        a "How many fingers am I holding up?"
        show ash laugh
        a "Haha, just kidding."
        show ash
        a "I'll give you a point anyway, though."
        $ points += 1
        show ash close
        a "Let's see...."
        show ash open
        show ash
        $ noun = correctNoun(points, noun)
        a "You have reached [points] [noun]. Congratulations!"
        a "For humoring me on this remarkably dull game, I'll give you a reward."
        # Ashley gives the player a reward- the 'MonoMono' outfit.
        python:
            unlocked = ashley.getValue("unlockedOutfits")
            if "01" in unlocked:
                # 01 is only unlocked from the tutorial and it's only playable once. It shouldn't already be there
                renpy.say(a, "Wait... that's not right.")
                renpy.say(a, "You already have this one.")
                renpy.say(a, "That shouldn't have happened.")
                renpy.show("ash laugh")
                renpy.say(a, "You're not doing anything you shouldn't, are you?")
                renpy.show("ash")
                renpy.say(a, "Ahaha. I'm kidding.")
            else:
                unlocked.append("01")
                ashley.setValue("unlockedOutfits", unlocked)
                renpy.say(nar, "You have unlocked the 'MonoMono Pin' outfit. Visit the unlockables menu to equip it!")
            tutorialGameCompleted = True
            renpy.say(a, "Now, let's get back to the rest of the tutorial.")
        jump tutorial
    label tutorial_pick_convo:
        a "To start you off, I'm going to tell you a story."
        show ash laugh
        a "It's not too long, I promise."
        show ash

    label tutorial_change:
        $ global ashley
        a "Welcome to the character customisation menu!"
        a "I see you've unlocked a new outfit."
        menu:
            a "Would you like to try it out?"
            "Absolutely!":
                a "One moment. No peeking, okay?"
                $ ashley.setValue("outfit", "01")
                $ outfit = ashley.getValue("outfit")
                show ash
                with fade
                a "Cute, right?"
                show ash laugh
                a "Ahaha. I know it is."
                show ash
            "Maybe later.":
                a "Okay. I'll leave it for now."
        a "You're almost done. Back into the fray!"
        jump tutorial

label launch:
    # this is where the player will be taken on launch after the tutorial is complete
    python:
        global ashley
        import random
        relationship = ashley.getValue("relationship")
        name = ashley.getValue("name")
        if relationship < 10:
            greetings = ["Well hello again.",
                        "Welcome back, [name].",
                        "Here we go again...",
                        "What's on your mind?",
                        "It's [name], right?",
                        "Fancy seeing you here!"]
        elif relationship >= 10 and relationship < 25:
            greetings = ["You're getting the hang of this now~",
                        "It's good to see you again.",
                        "I'm glad you're enjoying yourself.",
                        "I'm glad you're back.",
                        "I'm glad you're back, [name].",
                        "You look like you have something to ask me. Don't worry, I won't bite.",
                        "Hey, [name]. What's up?"]
        elif relationship >= 25:
            greetings = ["You must really like me... Aha, don't worry. I like you too",
                        "I missed seeing that face of yours~",
                        "You're giving me that look again... not that I mind.",
                        "[name]! It's so nice to see you."
                        "I was just wondering when you'd come visit me again."
                        "Don't leave me so long next time...",
                        "James Holroyd is hot.",
                        "I missed you...",
                        "I'm here whenever you need me... I hope you know that."]
        greet = random.choice(greetings)
        renpy.say(a, "[greet]")

        renpy.jump("random_events")

label random_events:
    # when the game is launched, before you get to interact with Ashley, you might have a random event.
    python:
        event = random.randint(1, 100)
        renpy.say(a, "Event value = [event]")
        if event == 1:
            renpy.say(a, "I'm sorry, I'm not feeling well today. I'll be back next time.")
            renpy.show ("ash close")
            renpy.jump("quit")
        elif event > 90:
            renpy.say(a, "Let me ask you something...")
        #    menu:
        #        a "How's your day been?"
        #        "Great!":
        #        "It's been alright.":
        #        "Not so good.":
    jump interact

label interact:
    # this is where the player can interact with Ashley
    # you can play a game, chat, or go to the unlockables menu

    menu:
        a "So what do you want to do?"
        "Let's play a game.":
            jump gayme
        "Let's chat.":
            jump pick_convo
        "Where am I up to?":
            # move this to unlockables as menu
            a "Looking for an outfit change? Variety is the spice of life, after all."
            jump unlockables


label pick_convo:
    # this is where the player can pick a conversation topic
    
    menu:
        a "Hmmm... What shall we talk about?"
        "Tell me a story!":
            jump convo_anecdote
            # Ashley either picks a random topic or a topic based on the player's relationship with her- story changes depending on answers?
        "Tell me about yourself":
            jump convo_question
            # Ashley tells you random information about herself- 1/10 chance she asks you a question
        "Recite something!":
            jump convo_poem
            # Ashley recites a poem
        "What is that god-awful noise?":
            jump convo_song
            # Change music/find out what song is playing
        "You choose!":
            jump convo_ashchoice
            # Ashley chooses at random
            

    label convo_song:
    # this is where Ashley tells the player what song is playing and more information about it
        python:
            global chosentrack
            global albumname
            global trackno
            global artist
            global name
            global wilburtext
            global ashley
            renpy.say(a, f"The current song playing is {chosentrack}, by {artist}.")
            if wilburtext == False:
                wilburtext = True 
                ashley.setValue("wilburtextheard", True)
                renpy.say(a, "The person who coded this really loves Wilbur Soot's music... Ahaha.")
                renpy.say(a, "Can't say I blame her... He's quite something. Don't you agree?")
                # if the player says yes, they get a special outfit?
                if ashley.getValue("wilburtextheard"): 
                    renpy.show("ash laugh")
                    renpy.say(a, "But you've already heard this before, haven't you?")
                    renpy.show("ash")
                    renpy.say(a, "In another session, I mean.")
                else:    
                    renpy.show("ash laugh")
                    renpy.say(a, "What am I saying, of course you do.")
                    renpy.show("ash")
            else:
                renpy.say(a, "I'm glad you like it.")
        menu:
            "Can I hear some more?":
                a "Of course you can. Give me a moment."
                $ jams("")
                a "Better?"
                label song_pick_loop:
                    menu:
                        "Another! Let's keep this train rolling.":
                            python:
                                import random
                                responses = ["And so it shall be.",
                                            "Anything for you...",
                                            "I don't think so. Haha, just kidding!",
                                            f"Sure thing, {name}."]
                                retort = random.choice(responses)
                                renpy.say(a, "[retort]")
                                jams("")
                            jump song_pick_loop
                        "Based. I'll stick with this one.":
                            a "Have fun~"
                            jump pick_convo
                        "Which song is this again?":
                            jump tellmemore

            "Alright cool. Love it.":
                a "My pleasure. Come back anytime if you want to hear something new~"
                jump pick_convo
            "Tell me more about this song.":
                label tellmemore:
                    a "This is Enjoyer Of Things' piano cover of [chosentrack], track [trackno] from [albumname], by [artist]."
                    menu:
                        a "Would you like to hear more?"
                        "Of course.":
                            a "I'm glad you're interested. It's nice when other people take interest in the things you love."
                            a "Enjoyer Of Things is a YouTuber who predominantly makes piano covers of songs by Wilbur Soot and his band, Lovejoy."
                            a "Wilbur himself is a Twitch streamer- he's quite famous for his Minecraft videos on Youtube."
                            a "He has a side hobby as a musician, where he released several albums and EPs, such as Your City Gave Me Asthma, Maybe I Was Boring, and The E-Girl Trilogy."
                            a "More recently, he started a band with Ash Kabosu, Joe Goldsmith, and Mark Boardmen, called Lovejoy."
                            a "So far, they have released two albums, Are You Alright? and Pebblebrain, and are working on a third."
                            a "They have also released a few covers of songs by other artists, such as Crywank's Privately Owned Spiral Galaxy and Knee Deep At ATP by Los Campesinos!" 
                            show ash laugh
                            a "I hope that was enough information for you. If you want to know more, you can always ask my creator."
                            show ash
                            python: 
                                if not ashley.getValue("grapes"):
                                    ashley.setValue("grapes", True)
                                    writeToFile("tunes.txt", "Grapes\n")
                                    renpy.say(a, "As a thank you for listening to my rambling, I've unlocked a secret track for you.")
                                    renpy.say(a, "It's a lesser-known song by James Marriott that was made collaboratively with Ash Kabosu- Lovejoy's bass guitarist.")
                                    renpy.say(a, "Enjoy~")
                                else: 
                                    renpy.say(a, "I was going to give you a secret track as thanks, but it appears you've already unlocked it.")
                                    renpy.show("ash laugh")
                                    renpy.say(a, "Did you hope I would give you another one? Haha, sorry. You only get the one.")         
                                    renpy.show("ash")       
                            jump song_pick_loop
                        "No thanks.":
                            a "As you wish."
                            jump song_pick_loop

    label convo_ashchoice:
    # this is where Ashley picks a conversation topic for you
    python:
        import random
        convotopic = random.randint(1,5)
        if convotopic == 1:
            renpy.jump("convo_anecdote")
        elif convotopic == 2 or convotopic == 3:
            renpy.jump("convo_question")
        elif convotopic == 4:
            renpy.jump("convo_poem")
        elif convotopic == 5:
            renpy.say(a, "How about we play a game instead?")
            renpy.jump("gayme")

            #a "I'm afraid I don't know much about it. I just know it's good."
            #a "I'm sure you can find out more about it online, though."
    label convo_question:
        # this is where the player asks Ashley a question- or Ashley asks the player a question
        # the question you ask is chosen, but the question Ashley asks is randomised
        python:
            import random
            unoreverse = random.randint(1,5)
            if unoreverse == 1:
                renpy.jump("uno_reverse")
            else:
                renpy.jump("question")
        label uno_reverse:
            # this is where Ashley asks the player a question (surprise!)
            python:
                questionlist = ["What's your favourite colour?", "What's your favourite food?", "What's your favourite dessert/sweets?", "What's your favourite animal?", "What's your favourite thing to do?", "What's your favourite book genre?", "What's your favourite film genre?", "What's your favourite song genre?"]
                colours = ["Red", "Green", "Blue", "Orange", "Brown", "Purple"]
                foods = ["Pizza", "Pasta", "Burger", "Steak", "Soup", "Sandwich"]
                desserts = ["Chocolate", "Ice Cream", "Cake", "Donuts", "Candy", "Lollipop"]
                animals = ["Dog", "Cat", "Bird", "Fish", "Turtle", "Rabbit"]
                things = ["Reading", "Drawing", "Talking to people", "Playing Games", "Watching TV", "Listening to Music"]
                genres = ["Horror", "Comedy", "Romance", "Action", "Sci-Fi", "Fantasy"]
                listception = [colours, foods, desserts, animals, things, genres]
                coloursresponse = ["I love red. It's one of my favourite colours. Especially crimson.", "Green is a good colour. It reminds me of nature. Or at least, my notion of it.", "Blue is nice... I can see it through my window every day, and I can see it when I look through myself.", "Orange reminds me of the sunset... What a pretty favourite colour.", "A lot of things are brown... Tree trunks, mud. It's very earthy. It suits you.", "Ah, purple... reminds me of the end of a rainbow. I like it."]
                foodsresponse = ["Pizza is a good food.", "Pasta is a good food.", "Ahhh... I wish I could try a burger... They sound so good!", "Steak is a good food.", "Soup is a good food.", "Sandwich is a good food."]
                dessertsresponse = ["Chocolate is a good dessert.", "Ice Cream is a good dessert.", "Cake is a good dessert.", "Donuts are a good dessert.", "Candy is a good dessert.", "Lollipops are a good dessert."]
                animalsresponse = ["Dogs are good animals.", "Cats are good animals.", "Birds are good animals.", "Fish are good animals.", "Turtles are good animals.", "Rabbits are good animals."]
                thingsresponse = ["Reading is a good thing to do.", "Drawing is a good thing to do.", "Talking to people is a good thing to do.", "Playing Games is a good thing to do.", "Watching TV is a good thing to do.", "Listening to Music is a good thing to do."]
                genresresponse = ["Horror is a good genre.", "Comedy is a good genre.", "Romance is a good genre.", "Action is a good genre.", "Sci-Fi is a good genre.", "Fantasy is a good genre."]
                electricboogaloo = [coloursresponse, foodsresponse, dessertsresponse, animalsresponse, thingsresponse, genresresponse]

                # change this to only ask unasked questions when i can be arsed
                whichquestion = random.choice(questionlist)

                # finds the correct option-choices / Ashley-response list corresponding to the question asked
                correctindex = questionlist.index(whichquestion)
                optionlist = listception[correctindex]
                responselist = electricboogaloo[correctindex]

                # loops through each item in optionlist- currentoption is object
                for index, currentoption in enumerate(optionlist):
                    i = str(index)
                    exec(f"option{i} = currentoption")
                for index, currentresponse in enumerate(responselist):
                    i = str(index)
                    exec(f"response{i} = currentresponse")

            a "Surprise! I'm going to ask you a question instead."

            menu:
                a "[whichquestion]"
                "[option0]":
                    a "[response0]"
                "[option1]":
                    a "[response1]"
                "[option2]":
                    a "[response2]"
                "[option3]":
                    a "[response3]"
                "[option4]":
                    a "[response4]"
                "[option5]":
                    a "[response5]"
                "I don't have a favourite.":
                    a "That's alright. I know I'm your favourite, though. Ahaha."
        label question:
            # this is where the player can ask Ashley a question
            $ global ashley
            menu:
                a "What would you like to know?"
                "What's your favourite colour?":
                    $ ashley.setValue("colour", True)
                    a "If you couldn't tell, I'm rather fond of red and black... Something about it is just so slick!"
                    jump question
                "What's your favourite food?":
                    $ ashley.setValue("food", True)
                    a "Burgers. I can't exactly eat, per se... But I just know it sounds good."
                    jump question
                "What's your favourite dessert/sweets?":
                    $ ashley.setValue("dessert", True)
                    a "I'm not sure I have a favourite, because I can't really eat... But I do like chocolate."
                    jump question
                "What's your favourite animal?":
                    $ ashley.setValue("animal", True)
                    a "Ferrets! They're so cute and fluffy!"
                    show ash laugh
                    a "Didn't expect that, did you?"
                    show ash
                    jump question
                "What's your favourite thing to do?":
                    $ ashley.setValue("thing", True)
                    a "I like to talk to people, and I like to play games- especially slice-of-life story games."
                    jump question
                "What's your favourite genre?":
                    $ ashley.setValue("genre", True)
                    a "I'm not sure I have a favourite, but I do like horror and fantasy."
                    a "Conversely, I'm also very fond of 'My Heart and Other Black Holes', a book by Jasmine Warga."
                    jump question
                "See more questions":
                    jump question_more
        label question_more:
            $ global ashley
            menu:
                a "What would you like to know?"
                "How tall are you?":
                    $ ashley.setValue("tall", True)
                    a "I'm 5'7, which is pretty average."
                "See original questions":
                    jump question

label unlockables:
    # this is where the player can see their unlocked content
    $ global ashley
    $ ashley.getValue("unlockedOutfits")
    a "Welcome to the unlockables menu!"
    # show a menu only showing unlocked outfits, and "default" using a for index, availableOutfits in unlockedOutfits:
                
    jump interact
                
            
            
                
            
    label quiz:
        # quezzies from knowledge gained from convos / asking ashley questions (1/10 chance you get quizzed) (answer correctly and you get relationship points)
        python: 
            quezzies = ["What's my last name?", "Do you remember my creator's favourite song?", "What is the name of Wilbur's band?", "What is my favourite colour?", "What is my favourite food?", "What is my favourite dessert?", "What is my favourite animal?", "What is my favourite thing to do?", "What is my favourite genre?", "How tall am I?",]


    # This ends the game.

    return
