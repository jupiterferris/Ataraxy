init python:         
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
            card = Card(cardStats[0], cardStats[1], cardStats[2], cardStats[3], cardStats[4])
            print(card)
            print(card.name)