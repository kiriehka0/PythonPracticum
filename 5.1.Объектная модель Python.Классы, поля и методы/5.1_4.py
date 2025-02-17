class Programmer:
    def __init__(self, name, job_title, a=0):
        self.name = name
        self.job_title = job_title
        self.a = a
        self.b = 0
        self.c = 0
        if self.job_title == 'Junior':
            self.money = 10
        elif self.job_title == 'Middle':
            self.money = 15
        elif self.job_title == 'Senior':
            self.money = 20

    def rise(self):
        if self.job_title == 'Junior':
            self.job_title = 'Middle'
            self.money = 15
        elif self.job_title == 'Middle':
            self.job_title = 'Senior'
            self.money = 20
        elif self.job_title == 'Senior':
            self.money += 1

    def work(self, time):
        self.a += time
        self.b = time

    def info(self):
        self.c = (self.b * self.money) + self.c
        return f"{self.name} {self.a}ч. {self.c}тгр."
