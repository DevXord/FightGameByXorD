from HumanClass import Human
from random import randint as rand


class Adv(Human):
    def __init__(self, NM,HP,LV, ST,WP = None):
        super().__init__(NM,HP,LV, ST)
        self.__stealGold = 0
        self.__damage = 0
        self.__weapon = WP



    @property
    def advWeapon(self):
        return self.__weapon

    @advWeapon.getter
    def advWeapon(self):
        return self.__weapon

    @advWeapon.setter
    def advWeapon(self, value):
        self.__weapon = value


    @property
    def stealGold(self):
        return self.__stealGold

    @stealGold.getter
    def stealGold(self):
        return self.__stealGold

    @stealGold.setter
    def stealGold(self, value):
        self.__stealGold = value

    @property
    def Damage(self):
        return self.__damage

    @Damage.getter
    def Damage(self):
        return self.__damage

    @Damage.setter
    def Damage(self, value):
        self.__damage = value








    def atackLeftHand(self, adversary):

        if adversary != None:

            d1 = rand(self.MinDamage, self.MaxDamage)
            self.Damage = int(round(d1 / 5 * self.Strong))



            if self.Damage <= self.MinDamage:
                return print("Przeciwnik Miss")

            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Przeciwnik Zadał Ci", self.Damage, "Obrażeń")
            elif adversary.Health > self.Damage:
                print("Przeciwnik Zadał Ci", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage
            print()


    def atackRightHand(self, adversary):

        if adversary != None:

            d1 = rand(self.MinDamage, self.MaxDamage)
            self.Damage = int(round(d1 / 3 * self.Strong))

            if self.Damage <= self.MinDamage:
                return print("Przeciwnik Miss")

            if adversary.Health <= self.Damage:
                print("Przeciwnik Zadał Ci", self.Damage, "Obrażeń")
                adversary.Health = 0

            elif adversary.Health > self.Damage:
                print("Przeciwnik Zadał Ci", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage
            print()


