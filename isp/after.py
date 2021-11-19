# Много интерфейсов, специально предназначенных для клиентов, лучше, чем один интерфейс общего назначения

class Creature:
    def __init__(self, name):
        self.name = name


class SwimmerInterface:  # Интерфейс
    def swim(self):
        pass


class WalkerInterface:  # Интерфейс
    def walk(self):
        pass


class TalkerInterface:  # Интерфейс
    def talk(self):
        pass


class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):  # Клиент
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")

    def talk(self):
        print(f"I'm {self.name} and I can talk")


class Fish(Creature, SwimmerInterface):  # Клиент
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")


class Cat(Creature, SwimmerInterface, WalkerInterface):  # Клиент
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"I'm {self.name} and I can swim")

    def walk(self):
        print(f"I'm {self.name} and I can walk")


human = Human("John Doe")
human.swim()
human.walk()
human.talk()

fish = Fish("Nemo")
fish.swim()

cat = Cat("Mr. Buttons")
cat.walk()
cat.swim()