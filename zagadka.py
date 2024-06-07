class Zagadka:
    def __init__(self,question, answer):
        self.question = question
        self.answer = answer

    def solve(self, givenAnswer):
        return givenAnswer.upper() == self.answer.upper()