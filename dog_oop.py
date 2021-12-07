class Dog:
    def __init__(self, dog_name, dog_x, dog_y):
        self.name = dog_name
        self.x = dog_x
        self.y = dog_y

    def walk(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

    def get_location(self):
        print(self.x,self.y)

    def say_your_name(self):
        # name_list = [word[0].upper() + word[1:] for word in self.name.split()]
        # self.name = "".join(name_list)
        print('My name is' , self.name[:1].upper() + self.name[1:])


my_dog = Dog('sally', 0, 1)
my_dog.walk(1, 2)
my_dog.get_location()    # expected 1, 3
my_dog.say_your_name()   # My name is Sally





