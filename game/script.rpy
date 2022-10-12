# cummies :heart_eyes:

define a = Character("Ashley")
define nar = Character(what_italic=True)


##### TO DO #####

# figure out how to import time- add to greeting messages on boot (been a while, good morning etc)
# player input option(?)
# use seasonal music/skins- check on start to use diff text file
# random event on startup - how was your day? long time no see?
# pick from a menu option of games- hangman, dice game, sudoku, card games/21? jump to python subroutine- you can choose from unlocked games?
# winning games gives you relationship points- points can be used on unlockables at threshold. unlockable outfits based on criteria met?
# text-based adventure game? - choose your own adventure
# add an option for random outfit on startup?
# special item/ easter egg/ relationship points for 3 points in tutorial game?
# bluescreen lmfaoooo
# do something with outfit cheatsheet
# when you bi
# day structure like animal crossing- morning only activities etc, forces to play at different times etc

####################

##### Execution Flow #####
# 1. "Start" label
# 2. Branch to meet Ashley -> tutorial if first time, or to "launch" if not
# 3. Once tutorial is completed, branch to "launch" as if it is a cold open.
# 4. "launch" label determines time of day and handles which bg to use based on TOD.
####################

# declaring renpy variables (ashley)
# IMAGES REFRESH EVERY SECOND! USE FOR BACKGROUND CHANGES
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
    image bg room:
        f"images/bgs/bg {timeOfDay}.png"

