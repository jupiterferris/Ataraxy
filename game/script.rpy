# cummies :heart_eyes:
# when you bi

# declaring the RenPy speaking characters ("you" is added in meet_ashley)
define a = Character("Ashley")
define nar = Character(what_italic=True)

########## TO DO ##########
# time- add to greeting messages on boot (been a while, good morning etc)
# use seasonal music/skins- check on start to use diff text file
# pick from a menu option of games- hangman, dice game, sudoku, card games/21? jump to python subroutine- you can choose from unlocked games?
# unlockables from criteria, relationship points, and certain events
# text-based adventure game? - choose your own adventure
# add an option for random outfit on startup?
# special item/ easter egg/ relationship points for 3 points in tutorial game?
# bluescreen lmfaoooo
# day structure like animal crossing- morning only activities etc, forces to play at different times etc
# music player- can pick from any seen tracks
# can only play 1 game a day etc
##### Execution Flow #####
# 1. "Start" label
# 2. Branch to meet Ashley -> tutorial if first time, or to "launch" if not
# 3. Once tutorial is completed, branch to "launch" as if it is a cold open.
# 4. "launch" label determines time of day and handles which bg to use based on TOD.
#########################

# IMAGES REFRESH EVERY SECOND! DO NOT USE FUNCTIONS IN IMAGE DECLARATION OR IT WILL LAG HARDER THAN A 2000S PC RUNNING MINECRAFT
init:
    image ash_hair_back:
        f"ash_hair_back_{hairBack}"
    image ash_body:
        f"ash_body_{body}"
    image ash_nails:
        f"ash_nails_{nails}"
    image ash_hair_front:
        f"ash_hair_front_{hairFront}"
    image ash_accessory:
        f"ash_accessory_{accessory}"
    image ash_eyebrows:
        f"ash_eyebrows_{eyebrows}"
    image ash_blink:
        f"ash_eyes_{eyes}"
        pause 8.0
        f"ash_eyes_mid_{eyes}"
        pause 0.1
        f"ash_eyes_close"
        pause 0.5
        f"ash_eyes_mid_{eyes}"
        pause 0.1
        repeat
    image ash_wink:
        f"ash_eyes_wink_right_mid_{eyes}"
        pause 0.1
        f"ash_eyes_wink_right_close_{eyes}"
        pause 0.5
        f"ash_eyes_wink_right_mid_{eyes}"
        pause 0.1
        f"ash_eyes_{eyes}"
    image ash_close:
        f"ash_eyes_{eyes}"
        pause 0.1
        f"ash_eyes_mid_{eyes}"
        pause 0.1
        f"ash_eyes_close"
    image ash_open:
        f"ash_eyes_close"
        pause 0.5
        f"ash_eyes_mid_{eyes}"
        pause 0.1
        f"ash_eyes_{eyes}"
    image ash_laugh:
        f"ash_eyes_mid_{eyes}"
    
    image bg room:
        f"images/bgs/bg {timeOfDay}.png"
    layeredimage gameroom:
        always:
            Solid("#000000", xysize=(1920, 1080))
        group windows:
            attribute normal default:
                "windowback"
            attribute starry:
                "mask_2"
        group bg:
            attribute room default:
                "game room"
    image bg game:
        f"images/bgs/game room.png"
    image tint dark:
        f"images/masks/dark_tint.png"
    # in ascending layer order: Hair back, body, nails, face, eyes, hair front, accessory, eyebrows
    layeredimage ash:
        always:
            "ash_hair_back"
        group torso:
            attribute body default:
                "ash_body"
        group hands:
            attribute nails default:
                "ash_nails"
        group head:
            attribute face default:
                "ash_face"
        group eyes:
            attribute blink default:
                "ash_blink"
            attribute wink:
                "ash_wink"
            attribute close:
                "ash_close"
            attribute open:
                "ash_open"
            attribute laugh:
                "ash_laugh"
        group hairFront:
            attribute front default:
                "ash_hair_front"
        group hairTop:
            attribute accessory:
                "ash_accessory"
        group eyebrows:
            attribute eyebrows default:
                "ash_eyebrows"  
