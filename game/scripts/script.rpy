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

init python:
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
label splashscreen:
    show text "Loading." with dissolve
    pause 0.5
    show text "Loading.." with dissolve
    pause 0.5
    show text "Loading..." with dissolve
    pause 0.5
    hide text with dissolve
    return
label start:
    # this is the intro- also serves as initial loading progress.
    stop music fadeout 1.0 
    $ bootGame()

    # if the player has already completed the tutorial, skip the intro
    python:
        if not tutorialCompleted and name != "":
            renpy.jump("init_tutorial")
        elif name == "":
            renpy.jump("meet_ashley")

    #jump gayme

    scene bg room
    show ash blink
    with fade
    $ jamSelector("random")
    $ greeting = greetingSelector()
    a "[greeting]"
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
    call random_events
    jump interact
# decides what extra events will be played before the player gets control
label random_events:
    # when the game is launched, before you get to interact with Ashley, you might have a random event.
    $ event = random.randint(1, 100)
    a "Event value = [event]"
    if event == 1:
        a "I'm sorry, I'm not feeling well today. I'll be back next time."
        show ash close
        jump quit
    elif event > 90:
        a "Let me ask you something..."
        #    menu:
        #        a "How's your day been?"
        #        "Great!":
        #        "It's been alright.":
        #        "Not so good.":
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
                            $ randomSong = False
                            jump conversation
                        "Which song is this again?":
                            $ randomSong = False
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
                if len(unlocked) == 0:
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
    stop music fadeout 1.0
    scene bg gameroom
    show ash blink
    with fade 
    play music "audio/jams/Your Reality.mp3"
    a "Another challenger. It has been a while."
    a "So you've found your way to the game room."
    a "Welcome."
    a "Shall we begin?"
    window hide dissolve
    show screen table 
    show screen duck
    show cardtest at pos_1_1 onlayer screens
    show Project Bolan at pos_1_2 onlayer screens
    python:
        ui.interact()
    
# This ends the game.
return