# declaring functions
init python:
    import json
    import os
    from datetime import date
    from datetime import datetime
    # JSON handler
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

            # Relationship with Ashley
            relationship = self.json.get("relationship")
            if relationship is None:
                self.setValue("relationship", 0)

            # Ashley's unlocked outfits
            unlockedOutfits = self.json.get("unlockedOutfits")
            if unlockedOutfits is None:
                self.setValue("unlockedOutfits", ["00"])

            # Tutorial completed?
            tutorialCompleted = self.json.get("tutorialCompleted")
            if tutorialCompleted is None:
                self.setValue("tutorialCompleted", False)

            # Unlocked quiz topics
            quizTopics = self.json.get("quizTopics")
            if quizTopics is None:
                self.setValue("quizTopics", [])

            # Last time the player logged on
            lastPlayed = self.json.get("lastPlayed")
            if lastPlayed is None:
                self.setValue("lastPlayed", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            
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
    # music player
    def jams(name, **kwargs):
        global ashley
        global chosentrack
        global ATP_played
        import random
        global albumname
        global trackno
        global artist
        egirltrilogy = ("I'm In Love With An E-Girl", "Internet Ruined Me", "Your New Boyfriend")
        ycgma = ("Jubilee Line", "Saline Solution", "Your Sister Was Right", "Losing Face", "Since I Saw Vienna", "La Jolla", "I'm Sorry Boris")
        areyoualright = ("Taunt", "One Day", "Sex Sells", "Cause For Concern")
        pebblebrain = ("Oh Yeah, You Gonna Cry", "Model Buses", "Concrete", "Perfume", "You'll Understand When You're Older", "The Fall", "It's All Futile! It's All Pointless!")
        maybeiwasboring = ("Maybe I Was Boring", "For Memories", "White Wine In A Wetherspoons")
        covers = ("Knee Deep At ATP", "Privately Owned Spiral Galaxy")
        unlisted = ("Soft Boy", "The Nice Guy Ballad")
        secret = ("Grapes")
        lastplayedsong = chosentrack
        renpy.music.stop(fadeout=3.0)
        file = renpy.open_file("tunes.txt")
        songs = file.readlines()
        numofjams = len(songs)
        a(f"Number of songs available: {numofjams}")
        randomsong = random.choice(songs).decode()
        chosentrack = randomsong.replace("\r\n","")
        if chosentrack == lastplayedsong:
            renpy.say(a, f"Oops! I was going to play {lastplayedsong}, but that was already playing!")
            jams("")
        else:
            a(f"Track chosen: {chosentrack}")
            renpy.music.play(f"audio/jams/{chosentrack}.mp3")
        if chosentrack == "Knee Deep At ATP":
            renpy.show("ash laugh")
            renpy.say(a, "You lucky thing, that's my creator's favourite song!")
            addQuizTopic("ATP")
            renpy.show("ash")
        elif chosentrack == "Soft Boy":
            renpy.say(a, "Fun fact- this is actually the main menu song!")
            addQuizTopic("SoftBoy")
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
    # item get sound
    def zeldaRiff(outfitname, outfitno):
        global ashley
        if outfitno in ashley.getValue("unlockedOutfits"):
            renpy.show("ash laugh")
            renpy.say(a, "You cheeky fucker, you already have that outfit!")
            renpy.show("ash")
        else:
            ashley.setValue("unlockedOutfits", ashley.getValue("unlockedOutfits").append(outfitno))
            renpy.play("audio/getitem.mp3")
            renpy.say(nar, f"You unlocked the {outfitname} outfit! Visit the unlockables menu to equip it!")
    # add quiz topic to JSON
    def addQuizTopic(topicToAdd):
        global ashley
        ashley.setValue("quizTopics", ashley.getValue("quizTopics") + [topicToAdd])
    # setup quiz
    def initQuiz():
        # change "quizTopics" to the question strings
        global ashley
        global quizdict
        quizTopics = ashley.getValue("quizTopics")
        if len(quizTopics) == 0:
            return True
        topics = ("surname", "ATP", "SoftBoy", "grapes", "colour", "food", "dessert", "animal", "thing", "genre", "tall")
        answers = ("Rosemarry", "Knee Deep At ATP", "Soft Boy", "Grapes", "Red", "")
        #for topics in quizTopics:
        #    quizdict[topics] = 
        if "surname" in quizTopics:
            quizdict["surname"] = "What's my last name?"
        if "ATP" in quizTopics:
            quizdict["ATP"] = "Do you remember my creator's favourite song?"
        if "SoftBoy" in quizTopics:
            quizdict["SoftBoy"] = "Do you know the name of the main menu song?"
        if "wilburTextHeard" in quizTopics:
            quizdict["wilburTextHeard"] = "What is the name of Wilbur Soot's band?"
        if "grapes" in quizTopics:
            quizdict["grapes"] = "Do you remember how you unlocked 'Grapes'?"
        if "colour" in quizTopics:
            quizdict["colour"] = "What's my favourite colour?"
        if "food" in quizTopics:
            quizdict["food"] = "What's my favourite food?"
        if "dessert" in quizTopics:
            quizdict["dessert"] = "What's my favourite dessert/sweets?"
        if "animal" in quizTopics:
            quizdict["animal"] = "What's my favourite animal?"
        if "thing" in quizTopics:
            quizdict["thing"] = "What's my favourite thing to do?"
        if "genre" in quizTopics:
            quizdict["genre"] = "What's my favourite genre?"
        if "tall" in quizTopics:
            quizdict["tall"] = "How tall am I?"
        if len(ashley.getValue("unlockedOutfits")) > 1:
            #make this say outfit name eventually
            quizdict["outfit"] = f"Do you remember when you unlocked the {random.choice(ashley.getValue('unlockedOutfits'))} outfit?"
    # setup character customisation menu
    def initWardrobe():
        #fucking change this whole thing like do i want unlocked outfits to be a list or a dict- list = out of order but implement sort?
        global ashley
        global wardrobe
        unlockedOutfits = ashley.getValue("unlockedOutfits")
        wardrobe.append = "Default"
        if 01 in unlockedOutfits:
            wardrobe.append = "MonoMono Pin"
        if 02 in unlockedOutfits:
            wardrobe.append = "William Eyebrows"
        if 03 in unlockedOutfits:
            wardrobe.append = "Depression & Pronouns"
        if 04 in unlockedOutfits:
            wardrobe.append = "Sweet Tangerine"
        if 05 in unlockedOutfits:
            wardrobe.append = "Bodacious Babe"
        if 06 in unlockedOutfits:
            wardrobe.append = "Sumsar"
    # write to a file         
    def writeToFile(filename, text):
        with open(config.gamedir + "/" + filename, "a") as f:
            f.write(text)
        return
    # declaring all the variables for use in the game, startup defaults etc
    def initGame():
        global ashley
        global wilburtext
        global outfit
        global chosentrack
        global tutorialGameCompleted
        global tutorialConvoCompleted
        global outfitchanged
        global quizdict
        global wardrobe
        ashley = CharacterManager()
        chosentrack = "Soft Boy"
        wilburtext = False
        tutorialGameCompleted = False
        tutorialConvoCompleted = False
        outfitchanged = False
        quizdict = {}
        wardrobe = []
        getAshBasics()
        setBG()
    def setBG():
        global ashley
        global timeOfDay
        if ashley.getValue("name") == "" or ashley.getValue("tutorialCompleted") == False:
            timeOfDay = "day"
        else:
            getTimeOfDay()
    def getAshBasics():
        global ashley
        global outfit
        global tutorialCompleted
        global name
        global relationship
        outfit = ashley.getValue("outfit")
        tutorialCompleted = ashley.getValue("tutorialCompleted")
        name = ashley.getValue("name")
        relationship = ashley.getValue("relationship")
    # get Lat/Lon for use with sunrise/sunset API
    def getLocation():
        try:
            ipRequest = requests.get('https://ipwho.is')
            if ipRequest.status_code != 200:
                print("Error making request!")
                return
            json = ipRequest.json()
            return (json["latitude"], json["longitude"])
        except:
            print("IP could not be retrieved! Are you using a VPN?")
            return (53.3676, 3.1626)

    # get sunrise/sunset times for use with getTimeOfDay
    def getTimeBounds():
        lat, lon = getLocation()
        queryParameters = {
            "lat": lat,
            "lon": lon
        }
        try:
            boundsRequest = requests.get("https://api.sunrise-sunset.org/json", params=queryParameters)
            json = boundsRequest.json()
            results = json["results"]
            sunrise = results["sunrise"]
            sunset = results["sunset"]
            noon = results["solar_noon"]
        except:
            print("Local day cycle unavailable! Using default values.")
            sunrise = "06:00:00 AM"
            sunset = "06:00:00 PM"
            noon = "12:00:00 PM"

        return (sunrise, sunset, noon)

    # use current time and sunrise/sunset times to determine time of day
    def getTimeOfDay():
        global timeOfDay
        currentTime = datetime.now().strftime("%H:%M:%S")
        midnightTime = datetime.now().replace(hour=0, minute=0, second=0).strftime("%H:%M:%S")
        sunrise, sunset, noon = getTimeBounds()
        sunriseTime = datetime.strptime(sunrise, "%I:%M:%S %p").strftime("%H:%M:%S")
        sunsetTime = datetime.strptime(sunset, "%I:%M:%S %p").strftime("%H:%M:%S")
        noonTime = datetime.strptime(noon, "%I:%M:%S %p").strftime("%H:%M:%S")
        print(f"Current time: {currentTime}")
        print(f"Sunrise today: {sunriseTime}")
        print(f"Sunset today: {sunsetTime}")
        print(f"Noon today: {noonTime}")
        # [midnight] | morning | [sunrise] | day | [noon] | afternoon | [sunset] | night | [midnight]
        if currentTime > midnightTime and currentTime < sunriseTime:
            timeOfDay = "morning"
        elif currentTime > sunriseTime and currentTime < noonTime:
            timeOfDay = "day"
        elif currentTime > noonTime and currentTime < sunsetTime:
            timeOfDay = "afternoon"
        else:
            timeOfDay = "night"
        print(f"Time of day: {timeOfDay}")

# The game starts here.

# what the game does on bootup
label start:
    # this is the intro- also serves as initial loading progress.
    stop music fadeout 1.0

    $ global timeOfDay
    $ initGame()
    $ print(f"In-game time of day: {timeOfDay}")
    scene bg room

    show ash close
    with fade

    a "Initialising..."

    $ jams("")

    show ash open

    # DEBUGGING

    #a "Name in file = [name]. Relationship level [relationship]. Tutorial done? [tutorialCompleted]."

    #a "Approaching hyperspeed!"
    #jump popquiz

    # \DEBUGGING

    python:
        if tutorialCompleted and name != "":
            renpy.jump("launch")
        elif not tutorialCompleted and name != "":
            renpy.jump("tutorial")
        else:
            renpy.jump("meet_ashley")

# the precursor to the tutorial, only shown at the very beginning of the game
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

# tutorial game
label tutorial:
    # this is the tutorial run from a preset set of events
    #python:
    #    global ashley
    #    global tutorialGameCompleted
    #    global tutorialConvoCompleted
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
                    ashley.setValue("tutorialCompleted", True)
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
                renpy.play("audio/itemget.mp3")
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
                $ ashley.setValue("outfit", "01")
                $ outfit = ashley.getValue("outfit")
                $ outfitchanged = True
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

# normal game start provided tutorial is completed
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
        renpy.say(a, f"{random.choice(greetings)}")

        renpy.jump("random_events")

# decides what extra events will be played before the player gets control
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

# main interaction menu with Ashley
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

# chat section of Ashley interaction
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
                ashley.setValue("wilburTextHeard", True)
                renpy.say(a, "The person who coded this really loves Wilbur Soot's music... Ahaha.")
                renpy.say(a, "Can't say I blame her... He's quite something. Don't you agree?")
                # if the player says yes, they get a special outfit?
                if ashley.getValue("wilburTextHeard"): 
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
                                if not "grapes" in ashley.getValue("quizTopics"):
                                    addQuizTopic("grapes")
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
        convotopics = ["anecdote", "question", "poem", "gayme"]
        renpy.jump("convo_" + random.choice(convotopics))

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


                # change this to smth in json when i can be bothered
                whichquestion = random.choice(questionlist)
                questionlist -= whichquestion

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
            $ global ashley
            $ unlocked = ashley.getValue("unlockedOutfits")
            menu:
                a "[whichquestion]"
                "[option0]":
                    a "[response0]"
                    python:
                        if whichquestion == questionlist[0]:
                            relationship = ashley.getValue("relationship")
                            relationship += 5
                "[option1]":
                    a "[response1]"
                    python:
                        if whichquestion == questionlist[0]:
                            zeldaRiff("William Eyebrows", "02")
                "[option2]":
                    a "[response2]"
                    python:
                        if whichquestion == questionlist[0]:
                            zeldaRiff("Depressed & Pronouns", "03")
                "[option3]":
                    a "[response3]"
                    python:
                        if whichquestion == questionlist[0]:
                            zeldaRiff("Sweet Tangerine", "04")
                "[option4]":
                    a "[response4]"
                    python:
                        if whichquestion == questionlist[0]:
                            zeldaRiff("Bodacious Babe", "05")
                "[option5]":
                    a "[response5]"
                    python:
                        if whichquestion == questionlist[0]:
                            zeldaRiff("Sumsar", "06")
                "I don't have a favourite.":
                    a "That's alright. I know I'm your favourite, though. Ahaha."

            jump random_events
        label question:
            # this is where the player can ask Ashley a question
            $ global ashley
            menu:
                a "What would you like to know?"
                "What's your favourite colour?":
                    $ addQuizTopic("colour")
                    a "If you couldn't tell, I'm rather fond of red and black... Something about it is just so slick!"
                    jump question
                "What's your favourite food?":
                    $ addQuizTopic("food")
                    a "Burgers. I can't exactly eat, per se... But I just know it sounds good."
                    jump question
                "What's your favourite dessert/sweets?":
                    $ addQuizTopic("dessert")
                    a "I'm not sure I have a favourite, because I can't really eat... But I do like chocolate."
                    jump question
                "What's your favourite animal?":
                    $ addQuizTopic("animal")
                    a "Ferrets! They're so cute and fluffy!"
                    show ash laugh
                    a "Didn't expect that, did you?"
                    show ash
                    jump question
                "What's your favourite thing to do?":
                    $ addQuizTopic("thing")
                    a "I like to talk to people, and I like to play games- especially slice-of-life story games."
                    jump question
                "What's your favourite genre?":
                    $ addQuizTopic("genre")
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
                    $ addQuizTopic("tall")
                    a "I'm 5'7, which is pretty average."
                "See original questions":
                    jump question

# unlockables menu from the interaction menu
label unlockables:
    # this is where the player can see their unlocked content
    $ global ashley
    $ initWardrobe()
    a "Welcome to the unlockables menu!"
    menu:
        a "What would you like to see?"
        "Wardrobe change!":
            python:
                initWardrobe()
                unlocked = ashley.getValue("unlockedOutfits")
                if unlocked == 0:
                    renpy.say(a, "You haven't unlocked any outfits yet!")
                    renpy.jump("unlockables")
                else:
                    renpy.say(a, "You've unlocked the following outfits:")
                    for outfit in unlocked:
                        renpy.say(a, f"{outfit}")
                    renpy.jump("unlockables")
        "What can you quiz me on?":
            python:
                unlocked = ashley.getValue("unlockedQuizTopics")
                if unlocked == 0:
                    renpy.say(a, "You haven't unlocked any quiz topics yet! You're safe for now.")
                    renpy.jump("unlockables")
                else:
                    renpy.say(a, "You've unlocked the following quiz topics:")
                    for topic in unlocked:
                        renpy.say(a, f"{topic}")
                renpy.jump("unlockables")
        "Pictures, please!":
            jump gallery
        "All done!":
            jump interact
    # have a You Choose! option where she picks an unlocked outfit at random
    # show a menu only showing unlocked outfits, and "default" using a for index, availableOutfits in unlockedOutfits:

# 
label popquiz:
    # quezzies from knowledge gained from convos / asking ashley questions (1/10 chance you get quizzed) (answer correctly and you get relationship points)
    python: 
        # have an empty list, with if statements appending to the list.
        global ashley
        import json
        import random
        #quezzietopics = ashley.json.keys()
        quizopener = [
            "I hope you've been paying attention!", 
            "Time to test your knowledge!", 
            "Let's see how well you know me!", 
            "Let's see how much you've been paying attention!", 
            "Let's see how much you've learned!", 
            "Pop quiz!", 
            "Knowledge check!",
            "Think fast!"
        ]
        renpy.say(a, f"{random.choice(quizopener)}")

        initQuiz()

        if initQuiz():
            renpy.say (a, "Actually, I don't think you've learned anything from me yet. Come back later!")
            renpy.jump("question")

        renpy.say(a, f"{random.choice(list(quizdict.values()))}")

    
    
    # This ends the game.
    return
