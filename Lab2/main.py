class Pet:
    def __init__(self, name, age, trained = False, owner = None):
        self.name = name
        self.age = age
        self.trained = trained
        self.owner = owner


    def train(self):
        self.train = True

    def set_owner(self, owner):
        self.owner = owner

    def __str__(self):
        if self.train:
            train_str = 'house trained'
        else:
            train_str = 'not house trained'
        if self.owner:
            owner_str = ' and ' + self.owner + ' owns me'
        else:
            owner_str = ' and no one owns me'
        return 'Hi I am ' + str(
            self.age) + 'yrs and my name is ' + self.name + '.\nI am ' + train_str + owner_str + '.'