import random


class Universe:

    def __init__(self, object):
        self.object = object


class Object(Universe):
    owners = {}

    def __init__(self, object):
        super().__init__(object)


class Human(Object):
    def __init__(self, name, creature):
        super().__init__(creature)
        self.name = name

    def displaycat(self, name, owners):
        print(self.name + 'have cat with ' + owners.get(self.name)[0]
              + 'head ' + owners.get(self.name)[1] + 'tail')


class Cat(Object):

    def __init__(self, colorhead, colortail, creature):
        super().__init__(creature)
        self.colorhead = colorhead
        self.colortail = colortail


owners = {}

names = ('Peter John', 'Fucking Slave', 'Dungeon Master', 'Billy Bons', 'John Dee', 'Bob Glob', 'Isaac West',
         'Son Of Slut', 'Biba', 'Boba')
colors = ('White', 'Blue', 'Green', 'Black', 'Grey', 'Pink',)
i = 0


def setowner(name, colorhead, colortail, owners):
    colors = [colorhead, colortail]
    owners[name] = colors
    return owners


while i <= (len(names) - 1):
    person = Human(names[i], 'owner')
    pet = Cat(random.choice(colors), random.choice(colors), 'pet')
    setowner(person.name, pet.colorhead, pet.colortail, owners)
    print(person.name + ' have cat with ' + pet.colorhead + ' head ' + pet.colortail + ' tail ')
    i += 1