# declaring functions
init -1 python:
    import json
    import os
    import random
    from datetime import date
    from datetime import datetime
init python:
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
                self.setValue("outfit", ["00", "00", "00", "00", "00", "00", "00"])

            # Relationship with Ashley
            relationship = self.json.get("relationship")
            if relationship is None:
                self.setValue("relationship", 0)

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

            # Cosmetics unlocked for Ashley, given in lists of order (hairBack, body, nails, eyes, hairFront, accessory, eyebrows)
            cosmetics = self.json.get("cosmetics")
            if cosmetics is None:
                self.setValue("cosmetics", [["00"], ["00"], ["00"], ["00"], ["00"], ["00"], ["00"]])
        # Opens the JSON file
        def open(self):
            try:
                with open(self.filename, "r") as f:
                    try:
                        self.json = json.load(f)
                    except:
                        self.json = {}
            except:
                self.json = {}
        # Gets stored value from JSON
        def getValue(self, key):
            return self.json.get(key)
        # Sets value to JSON
        def setValue(self, key, value):
            self.json[key] = value
            dump = json.dumps(self.json)
            with open(self.filename, "w+") as f:
                f.write(dump)
    class Card:
        def __init__(self, name, power, health, cost, ability):
            self.name = name
            self.power = power
            self.health = health
            self.cost = cost
            self.ability = ability
        def __str__(self):
            cardDetails = [self.name, self.power, self.health, self.cost]
            return str(cardDetails)
        
    # setup all main functions with permanent data i.e all collectibles
    def initJams():
        global allSongs
        allSongs = {
            "Wilbur Soot" : {
                "The E-Girl Trilogy" : ("I'm In Love With An E-Girl", "Internet Ruined Me", "Your New Boyfriend"),
                "Your City Gave Me Asthma" : ("Jubilee Line", "Saline Solution", "Your Sister Was Right", "Losing Face", "Since I Saw Vienna", "La Jolla", "I'm Sorry Boris"),
                "Maybe I Was Boring" : ("Maybe I Was Boring", "For Memories", "White Wine In A Wetherspoons"),
                "unlisted" : ("Soft Boy", "The Nice Guy Ballad")
            },
            "Lovejoy" : {
                "Are You Alright?" : ("Taunt", "One Day", "Sex Sells", "Cause For Concern"),
                "Pebblebrain" : ("Oh Yeah, You Gonna Cry", "Model Buses", "Concrete", "Perfume", "You'll Understand When You're Older", "The Fall", "It's All Futile! It's All Pointless!"),
                "covers" : ("Knee Deep At ATP", "Privately Owned Spiral Galaxy")
            },
            "James Marriott" : { 
                "secret" : ("Grapes")
            },
            "a very talented team" : {
                "misc songs" : ("Rose's Fountain", "Lily Flower")
            }
        }
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
        if len(ashley.getValue("cosmetics")) > 1:
            #make this say outfit name eventually
            quizdict["outfit"] = f"Do you remember when you unlocked the {random.choice(ashley.getValue('cosmetics'))} outfit?"
    def initUnoReverse():
        global playerQuestions
        playerQuestions = {
            "What's your favourite colour?" : {
                "Red" : "I love red. It's one of my favourite colours. Especially crimson.",
                "Purple" : "Ah, purple... reminds me of the end of a rainbow. I like it.",
                "Green" : "Green is a good colour. It reminds me of nature. Or at least, my notion of it.",
                "Blue" : "Blue is nice... I can see it through my window every day, and I can see it when I look through myself.",
                "Orange" : "Orange reminds me of the sunset... What a pretty favourite colour.",
                "Brown" : "A lot of things are brown... Tree trunks, mud. It's very earthy. It suits you."
            },
            "What's your favourite dessert?" : {
                "Chocolate" : "",
                "Ice cream" : "",
                "Cake" : "",
                "Donuts" : "",
                "Sweets" : "",
                "Pie" : ""
            },
            "What's your favourite drink?" : {
                "Water" : "",
                "Tea" : "",
                "Coffee" : "",
                "Juice" : "",
                "Milk" : "",
                "Fizzy drinks" : ""
            },
            "What's your favourite season?" : {
                "Spring" : "",
                "Summer" : "",
                "Autumn" : "",
                "Winter" : "",
                "All of them" : "",
                "None of them" : ""
            },
            "What's your favourite holiday?" : {
                "Christmas" : "",
                "Halloween" : "",
                "Easter" : "",
                "New Year" : "",
                "Valentine's Day" : "",
                "Thanksgiving" : ""
            },
            "What's your favourite fruit?" : {
                "Apple" : "",
                "Banana" : "",
                "Orange" : "",
                "Pear" : "",
                "Grapes" : "",
                "Strawberry" : ""
            },
            "What's your favourite thing to do?" : {
                "Listen to music" : "",
                "Play video games" : "",
                "Watch TV" : "",
                "Read" : "",
                "Go outside" : "",
                "Sleep" : ""
            },
            "What's your favourite genre?" : {
                "Horror" : "",
                "Romance" : "",
                "Comedy" : "",
                "Action" : "",
                "Drama" : "",
                "Mystery" : ""
            }
        }
    def initWardrobe():
        global cosmeticsAll
        cosmeticsAll = {
            "hairBackAll" : {
                "00" : "Black Bob",
                "01" : "Miss Aiko"
            },
            "bodyAll" : {
                "00" : "Casual Friday",
                "01" : "I Like Dogs",
                "02" : "A Thousand Paper Cranes",
                "03" : "Sweater Weather"
            },
            "nailsAll" : {
                "00" : "Noire",
                "01" : "Thirium Blue",
                "02" : "Laceration",
                "03" : "Natural"
            },
            "eyesAll" : {
                "00" : "Slate Grey"
            },
            "hairFrontAll" : {
                "00" : "Sideswept Crimson",
                "01" : "Emo Streak",
                "02" : "Sumsar",
                "03" : "William Eyebrows",
                "04" : "Depression & Pronouns",
                "05" : "Sweet Tangerine",
                "06" : "Bodacious Babe",
            },
            "accessoryAll" : {
                "00" : "None",
                "01" : "MonoMono Pin",
                "02" : "Oh Lardy",
                "03" : "Thorny Rose",
            },
            "eyebrowsAll" : {
                "00" : "Thinly Veiled",
            }
        }
    def initCards():
        cardList = readFile("cardList.txt")
        for card in cardList:
            cardStats = card.split(",")
            if len(cardStats) != 5:
                print("Error: Card list is not formatted correctly.")
                continue
            card = Card(cardStats[0], cardStats[1], cardStats[2], cardStats[3])
            print(card)
            print(card.name)
        
    # situational functions used as a specific part of a label
    def namePlayer():
        global ashley
        global name
        name = renpy.input(_("Enter your name."))
        name = name.strip() or __("Babes")
        lowerName = name.lower()
        nameContingencies(lowerName)
        ashley.setValue("name", name)
    def nameContingencies(lowerName):
        if lowerName == "daddy":
            name = "Master Hardwick"
        elif lowerName == "raffi" or name.lower() == "raf" or name.lower() == "gearloe":
            a("Well, well, well... I knew this day would come.")
            a("Finally, a worthy adversary. Our battle will be legendary!")
            renpy.show("ash laugh")
            a("...love you xx :)")
            renpy.show("ash")
        elif lowerName == "bibblyboy":
            renpy.show("ash laugh")
            a("I love men.")
            renpy.show("ash")
        elif lowerName == "pipster":
            a("Fuck, this is painful, isn't it?")
            renpy.show("ash laugh")
            a("It's okay, it might work this time!")
            renpy.show("ash blink")
    def jamSelector(selectionMethod):
        global songsPlayed
        renpy.music.stop(fadeout=3.0)
        numOfJams = len(readFile("tunes.txt"))
        numOfHeard = len(readFile("heardSongs.txt"))
        if selectionMethod == "previous":
            chosenTrack = getPreviousSong(songsPlayed)
            songsPlayed = songsPlayed[:-1]
        elif selectionMethod == "specific":
            a(f"Number of songs heard: {numOfHeard}/{numOfJams}")
            chosenTrack = getSpecificSong()
        else:
            a(f"Number of songs available: {numOfJams}")
            chosenTrack = getRandomSong(songsPlayed)
        a(f"Track chosen: {chosenTrack}")
        renpy.music.play(f"audio/jams/{chosenTrack}.mp3")
        writeToFile("heardSongs.txt", chosenTrack)
        songsPlayed.append(chosenTrack)
        songsPlayed = songsPlayed[-5:]
        print(songsPlayed)
        jamContingencies(chosenTrack)
        getTrackDetails(chosenTrack)
    def jamContingencies(chosenTrack):
        if chosenTrack == "Knee Deep At ATP":
            renpy.show("ash laugh")
            a("You lucky thing, that's my creator's favourite song!")
            addQuizTopic("ATP")
            renpy.show("ash")
        elif chosenTrack == "Soft Boy":
            a("Fun fact- this is actually the main menu song!")
            addQuizTopic("SoftBoy")
    def wardrobe():
        global ashley
        # order hairBack, body, nails, eyes, hairFront, accessory, eyebrows
        cosmetics = ashley.getValue("cosmetics")
        for outfit in cosmetics:
            for key, value in wardrobe.items():
                if outfit == key:
                    wardrobe[key] = value
    # useful, commonly used functions
    def zeldaRiff(cosmeticType, cosmeticNo):
        global ashley
        cosmeticTypes = ["hairBack", "body", "nails", "eyes", "hairFront", "accessory", "eyebrows"]
        cosmeticIndex = cosmeticTypes.index(cosmeticType)
        cosmeticName = getCosmeticName(cosmeticType, cosmeticNo)
        cosmetics = ashley.getValue("cosmetics")
        if cosmeticNo in cosmetics[cosmeticIndex]:
            renpy.show("ash laugh")
            a(f"You cheeky fucker, you already have '{cosmeticName}'!")
            renpy.show("ash blink")
        else:
            cosmetics[cosmeticIndex].append(cosmeticNo)
            ashley.setValue("cosmetics", cosmetics)
            renpy.play("audio/itemget.mp3")
            nar(f"You unlocked the '{cosmeticName}' cosmetic! Visit the unlockables menu to equip it!")
    def writeToFile(filename, text):
        with open(config.gamedir + "/" + filename) as rf:
            if text not in rf.read():
                with open(config.gamedir + "/" + filename, "a") as af:
                    af.write(text + "\n")
        return
        # contingencies for time of day whether tutorial is completed or not
    def readFile(filename):
        itemList = open(config.gamedir + "/" + filename).readlines()
        for index, item in enumerate(itemList):
            itemList[index] = item.replace("\n", "")
        return itemList
    def addQuizTopic(topicToAdd):
        global ashley
        quizTopics = ashley.getValue("quizTopics")
        if not topicToAdd in quizTopics:
            quizTopics.append(topicToAdd)
            ashley.setValue("quizTopics", quizTopics)
        else:
            renpy.show("ash laugh")
            a("But, you already know about that.")
            renpy.show("ash blink")
    def inputQuestion(question, correctAnswer):
        global points
        a(f"{question}")
        answer = renpy.input("Enter your answer.").strip().lower()
        if answer == correctAnswer.lower():
            points += 1
            a("Correct! You get a point.")
        else:
            a("Incorrect. You don't get a point.")
        a(f"You have {points} {getCorrectNoun()}.")
    def menuQuestion(question, correctAnswer, options):
        global points
        a(f"{question}", interact=False)
        answer = renpy.display_menu(options)
        if answer == correctAnswer:
            points += 1
            a("Correct! You get a point.")
        else:
            a("Incorrect. You don't get a point.")
        a(f"You have {points} {getCorrectNoun()}.")   
    def menuFormat(options):
        formattedOptions = []
        for option in options:
            formattedOptions.append((option, option))
        return formattedOptions
    # sets time for bg from time of day/ tutorial status    
    def setBG():
        global ashley
        global timeOfDay
        if ashley.getValue("name") == "" or ashley.getValue("tutorialCompleted") == False:
            timeOfDay = "day"
        else:
            getTimeOfDay()
    # getting variables from other functions
    def getAshBasics():
        global ashley
        global hairBack
        global body
        global nails
        global hairFront
        global accessory
        global eyebrows
        global eyes
        global tutorialCompleted
        global name
        global relationship
        outfit = ashley.getValue("outfit")
        # (hairBack, body, nails, eyes, hairFront, accessory, eyebrows)
        hairBack = outfit[0]
        body = outfit[1]
        nails = outfit[2]
        eyes = outfit[3]
        hairFront = outfit[4]
        accessory = outfit[5]
        eyebrows = outfit[6]
        tutorialCompleted = ashley.getValue("tutorialCompleted")
        name = ashley.getValue("name")
        relationship = ashley.getValue("relationship")
    def getCorrectNoun():
        global points
        if points == 1:
            return "point"
        else:
            return "points"
    def getCosmeticName(cosmeticType, cosmeticNo):
        global cosmeticsAll
        dictName = cosmeticType + "All"
        return cosmeticsAll[dictName][cosmeticNo]
    def getTrackDetails(chosenTrack):
        global allSongs
        global albumName
        global artistName
        global trackNo
        global currentTrack
        currentTrack = chosenTrack
        albumName = None
        artistName = None
        trackNo = None
        # find album name, track number
        for key, value in allSongs.items():
            for album, songs in value.items():
                if currentTrack in songs:
                    artistName = key
                    albumName = album
                    trackNo = songs.index(currentTrack) + 1
                
        # error catching (incase i add new tracks and forget to add to the dictionary)
        if artistName is None:
            albumName = "Unknown"
            trackNo = "N/A"
            artistName = "Unknown"
    def getRandomSong(songsPlayed):
        chosenTrack = random.choice(readFile("tunes.txt"))
        try:
            if chosenTrack == songsPlayed[-1]:
                a(f"Oops! I was going to play {songsPlayed[-1]}, but you just heard that one!")
                getRandomSong(songsPlayed)
        except IndexError:
            pass
        return chosenTrack
    def getPreviousSong(songsPlayed):
        if len(songsPlayed) < 2:
            a("No other songs played yet! Come back once you've heard some jams.")
        return songsPlayed[-1]
    def getSpecificSong():
        specificSong = renpy.display_menu(menuFormat(readFile("heardSongs.txt")))
        return specificSong


    # API functions
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
    # declaring all the variables for use in the game, startup defaults etc, calling all init functions
    def bootGame():
        global ashley
        global wilburText
        global tutorialGameCompleted
        global tutorialConvoCompleted
        global outfitchanged
        global songsPlayed
        ashley = CharacterManager()
        wilburText = False
        tutorialGameCompleted = False
        tutorialConvoCompleted = False
        outfitchanged = False
        songsPlayed = []
        getAshBasics()
        setBG()
        initJams()
        initWardrobe()
        initUnoReverse()
        initCards()
