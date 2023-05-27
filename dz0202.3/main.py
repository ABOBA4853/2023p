from lottery import Lottery
from human import Human
humans = list()
lottery = Lottery ('Lottery "Three-room apartment"')
dima = Human('Dima', True)
tanya = Human('Tanya')
dmytro = Human('Dmytro')
mariya = Human('Mariya')
humans.append(dima)
humans.append(tanya)
humans.append(dmytro)
humans.append(mariya)
for human in humans:
    lottery.AddHumanToLottery(human)
    lottery.ShowInfo(human)