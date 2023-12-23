
import random

class Human:

    def __init__(self, name, job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.food = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        pass

    def work(self):
        pass

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def shopping(self):
        pass

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def repair(self):
        self.car.strenght += 100
        self.money -= 50

    def day_indexes(self, day):
        pass

    def is_alive(self):
        if self.gladness < 0:
            print('Depression..')
            return False
        if self.food < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt..')
            return False

    def live(self, day):
        pass

    def adopt_pet(self, pet):
        self.pet = pet

    def play_with_pet(self):
        if self.pet:
            self.pet.play()
            print(f"{self.name} is playing with {self.pet.name}.")
        else:
            print(f"{self.name} doesn't have a pet.")

    def feed_pet(self):
        if self.pet:
            self.pet.feed()
            print(f"{self.name} is feeding {self.pet.name}.")
        else:
            print(f"{self.name} doesn't have a pet.")

class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fust = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strenght > 0 and self.fust >= self.consumption:
            self.fust -= self.consumption
            self.strenght -= 1
            return True
        else:
            print('Car cannot move :(')
            return False

class House:

    def __init__(self):
        self.mess = 0
        self.products = 0

class Job:

    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

job_list = {}
brands_of_car = {}

nick = Human(name='nick')
for day in range(1, 8):
    if nick.is_alive() == False:
        break