# what the game does on bootup
label start:
    # this is the intro- also serves as initial loading progress.
    stop music fadeout 1.0 
    python:
        bootGame()
        print(f"In-game time of day: {timeOfDay}")
        print(f"Name in file: {name}\nRelationship level {relationship}\nTutorial done? {tutorialCompleted}\n")
        if not tutorialCompleted and name != "":
            renpy.jump("init_tutorial")
        elif name == "":
            renpy.jump("meet_ashley")
    scene bg room
    show ash blink
    with fade
    $ jamSelector("random")

    # DEBUGGING
    #stop music fadeout 6.0
    #a "Wait... something's not right..."
    #a "I can't..."
    #a "Can you hear me?"
    #a "Please help me."
    #jump gayme
    #a "Approaching hyperspeed!"
    #jump popquiz
    # \DEBUGGING
    jump launch
# the precursor to the tutorial, only shown at the very beginning of the game. This is where the player inputs their name
label meet_ashley:
    scene bg room
    show ash close
    with fade
    nar "Performing first time setup..."
    show ash open
    play music "audio/jams/Lily Flower.mp3"
    show ash blink
    $ writeToFile("heardSongs.txt", "Lily Flower\n")
    a "Hello. I'm Ashley. I'm a virtual girlfriend."
    show ash wink
    a "{i}Your{/i} virtual girlfriend."
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
    scene bg room
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
            jump tutorial_pick_convo
            #exclusive outfits from listening to stories- picked at random or user input- option removed from list after use.
        "Where am I up to?":
            python:
                if tutorialGameCompleted and tutorialConvoCompleted:
                    a("Welcome back!")
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
        # resets point value to 0, good form incase for whatever reason it isn't already 0
        $ points = 0
        a "I'm going to ask you a question, and you have to answer it."
        a "If you get it right, you get a point."
        a "If you get it wrong, you don't."
        show ash laugh
        a "Let's start with an easy one."
        show ash blink
        $ inputQuestion("What's my name?", "Ashley")
        a "Let's try another one."
        $ menuQuestion("What's my favorite color?", "r", [("Red", "r"), ("Blue", "b"), ("Green", "g"), ("Yellow", "y")])
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

    label tutorial_pick_convo:
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
# normal game start provided tutorial is completed
label launch:
    # this is where the player will be taken on launch after the tutorial is complete
    python:
        getAshBasics()
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
        a("Event value = [event]")
        if event == 1:
            a("I'm sorry, I'm not feeling well today. I'll be back next time.")
            renpy.show ("ash close")
            renpy.jump("quit")
        elif event > 90:
            a("Let me ask you something...")
        #    menu:
        #        a "How's your day been?"
        #        "Great!":
        #        "It's been alright.":
        #        "Not so good.":
    jump interact
