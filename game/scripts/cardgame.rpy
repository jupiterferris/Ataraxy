init:
    transform pos_1_1:
        xalign 0.3 yalign 0.0
        linear 1.0 yalign 0.12
    transform pos_1_2:
        xalign 0.3 yalign 0.0
        linear 1.0 yalign 0.5
    transform pos_2_1:
        xalign 0.43 yalign 0.0
        linear 1.0 yalign 0.12
    transform pos_2_2:
        xalign 0.43 yalign 0.0
        linear 1.0 yalign 0.5
    transform pos_3_1:
        xalign 0.57 yalign 0.0
        linear 1.0 yalign 0.12
    transform pos_3_2:
        xalign 0.57 yalign 0.0
        linear 1.0 yalign 0.5
    transform pos_4_1:
        xalign 0.7 yalign 0.0
        linear 1.0 yalign 0.12
    transform pos_4_2:
        xalign 0.7 yalign 0.0
        linear 1.0 yalign 0.5

    transform cardtrans:
        Fixed(
        f"images/cards/{card.name}.png",
        Text(f"{card.health}", align=(0.16, 0.9)),
        Text(f"{card.strength}", align=(0.82, 0.9)),
        Text(f"{card.cost}", align=(0.88, 0.215)),
        fit_first=True
        )
    image cardtest:
        contains cardtrans

    image Project Bolan:
        "images/cards/Project Bolan.png"
    image Zerg:
        "images/cards/Zerg.png"
    
    screen duck():
        frame:
            background Solid("#b0000069")
            align(0.99, 0.9)
            grid 2 1:
                spacing 10
                imagebutton idle "images/cards/back.png" hover "images/cards/backhover.png" action Return()
                imagebutton idle "images/cards/zergback.png" hover "images/cards/zergbackhover.png" action Return()
                
    screen table():
        frame:
            background Solid("#b0000069")
            align(0.5, 0.2)
            grid 4 2:
                spacing 10
                for x in range(4):
                    image "images/cards/emptyslot.png"
                for x in range(4):
                    imagebutton idle "images/cards/emptyslot.png" hover "images/cards/emptyslothover.png" action Return(x)
    #screen hand():
    #    frame:
    #        background Solid("#b0000069")
    #        align(0.5, 0.9)
    #        hbox:

    layeredimage bg gameroom:
        always:
            "bg game"
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