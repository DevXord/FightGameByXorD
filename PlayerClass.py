from HumanClass import Human
from random import randint as rand

class Player(Human):
    def __init__(self, name,WP = None):
        super().__init__(name)
        self.__nextAdv = ""
        self.__damage = 0
        self.__gold = 5
        self.__exp = 0
        self.__skillPonint = 5
        self.__exptonextlv = 50
        self.__weapon = WP
        self.__pocketToPotion1  = None
        self.__pocketToPotion2  = None
        self.__MAX_HEALT_PLAYER = 100 +  self.wital *10

    @property
    def MAX_PLAYER_HEALT(self):
        return self.__MAX_HEALT_PLAYER

    @MAX_PLAYER_HEALT.getter
    def MAX_PLAYER_HEALT(self):
        return self.__MAX_HEALT_PLAYER

    @MAX_PLAYER_HEALT.setter
    def MAX_PLAYER_HEALT(self, value):
        self.__MAX_HEALT_PLAYER = value

    @property
    def packetToPotion2(self):
        return self.__pocketToPotion2

    @packetToPotion2.getter
    def packetToPotion2(self):
        return self.__pocketToPotion2

    @packetToPotion2.setter
    def packetToPotion2(self, value):
        self.__pocketToPotion2 = value

    @property
    def packetToPotion1(self):
        return self.__pocketToPotion1

    @packetToPotion1.getter
    def packetToPotion1(self):
        return self.__pocketToPotion1

    @packetToPotion1.setter
    def packetToPotion1(self, value):
        self.__pocketToPotion1 = value



    @property
    def playerWeapon(self):
        return self.__weapon

    @playerWeapon.getter
    def playerWeapon(self):
        return self.__weapon

    @playerWeapon.setter
    def playerWeapon(self, value):
        self.__weapon = value



    @property
    def NextAdv(self):
        return self.__nextAdv

    @NextAdv.getter
    def NextAdv(self):
        return self.__nextAdv

    @NextAdv.setter
    def NextAdv(self, value):
        self.__nextAdv = value


    @property
    def SkillPonint(self):
        return self.__skillPonint

    @SkillPonint.getter
    def SkillPonint(self):
        return self.__skillPonint

    @SkillPonint.setter
    def SkillPonint(self, value):
        self.__skillPonint = value

    @property
    def ExpToNextLv(self):
        return self.__exptonextlv

    @ExpToNextLv.getter
    def ExpToNextLv(self):
        return self.__exptonextlv

    @ExpToNextLv.setter
    def ExpToNextLv(self, value):
        self.__exptonextlv = value

    @property
    def Exp(self):
        return self.__exp

    @Exp.getter
    def Exp(self):
        return self.__exp

    @Exp.setter
    def Exp(self, value):
        self.__exp = value

    @property
    def Damage(self):
        return self.__damage
    @Damage.getter
    def Damage(self):
        return self.__damage
    @Damage.setter
    def Damage(self, value):
        self.__damage = value

    @property
    def gold(self):
        return self.__gold

    @gold.getter
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value):
        self.__gold  = value




    def checkstats(self):

        print("Punkty Umiejetnosci",str(self.SkillPonint))
        print()
        print("Poziom",str(self.Level))
        print("Exp",str(self.Exp) + "/" + str(self.ExpToNextLv))
        print("Gold",str(self.gold))
        if self.playerWeapon != None:
            print("Bro??", str(self.playerWeapon.weaponName))
        else:
            print("Bro??", "Brak")
        print("Punkty ??ycia",str(self.Health))
        print("Si??a",str(self.Strong))
        print("Witalno????", str(self.wital))
        print("Max Obra??e??",str(self.MaxDamage))
        print("Min Obra??e??",str(self.MinDamage))

    def checklevelup(self):
        if self.Exp >= self.ExpToNextLv:
            print("Level Up!")
            self.Exp = 0
            self.Level = self.Level + 1
            self.SkillPonint = self.SkillPonint + 5
            self.ExpToNextLv = self.Level * 50

    def atackLeftHand(self, adversary):

        if adversary != None:

            d1 = rand(self.MinDamage,self.MaxDamage)
            self.Damage = int(round( d1/5 * self.Strong))
            if self.Damage <= self.MinDamage:
               return print("Miss")

            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zada??e??", self.Damage, "Obra??e??")
            elif adversary.Health > self.Damage:
                print("Zada??e??", self.Damage, "Obra??e??")
                adversary.Health = adversary.Health -self.Damage
            print()


    def atackRightHand(self, adversary):

        if adversary != None:

            d1 = rand(self.MinDamage, self.MaxDamage)
            self.Damage = int(round(d1 / 3 * self.Strong))
            if self.Damage <= self.MinDamage:
                return print("Miss")
            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zada??e??", self.Damage, "Obra??e??")
            elif adversary.Health > self.Damage:
                print("Zada??e??", self.Damage, "Obra??e??")
                adversary.Health = adversary.Health - self.Damage
            print()