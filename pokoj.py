import random

from zagadka import Zagadka


class Pokoj:

    def __init__(self, name, description):
        quests = [
            Zagadka("Co ma 4 nogi i szczeka?", "pies"),
            Zagadka("Co jest gorsze niż pamięć RAM?", "pamięć ROM"),
            Zagadka("Gdy miarka się przelewa, co się robi?", "mierzy"),
        ]
        self.name = name
        self.description = description
        self.relations = {}
        self.quest = random.choice(quests)

    def addRelation(self, direction, room):
        self.relations[direction] = room

    def getRelation(self, direction):
        return self.relations.get(direction)

    def hasQuest(self):
        return self.quest is not None

    def solve_puzzle(self, answer):
        if self.quest:
            return self.quest.solve(answer)
        return False
