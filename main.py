class Fan:
    def __init__(self, nom):
        self.nom = nom


class Universitet:
    def __init__(self):
        self.fanlar = []

    def add_fan(self, fan):
        self.fanlar.append(fan.nom)

    def info(self):
        print(self.fanlar)


f1 = Fan("Fizika")
f2 = Fan("Kimyo")

u1 = Universitet()
u1.add_fan(f1)
u1.add_fan(f2)
u1.info()
