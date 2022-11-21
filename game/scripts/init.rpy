init:
    $ getAshBasics
    $ removeKeybinds(['rollback', 'rollforward', 'help', 'skip', 'toggle_skip', 'fast_skip', 'game_menu'])
    $ rebindKeybinds([['quit', 'K_ESCAPE']])

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

    screen chosenPicture():
        imagebutton idle "images/gallery/[pictureChoice].png" hover "images/gallery/[pictureChoice].png" action Return() at truecenter
    image bg room:
        f"images/bgs/bg {timeOfDay}.png"
    image clouds:
        "images/bgs/tutorial/clouds.png"
        xalign 0.0
        linear 40.0 xalign 1.0
        repeat
    image petals:
        "images/bgs/tutorial/sakura.png"
        xanchor 0
        yanchor 0
        xalign 1.0
        yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0
        repeat
    style widgetback:
        background "gui/rightbox.png"    
    
    screen dayTime:
        $ modal = False 
        add "gui/time/timebg.png" xpos 0 ypos 0
        add f"gui/time/{timeOfDay}.png" xpos 5 ypos 0
        text(f"{timeOfDay}") xpos 80 ypos 15
    screen currentlyPlaying:
        $ modal = False 
        add "gui/playing.png" xpos 0 ypos 80
        python:
            current = currentTrack.replace("Alternative", "Alt.") + " - " + artistName
            if len(current) > 27:
                current = current[:27] + "..."
        text("{image=note.png}[current]") xpos 0 ypos 80 size 18
    screen balance:
        $ modal = False
        grid 2 4:
            align(1.0, 0)
            for i in range (4):
                add "gui/fruitbox.png" zoom .2 at right
                add "gui/fruitname.png" yalign 0.5
        frame:
            align(1.0, 0)
            background "#00000000"
            grid 2 4:
                add "starfruit" zoom .2 at right
                text("Behold, starfruit!") yalign 0.5
                add "strawberry" zoom .2 at right
                text("This is a strobbery") yalign 0.5
                add "cherry" zoom .2 at right
                text("This is a chewwy") yalign 0.5
                add "melon" zoom .2 at right
                text("This is a mewwon") yalign 0.5

        
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
            attribute accessory default:
                "ash_accessory"
        group eyebrows:
            attribute eyebrows default:
                "ash_eyebrows"  
