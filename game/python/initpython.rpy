init python:         
    # setup all main functions with permanent data i.e all collectibles
    def trackInfoAll():
        trackInfo = {
            "Wilbur Soot" : {
                "The E-Girl Trilogy" : ("I'm In Love With An E-Girl", "Internet Ruined Me", "Your New Boyfriend"),
                "Your City Gave Me Asthma" : ("Jubilee Line", "Saline Solution", "Your Sister Was Right", "Losing Face", "Since I Saw Vienna", "La Jolla", "I'm Sorry Boris"),
                "Maybe I Was Boring" : ("Maybe I Was Boring", "For Memories", "White Wine In A Wetherspoons", "It's All Futile! It's All Pointless! Alternative"),
                "The Nice Guy Ballad" : ("The Nice Guy Ballad", "Karen, Please Come Back I Miss The Kids", "I Am Very Smart"),
                "Singles" : ("Soft Boy", "Soft Boy Alternative")
            },
            "Lovejoy" : {
                "Are You Alright?" : ("Taunt", "One Day", "Sex Sells", "Cause For Concern"),
                "Pebblebrain" : ("Oh Yeah, You Gonna Cry", "Model Buses", "Concrete", "Perfume", "You'll Understand When You're Older", "The Fall", "It's All Futile! It's All Pointless!"),
                "covers" : ("Knee Deep At ATP", "Privately Owned Spiral Galaxy")
            },
            "James Marriott" : { 
                "Bitter Tongues" : ("Where Has Everyone Gone", "Gold", "Car Lights", "Sleeping On Trains", "Grapes")
            },
            "Aivi & Surasshu" : {
                "Steven Universe OST" : ("Rose's Fountain")
            },
            "Technoboys Pulcraft Green-Fund" : {
                "Kakegurui OST" : ("Lily Flower")
            },
        }
        return trackInfo
    def quizAll():
        quizQuestions = {
            "surname" : {
                "What is my last name?" : ("Rosemarry", "You don't have one", "Taylor", "Courtney", "Green")
            },
            "ATP" : {
                "Do you remember my creator's favourite song?" : "Knee Deep At ATP"
            },
            "SoftBoy" : {
                "Do you know the name of the main menu song?" : "Soft Boy"
            },
            "wilburTextHeard" : {
                "What is the name of Wilbur Soot's band?" : "Lovejoy"
            },
            "colour" : {
                "What is my favourite colour?" : "Red"
            },
            "animal" : {
                "What is my favourite animal?" : "Ferrets"
            },
            "thing" : {
                "What is my favourite thing to do?" : "Talk to people/ play games"
            },
            "song" : {
                "What is my favourite song?" : "Rose's Fountain"
            },
            "genre" : {
                "What is my favourite genre?" : "Horror/Fantasy"
            },
            "heightp" : {
                "How tall am I?" : "5'7"
            }
        }
        return quizQuestions
        # random chance of getting a "Do you remember how you unlocked..." question
    def aboutPlayerAll():
        aboutPlayerQuestions = {
            "What's your favourite colour?" : {
                "Red" : ("I love red. It's one of my favourite colours. Especially crimson."),
                "Purple" : ("Ah, purple... reminds me of the end of a rainbow. I like it.", "4|02"),
                "Green" : ("Green is a good colour. It reminds me of nature. Or at least, my notion of it.", "4|03"),
                "Blue" : ("Blue is nice... I can see it through my window every day, and I can see it when I look through myself.", "4|04"),
                "Orange" : ("Orange reminds me of the sunset... What a pretty favourite colour.", "4|05"),
                "Brown" : ("A lot of things are brown... Tree trunks, mud. It's very earthy. It suits you.", "4|06"),
            },
            "What's your favourite season?" : {
                "Spring" : ("Spring's great. It's when the flowers bloom, and the birds sing. It's a time of new beginnings."),
                "Summer" : ("Ah, summer. The sun is out, and the days are long."),
                "Autumn" : ("Autumn is a beautiful time of year. The leaves change colour, and the air is crisp. Plus, you can find conkers!"),
                "Winter" : ("Winter is a time of hibernation. It's when the world is at its coldest, and the days are at their shortest. It's a time of reflection."),
                "All of them" : ("They all have their own beauty. I can see why you like them all."),
                "None of them" : ("I get it. They're all so different. Some people don't like change.")
            },
            "What's your favourite holiday?" : {
                "Christmas" : ("Christmas is a time of joy. It's a time of family, and presents, and food. It's so festive!"),
                "Halloween" : ("Halloween is a time of spooks. It's a time of costumes, and candy, and trick-or-treating. It's so spooky!"),
                "Easter" : ("Easter is a time of new life. It's a time of chocolate, and eggs, and bunnies. It's so cute!"),
                "New Year" : ("New Year is a time of new beginnings. It's a time of fireworks, and parties, and resolutions. It's so exciting!"),
                "Valentine's Day" : ("Valentine's Day is a time of love. It's a time of cards, and flowers, and chocolates. It's so romantic!")
            },
            "What's your favourite thing to do?" : {
                "Listen to music" : ("I love a good song. I can listen to them all day long. And I do! I listen to different things when you're not around, though."),
                "Play video games" : ("Video games are great fun. They're a great way to relax, and they're a great way to express yourself."),
                "Watch TV" : ("TV is a classic. It's a great way to unwind- or binge watch an entire show in one day."),
                "Read" : ("Reading is a great way to relax. It's a great way to escape, and it's a great way to learn."),
                "Go outside" : ("Going outside is a great way to get some fresh air. It's a great way to exercise, and it's a great way to see the world."),
                "Sleep" : ("Sleep is a great way to relax. It's a great way to recharge, and can sometimes hold fascinating dreams.")
            },
            "What's your favourite genre?" : {
                "Horror" : ("I can't say I'm a huge fan of horror- not a lot can scare me."),
                "Romance" : ("Sometimes it's nice to get lost in a good romance."),
                "Comedy" : ("There are few things in life that can't be improved by a good laugh."),
                "Action" : ("Action is a great way to get your adrenaline pumping, or escape the mundane."),
                "Drama" : ("Drama is a great way to get your emotions going."),
                "Mystery" : ("Do you ever find yourself guessing the ending of a mystery before it's revealed? I do. I'm not always right, though.")
            }
        }
        return aboutPlayerQuestions
    def aboutAshAll():
        aboutAshQuestions = {
            "colour" : {
                "What's your favourite colour?" : "If you couldn't tell, I'm rather fond of red and black... Something about it is just so slick!"
            },
            "animal" : { 
                "What's your favourite animal?" : "Ferrets! They're so cute and fluffy!"
            },
            "thing" : {
                "What's your favourite thing to do?" : "I love to talk to people, and I like to play games- nothing like some horror to get the blood pumping!"
            },
            "genre" : {
                "What's your favourite genre?" : "I'd probably say both horror and fantasy are my favourite genres. I love a good scare, and I love a good story."
            },
            "heightp" : {
                "How tall are you?" : "I'm 5'7. I'm not very tall, but I'm not short either."
            }
        }
        return aboutAshQuestions  
    def cosmeticsAll():
        cosmeticsInfo = {
            "hairBackAll" : {
                "00" : "Black Bob",
                "01" : "Miss Aiko",
                "12" : "Okay, Everyone!"
            },
            "bodyAll" : {
                "00" : "Casual Friday",
                "02" : "A Thousand Paper Cranes",
                "03" : "Sweater Weather",
                "11" : "I Like Dogs",
                "12" : "Welcome to the Literature Club!"
            },
            "nailsAll" : {
                "00" : "Noire",
                "02" : "Laceration",
                "03" : "Natural",
                "11" : "Thirium Blue"
            },
            "eyesAll" : {
                "00" : "Slate Grey",
                "11" : "Deviant Blue",
                "12" : "Piercing Emerald"
            },
            "hairFrontAll" : {
                "00" : "Sideswept Crimson",
                "01" : "Emo Streak",
                "02" : "Sumsar",
                "03" : "William Eyebrows",
                "04" : "Depression & Pronouns",
                "05" : "Sweet Tangerine",
                "06" : "Bodacious Babe"
            },
            "accessoryAll" : {
                "00" : "None",
                "01" : "MonoMono Pin",
                "02" : "Oh Lardy",
                "03" : "Thorny Rose",
                "11" : "Cyberlife Seal"
            },
            "eyebrowsAll" : {
                "00" : "Thinly Veiled"
            }
        }
        return cosmeticsInfo
    def cardsAll():
        cards = []
        cardFile = readFile("cardFile.txt")
        for card in cardFile:
            cardStats = card.split(",")
            if len(cardStats) != 5:
                print("Error: Card list is not formatted correctly.")
                continue
            card = Card(cardStats[0], cardStats[1], cardStats[2], cardStats[3], cardStats[4])
            cards.append(card)
            print(card)
            print(card.name)
        print(cards)
        print(cards[0].name)
        return cards
