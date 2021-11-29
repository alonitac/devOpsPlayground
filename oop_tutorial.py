class Dog:
    def __init__(self, dog_name, dog_type):
        self.dog_type = dog_type
        self.name = dog_name

    def walk(self):
        print(self.name, 'is walking')

    def bark(self, n):
        for i in range(n):
            print(self.name, 'is saying HAW')


class GuideDog(Dog):
    def cross_road(self):
        print('crossing...')

    def bark(self, n):
        print(self.name, 'is saying HAW')


def game(dog):
    dog.walk()
    dog.bark()


dog1 = GuideDog('papi', 'guide')
dog2 = Dog('sally', 'pet')

game(dog1)
game(dog2)





