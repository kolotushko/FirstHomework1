class Student:
    def __init__(self, name, age, group):
        self.Name = name
        self.Age = age
        self.Group = group
        self.gladness = 50

        self.progress = 0

        self.alive = True

        self.money = 0

    def to_study(self):

        print("Time to study")

        self.progress += 0.12

        self.gladness -= 3

    def to_chill(self):

        if self.money >= 10:

            print("Time to chill")

            self.gladness += 5

            self.progress -= 0.1

            self.money -= 10

        else:

            print("Not enough money to chill. Time to work.")

            self.to_work()

    def to_sleep(self):

        print("Time to sleep")

        self.gladness += 2

        self.progress -= 0.05

    def to_work(self):

        print("Time to work")

        self.money += 20

        self.progress -= 0.1

    def ToString(self):
        print(f"Name: {self.Name}\n"
              f"Age: {self.Age}\n"
              f"Group: {self.Group}")
