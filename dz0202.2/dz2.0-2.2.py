class Pet:

   def __init__(self, name, species):

       self.name = name
       self.species = species
       self.hungry = True
       self.tired = True
       self.happy = False

   def feed(self):

       if self.hungry:

           print(f'{self.name} Бублік був нагодований.')

           self.hungry = False

       else:

           print(f'{self.name} Бублік зовсім не голодний.')


   def sleep(self):

       if self.tired:

           print(f'{self.name} пішов спатки.')

           self.tired = False

       else:

           print(f'{self.name} не втомився.')


   def play(self):

       if self.happy:

           print(f'{self.name} Бублік вже граєсться.')

       else:

           print(f'{self.name} Бублік грається.')

           self.happy = True