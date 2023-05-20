from car import Car
from human import Human
humans = list()
car = Car ('BMW')
dima = Human('Dima', True)
tanya = Human('Tanya')
dmytro = Human('Dmytro')
mariya = Human('Mariya')
humans.append(dima)
humans.append(tanya)
humans.append(dmytro)
humans.append(mariya)
for human in humans:
    car.AddHumanToCar(human)
    car.ShowInfo(human)