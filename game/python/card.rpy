init python:
    class Card:
        def __init__(self, name, strength, health, cost, ability):
            self.name = name
            self.strength = strength
            self.health = health
            self.cost = cost
            self.ability = ability
        def __str__(self):
            cardDetails = [self.name, self.strength, self.health, self.cost, self.ability]
            return str(cardDetails)