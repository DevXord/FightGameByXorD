from random import  randint as rand
class Weapon:
    def __init__(self,id,name,mindmg = 4,maxdmg=10,levelweapon=1,weaponPrice=0):
        self.__wname = name
        self.__mdmg = mindmg
        self.__id = id
        self.__mxdmg = maxdmg
        self.__weaponlv = levelweapon
        self.__price = weaponPrice

    @property
    def weaponPrice(self):
        return self.__price

    @weaponPrice.getter
    def weaponPrice(self):
        return self.__price

    @weaponPrice.setter
    def weaponPrice(self, value):
        self.__price = value


    @property
    def weaponID(self):
        return self.__id

    @weaponID.getter
    def weaponID(self):
        return self.__id

    @weaponID.setter
    def weaponID(self, value):
        self.__id = value

    @property
    def weaponName(self):
        return self.__wname
    @weaponName.getter
    def weaponName(self):
        return self.__wname
    @weaponName.setter
    def weaponName(self, value):
        self.__wname = value


    @property
    def weaponMinDamage(self):
        return self.__mdmg


    @weaponMinDamage.getter
    def weaponMinDamage(self):
        return self.__mdmg


    @weaponMinDamage.setter
    def weaponMinDamage(self, value):
        self.__mdmg = value


    @property
    def weaponMaxDamage(self):
        return self.__mxdmg


    @weaponMaxDamage.getter
    def weaponMaxDamage(self):
        return self.__mxdmg


    @weaponMaxDamage.setter
    def weaponMaxDamage(self, value):
        self.__mxdmg = value


    @property
    def weaponLevel(self):
        return self.__weaponlv


    @weaponLevel.getter
    def weaponLevel(self):
        return self.__weaponlv


    @weaponLevel.setter
    def weaponLevel(self, value):
        self.__weaponlv = value


#class Two_handed(Weapon):
  #   def __init__(self,name,mindmg,maxdmg,levelweapon):
  #       super().__init__(name,mindmg,maxdmg,levelweapon)


class OneHanded(Weapon):
    def __init__(self,id,name,mindmg,maxdmg,levelweapon,weaponPrice):
        super().__init__(id,name,mindmg,maxdmg,levelweapon,weaponPrice)
        self.Damage = 0

    def hardAtack(self, adversary,playerstrong):

        if adversary != None:

            d1 = rand(self.weaponMinDamage, self.weaponMaxDamage)
            self.Damage = int(round(d1 / 5 * playerstrong))
            if self.Damage <= self.weaponMinDamage:
                return print("Miss")

            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zadałeś", self.Damage, "Obrażeń")

            elif adversary.Health > self.Damage:
                print("Zadałeś", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage

    def lowAtack(self, adversary,playerstrong):

        if adversary != None:

            d1 = rand(self.weaponMinDamage, self.weaponMaxDamage)
            self.Damage = int(round(d1 / 3 * playerstrong))
            if self.Damage <= self.weaponMinDamage:
                return print("Miss")
            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zadałeś", self.Damage, "Obrażeń")

            elif adversary.Health > self.Damage:
                print("Zadałeś", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage

    def advHardAtack(self, adversary, playerstrong):

        if adversary != None:

            d1 = rand(self.weaponMinDamage, self.weaponMaxDamage)
            self.Damage = int(round(d1 / 5 * playerstrong))
            if self.Damage <= self.weaponMinDamage:
                return print("Miss")

            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zadał Ci", self.Damage, "Obrażeń")

            elif adversary.Health > self.Damage:
                print("Zadał Ci", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage

    def advLowAtack(self, adversary, playerstrong):

        if adversary != None:

            d1 = rand(self.weaponMinDamage, self.weaponMaxDamage)
            self.Damage = int(round(d1 / 3 * playerstrong))
            if self.Damage <= self.weaponMinDamage:
                return print("Miss")
            if adversary.Health <= self.Damage:
                adversary.Health = 0
                print("Zadał Ci", self.Damage, "Obrażeń")

            elif adversary.Health > self.Damage:
                print("Zadał Ci", self.Damage, "Obrażeń")
                adversary.Health = adversary.Health - self.Damage

class Potion:
    def __init__(self,pId,pName,pEfect=0,pPrice=0):
        self.__pname = pName
        self.__pEfect = pEfect
        self.__pPrice = pPrice
        self.__pID = pId


    @property
    def potionID(self):
        return self.__pID

    @potionID.getter
    def potionID(self):
        return self.__pID

    @potionID.setter
    def potionID(self, value):
        self.__pID = value



    @property
    def potionPrice(self):
        return self.__pPrice

    @potionPrice.getter
    def potionPrice(self):
        return self.__pPrice

    @potionPrice.setter
    def potionPrice(self, value):
        self.__pPrice = value

    @property
    def potionEfect(self):
        return self.__pEfect


    @potionEfect.getter
    def potionEfect(self):
        return self.__pEfect


    @potionEfect.setter
    def potionEfect(self, value):
        self.__pEfect = value

    @property
    def potionName(self):
        return self.__pname


    @potionName.getter
    def potionName(self):
        return self.__pname


    @potionName.setter
    def potionName(self, value):
        self.__pname = value


class HealPotion(Potion):
    def __init__(self,pId,pName,pEfect,pPrice):
        super().__init__(pId,pName,pEfect,pPrice)





