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

            firstPlayed = self.json.get("firstPlayed")
            if firstPlayed is None:
                self.setValue("firstPlayed", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

            # Last time the player logged on
            lastPlayed = self.json.get("lastPlayed")
            if lastPlayed is None:
                self.setValue("lastPlayed", "")

            # Cosmetics unlocked for Ashley, given in lists of order (hairBack, body, nails, eyes, hairFront, accessory, eyebrows)
            cosmetics = self.json.get("cosmetics")
            if cosmetics is None:
                self.setValue("cosmetics", [["00"], ["00"], ["00"], ["00"], ["00"], ["00"], ["00"]])
            
            pictures = self.json.get("pictures")
            if pictures is None:
                self.setValue("pictures", [])
            
            ashe = self.json.get("balance")
            if ashe is None:
                self.setValue("balance", [])

            aboutPlayer = self.json.get("aboutPlayer")
            if aboutPlayer is None:
                self.setValue("aboutPlayer", [])
            
            heardAnecdotes = self.json.get("heardAnecdotes")
            if heardAnecdotes is None:
                self.setValue("heardAnecdotes", [])
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
