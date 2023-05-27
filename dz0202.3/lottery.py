from human import Human
class Lottery:

    def __init__(self, prize = None):
        self.Prize =  prize
        self.Members = list()
        self.Winners = list()

    def AddHumanToLottery(self, human = Human()):
        if(human.isWinner):
            self.Winners.append(human)
        else:
            self.Members.append(human)
    def ShowInfo(self, human = Human()):
        if(human.isWinner):
            print(f'The Winner of {self.Prize} is {human.__str__()}')
        else:
            print(f'The member of {self.Prize} is {human.__str__()}')