init python:
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
    def greetingSelector():
        global ashley
        relationship = ashley.getValue("relationship")
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
        greeting = random.choice(greetings)
        return greeting

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
        with open(config.gamedir + "/files/" + filename) as rf:
            if text not in rf.read():
                with open(config.gamedir + "/files/" + filename, "a") as af:
                    af.write(text + "\n")
        return
        # contingencies for time of day whether tutorial is completed or not
    def readFile(filename):
        itemList = open(config.gamedir + "/files/" + filename).readlines()
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