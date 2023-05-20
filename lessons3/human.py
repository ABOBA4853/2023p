class Human:

    def __init__(self, name = None, isDriver = False):
        self.Name = name
        self.isDriver = isDriver

    def __str__(self):
        return self.Name


