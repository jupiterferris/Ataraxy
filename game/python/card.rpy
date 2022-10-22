init python:
    class Card:
        def __init__(self, name, power, health, cost, ability):
            self.name = name
            self.power = power
            self.health = health
            self.cost = cost
            self.ability = ability
        def __str__(self):
            cardDetails = [self.name, self.power, self.health, self.cost, self.ability]
            return str(cardDetails)
