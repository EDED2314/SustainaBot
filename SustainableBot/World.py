import random
import names


class World(object):

    def __init__(self):
        self.humans = 2
        self.human_list = []
        for i in range(self.humans):
            self.human_list.append(World.Human())

        self.co2 = 0
        self.aval_food = 100
        self.aval_water = 100

        for human in self.human_list:
            self.co2 = round(self.co2 + human.co2, 2)
            self.aval_food = round(self.aval_food - human.food_usage)
            self.aval_water = round(self.aval_water - human.water_usage)

        self.windmills = 0
        self.solarpanels = 0
        self.hydrualicplants = 0
        self.nuclearreactors = 0

        self.health = 100

        self.msg_co2 = 0

    def get_humans(self):
        data = []
        for human in self.human_list:
            data.append(human.return_info())
        return data

    def add_human(self):
        self.human_list.append(World.Human())
        self.update_human_info()

    def update_human_info(self):
        for human in self.human_list:
            self.co2 = round(self.co2 + human.co2, 2)
            self.aval_food = round(self.aval_food - human.food_usage)
            self.aval_water = round(self.aval_water - human.water_usage)
        self.humans = len(self.human_list)


    class Human(object):
        def __init__(self):
            self.co2 = random.randint(0, 75) / 100
            self.food_usage = random.randint(0, 75) / 100
            self.water_usage = random.randint(0, 75) / 100
            self.id = random.randint(100000, 999999)
            number = random.randint(0, 1)
            if number == 0:
                self.name = names.get_full_name("male")
                self.gender = "male"
            else:
                self.name = names.get_full_name('female')
                self.gender = "female"

        def return_info(self):
            info = {"🆔": self.id, "🌲**Carbon Emission**🚗": self.co2, "🍖**Food usage**🍚": self.food_usage, "💧**Water Usage**🚿": self.water_usage,
                    "🧑**Name**👧": self.name,
                    "🚹**Gender**🚺": self.gender}
            return info