# main interaction menu with Ashley, where you choose what to do
label interact:
    # this is where the player can interact with Ashley
    # you can play a game, chat, or go to the unlockables menu

    menu:
        a "So what do you want to do?"
        "Let's play a game.":
            jump gayme
        "Let's chat.":
            jump conversation
        "Where am I up to?":
            # move this to unlockables as menu
            a "Looking for an outfit change? Variety is the spice of life, after all."
            jump unlockables
# chat section of Ashley interaction
label conversation:
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
    # this is where Ashley tells the player what song is playing and more information about it
    label convo_song:
        python:  
            a(f"The current song playing is {currentTrack}, by {artistName}.")
            if not wilburText and (artistName == "Wilbur Soot" or artistName == "Lovejoy"):
                wilburText = True
                a("The person who coded this really loves Wilbur Soot's music... Ahaha.")
                a("Can't say I blame her... He's quite something. Don't you agree?")
                if "wilbur" in ashley.getValue("quizTopics"): 
                    renpy.show("ash laugh")
                    a("But you've already heard this before, haven't you?")
                    renpy.show("ash blink")
                    a("In another session, I mean.")
                else:    
                    addQuizTopic("wilbur")
                    renpy.show("ash laugh") 
                    a("What am I saying, of course you do.")
                    renpy.show("ash blink")
            else:
                a("I'm glad you like it.")
        menu:
            "Can I hear some more?":
                a "Of course you can. Did you have anything specific in mind?"
                $ randomSong = False
                menu:
                    "Random song, please!":
                        a "Invoking RNGesus..."
                        $ jamSelector("random")
                        $ randomSong = True
                        
                    "Can I have the previous song?":
                        a "Let's see..."
                        $ jamSelector("previous")
                    "Actually, I'd like something specific.":
                        a "Alright, let's see what you've heard."
                        $ jamSelector("specific")
                    "Never mind, this song is fine.":
                        a "No worries. I'll leave it as it is."
                a "Anything else?"
                label song_pick_loop:
                    menu:
                        "Another! Let's keep this train rolling." if randomSong:
                            python:
                                responses = ["And so it shall be.",
                                            "Anything for you...",
                                            "I don't think so. Haha, just kidding!",
                                            f"Sure thing, {name}."]
                                retort = random.choice(responses)
                                a("[retort]")
                                jamSelector("random")
                            jump song_pick_loop
                        "Based. I'll stick with this one.":
                            a "Have fun~"
                            jump conversation
                        "Which song is this again?":
                            jump tellmemore

            "Alright cool. Love it.":
                a "My pleasure. Come back anytime if you want to hear something new~"
                jump conversation
            "Tell me more about this song.":
                label tellmemore:
                    a "This is Enjoyer Of Things' piano cover of [currentTrack], track [trackNo] from [albumName], by [artistName]."
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
                            show ash blink
                            python: 
                                if not "grapes" in ashley.getValue("quizTopics"):
                                    addQuizTopic("grapes")
                                    writeToFile("tunes.txt", "Grapes\n")
                                    a("As a thank you for listening to my rambling, I've unlocked a secret track for you.")
                                    a("It's a lesser-known song by James Marriott that was made collaboratively with Ash Kabosu- Lovejoy's bass guitarist.")
                                    a("Enjoy~")
                                else: 
                                    a("I was going to give you a secret track as thanks, but it appears you've already unlocked it.")
                                    renpy.show("ash laugh")
                                    a("Did you hope I would give you another one? Haha, sorry. You only get the one.")         
                                    renpy.show("ash blink")       
                            jump song_pick_loop
                        "No thanks.":
                            a "As you wish."
                            jump song_pick_loop
    
    # this is where Ashley picks a conversation topic for you
    label convo_ashchoice:
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
            
               

                # change this to smth in json when i can be bothered
                #whichquestion = random.choice(questionlist)
                #questionlist -= whichquestion

                # finds the correct option-choices / Ashley-response list corresponding to the question asked
                #correctindex = questionlist.index(whichquestion)
                #optionlist = listception[correctindex]
                #responselist = electricboogaloo[correctindex]

                # loops through each item in optionlist- currentoption is object
                #for index, currentoption in enumerate(optionlist):
                #    i = str(index)
                #    exec(f"option{i} = currentoption")
                #for index, currentresponse in enumerate(responselist):
                #    i = str(index)
                #    exec(f"response{i} = currentresponse")

            a "Surprise! I'm going to ask you a question instead."
            $ global ashley
            $ unlocked = ashley.getValue("cosmetics")
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
                    show ash blink
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
                unlocked = ashley.getValue("cosmetics")
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
                        topicList = topicList.append(topic)
                    renpy.say(a, f"{', '.join(topicList)}")
                renpy.jump("unlockables")
        "Pictures, please!":
            jump gallery
        "All done!":
            jump interact
    # have a You Choose! option where she picks an unlocked outfit at random
    # show a menu only showing unlocked outfits, and "default" using a for index, availableOutfits in cosmetics:

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
        a(f"{random.choice(quizopener)}")

        initQuiz()

        if initQuiz():
            renpy.say (a, "Actually, I don't think you've learned anything from me yet. Come back later!")
            renpy.jump("question")

        renpy.say(a, f"{random.choice(list(quizdict.values()))}")

label gayme:
    scene gameroom
    show ash blink
    with fade 
    play music "audio/jams/Your Reality.mp3"
    a "Welcome to the game room!"
    
# This ends the game.
return
