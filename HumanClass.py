class Human:
    def __init__(self, name,health = 100,level= 1, strong= 5,wital = 5):
        self.__name = name
        self.__health = health
        self.__lv = level
        self.__strong = strong
        self.__wtial = wital
        self.__MAX_DAMAGE = 5
        self.__MIN_DAMAGE = 1


    @property
    def wital(self):
        return self.__wtial

    @wital.getter
    def wital(self):
        return self.__wtial

    @wital.setter
    def wital(self, value):
        self.__wtial = value


    @property
    def Level(self):
        return self.__lv

    @Level.getter
    def Level(self):
        return self.__lv

    @Level.setter
    def Level(self, value):
        self.__lv = value

    @property
    def Name(self):
        return self.__name

    @Name.getter
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        self.__name = value

    @property
    def Health(self):
        return self.__health

    @Health.getter
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        self.__health = value

    @property
    def Strong(self):
        return self.__strong

    @Strong.getter
    def Strong(self):
        return self.__strong

    @Strong.setter
    def Strong(self, value):
        self.__strong = value

    @property
    def MaxDamage(self):
        return self.__MAX_DAMAGE

    @MaxDamage.getter
    def MaxDamage(self):
        return self.__MAX_DAMAGE

    @MaxDamage.setter
    def MaxDamage(self, value):
        self.__MAX_DAMAGE = value

    @property
    def MinDamage(self):
        return self.__MIN_DAMAGE

    @MinDamage.getter
    def MinDamage(self):
        return self.__MIN_DAMAGE

    @MinDamage.setter
    def MinDamage(self, value):
        self.__MIN_DAMAGE = value


