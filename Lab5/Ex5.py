
class Animal:
    def __init__(self, name, age, species, edible, size):
        self.name = name
        self.age = age
        self.species = species
        self.health = 100
        self.edible = edible
        self.size = size

    def update_health(self, amount):
        self.health += amount
        # Verificăm dacă sănătatea a depășit 100 și, în caz afirmativ, o setăm la 100
        self.health = min(self.health, 100)

    def check_health(self):
        print(f"{self.name}'s health is {self.health}%.")

    def is_edible(self):
        if self.edible:
            print(f"{self.name} is edible.")
        else:
            print(f"{self.name} is not edible.")

    def eat(self, prey):
        if self.size > prey.size:
            print(f"{self.name} is eating {prey.name}!")
            prey.update_health(-prey.health)
            self.update_health(20)
        else:
            print(f"{self.name} tried to eat {prey.name} but it was too big!")


class Mammal(Animal):
    def __init__(self, name, age, species, edible,size,fur_color, nr_legs):
        super().__init__(name, age, species, edible,size)
        self.fur_color = fur_color
        self.nr_legs = nr_legs

    def give_birth(self):
        print(f"{self.name} is giving birth.")

    def nurse_young(self):
        print(f"{self.name} is nursing its young.")

    def pet(self):
        print(f"{self.name} enjoys being petted.")

    def socialize(self):
        print(f"{self.name} is socializing with other mammals.")

    def sleep(self):
        print(f"{self.name} is taking a nap.")


class Bird(Animal):
    def __init__(self, name, age, species, edible, size, can_fly):
        super().__init__(name, age, species, edible, size)
        self.can_fly = can_fly
        self.feather_color = ""

    def fly(self):
        if self.can_fly:
            print(f"{self.name} can fly.")
        else:
            print(f"{self.name} cannot fly.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

    def build_nest(self):
        print(f"{self.name} is building a nest.")

    def peck(self):
        print(f"{self.name} is pecking for food.")

    def set_feather_color(self, color):
        self.feather_color = color
        print(f"{self.name}'s feathers are now {self.feather_color}.")


class Fish(Animal):
    def __init__(self, name, age, species, edible,size, scale_color, can_swim):
        super().__init__(name, age, species, edible,size)
        self.scale_color = scale_color
        self.can_swim = can_swim
        self.edible = edible

    def swim(self):
        if self.can_swim:
            print(f"{self.name} is gracefully swimming through the water.")
        else:
            print(f"{self.name} wishes it could swim, but unfortunately, it can't.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

    def school(self, school_size):
        print(f"{self.name} is swimming in a school with {school_size} other fish.")



    def deep_dive(self, depth):
        print(f"{self.name} is making a deep dive to a depth of {depth} meters.")


if __name__ == '__main__':
    # Exemplu pentru un mamifere
    dog = Mammal("Buddy", 3, "Dog", False, 3, "Brown", 4)
    dog.give_birth()
    dog.pet()
    dog.socialize()
    dog.sleep()
    dog.check_health()
    dog.is_edible()

    # Exemplu pentru pasari
    hen = Bird("Henrietta", 2, "Chicken", True, 1, False)
    hen.fly()
    hen.build_nest()
    hen.peck()
    hen.set_feather_color("Brown")
    hen.lay_eggs()
    hen.is_edible()

    # Exemplu pentru pesti
    tuna = Fish("Tuna", 5, "Tuna Fish", "Silver", 2,True, True)
    tuna.swim()
    tuna.lay_eggs()
    tuna.school(15)
    tuna.deep_dive(10)
    tuna.check_health()
    tuna.is_edible()

    shark = Fish("Tiger Shark", 8, "Shark", "Grey", 40, True, True)
    shark.swim()
    shark.lay_eggs()  # Deși nu este specific pentru toți rechinii, am păstrat această metodă pentru coerență
    shark.is_edible()
    shark.health = 70
    shark.eat(tuna)
    shark.check_health()
    tuna.check_health()



