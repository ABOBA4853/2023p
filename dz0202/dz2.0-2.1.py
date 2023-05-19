import random
class Student:
   def __init__(self, name):

       self.name = name
       self.gladness = 50
       self.progress = 0
       self.alive = True
       self.money = 0

   def to_study(self):
       print('Час вчитися')
       self.progress += 0.50
       self.gladness -= 5

   def to_chill(self):
       if self.money >= 10:
           print('Час відпочити')
           self.gladness += 5
           self.progress -= 0.1
           self.money -= 10
       else:
           print('Не вистачає грошей, щоб відпочити. Час працювати.')
           self.to_work()
   def to_sleep(self):
       print('Час спати.')
       self.gladness += 2
       self.progress -= 0.05
   def to_work(self):
       print('Час працювати.')
       self.money += 20
       self.progress -= 0.1
   def is_alive(self):
       if self.progress < -0.5:
           print('Пішов')
           self.alive = False
       elif self.gladness <= 0:
           print('Депресія')
           self.alive = False
       elif self.progress > 5:
           print('пройшов екперимент…')
           self.alive = False

   def end_of_day(self):
       print(f'Радість = {self.gladness}')
       print(f'Прогрес = {round(self.progress, 2)}')
       print(f'Грошей = {self.money}')

   def live(self):

       for day in range(1, 366):
           day_str = f'Днів {day}  {self.name} життя'
           print(f'{day_str:=^50}')
           live_cube = random.randint(1, 4)
           if live_cube == 1:
               self.to_study()
           elif live_cube == 2:
               self.to_sleep()
           elif live_cube == 3:
               self.to_chill()
           elif live_cube == 4:
               self.to_work()
           self.end_of_day()
           self.is_alive()
           if not self.alive:
               print(f'{self.name} пішов з життя {day}.')
               break