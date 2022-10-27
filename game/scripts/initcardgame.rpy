init:
    screen cardtest():
        add Image(f"images/cards/{card.name}.png")
        hbox:
            align(0.0125, 0.2222)
            spacing 100
            text f"{card.health}"
            text f"{card.strength}"
        hbox:
            align(0.09, 0.05)
            text f"{card.cost}"
    screen deck():
        frame:
            background Solid("#b0000069")
            align(0.99, 0.9)
            grid 2 1:
                spacing 10
                imagebutton idle "images/cards/back.png" action Return()
                imagebutton idle "images/cards/Project Bolan.png" action Return()
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