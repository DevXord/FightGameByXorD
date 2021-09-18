import os
class GeneralSettings:
    __IS_PROGRAM_RUN = True
    __IS_PLAY_GAME = False
    __IS_FIGHT_GAME = False
    __IS_IN_SHOP = False
    __IS_IN_STATS = False

    weaponNameList = [
                        "Ostry kamien",
                        "Sztylet",
                        "Krótki miecz",
                        "Zardzewiały miecz",
                        "Miecz nowicjusza",
                        "Piechur",
                        "Miecz strażnika",
                        "Miecz mistrza",
                        "Miecz Kapitana",
                        "Samerters",
                        "Sindax",
                        "Miecz Palladyna",
                        "Wyjątkowy miecz",
                        "Miecz oficerski",
                        "Miecz generała",
                        "Miecz dyktatora",
                        "Pradawny miecz",
                        "Dziwomiecz",
                        "Dzanger",
                        "Kaster",
                        "Legendarny Miecz"]

    advnamelist = [
                    "Bill",
                    "Sentenz",
                    "Gabir",
                    "Samor",
                    "Kabo",
                    "Kirir",
                    "Samonir",
                    "Kapa",
                    "Killer",
                    "LastDream",
                    "Winner",
                    "G. Brenc",
                    "Borys",
                    "Heartless",
                    "Stone Hands",
                    "Monster Killer",
                    "Bill's brother",
                    "Captain Claw",
                    "Pirate John",
                    "Private Daniel",
                    "Private George",
                    "Private Jake",
                    "Capitan Harry",
                    "Capitan Richard",
                    "Officer Kingers",
                    "Officer Sangure",
                    "General Geralt",
                    "Dictator"]
    advnamelist2 = [
                    "Undead Bill",
                    "Undead Sentenz",
                    "Undead Gabir",
                    "Undead Samor",
                    "Undead Kabo",
                    "Undead Kirir",
                    "Undead Samonir",
                    "Undead Kapa",
                    "Undead Killer",
                    "Undead LastDream",
                    "Undead Winner",
                    "Undead G. Brenc",
                    "Undead Borys",
                    "Undead Heartless",
                    "Undead Stone Hands",
                    "Undead Monster Killer",
                    "Undead Bill's brother",
                    "Undead Captain Claw",
                    "Undead Pirate John",
                    "Undead Private Daniel",
                    "Undead Private George",
                    "Undead Private Jake",
                    "Undead Capitan Harry",
                    "Undead Capitan Richard",
                    "Undead Officer Kingers",
                    "Undead Officer Sangure",
                    "Undead General Geralt",
                    "Undead Dictator"]


    @property
    def Is_In_Stats(self):
        return self.__IS_IN_STATS

    @Is_In_Stats.getter
    def Is_In_Stats(self):
        return self.__IS_IN_STATS

    @Is_In_Stats.setter
    def Is_In_Stats(self, value):
        self.__IS_IN_STATS = value

    @property
    def Is_In_Shop(self):
        return self.__IS_IN_SHOP

    @Is_In_Shop.getter
    def Is_In_Shop(self):
        return self.__IS_IN_SHOP

    @Is_In_Shop.setter
    def Is_In_Shop(self, value):
        self.__IS_IN_SHOP = value


    @property
    def Is_Program_Run(self):
        return self.__IS_PROGRAM_RUN
    @Is_Program_Run.getter
    def Is_Program_Run(self):
        return self.__IS_PROGRAM_RUN
    @Is_Program_Run.setter
    def Is_Program_Run(self, value):
        self.__IS_PROGRAM_RUN = value

    @property
    def Is_Game_Run(self):
        return self.__IS_PLAY_GAME

    @Is_Game_Run.getter
    def Is_Game_Run(self):
        return self.__IS_PLAY_GAME

    @Is_Game_Run.setter
    def Is_Game_Run(self, value):
        self.__IS_PLAY_GAME = value

    @property
    def Is_Fight_Run(self):
        return self.__IS_FIGHT_GAME

    @Is_Fight_Run.getter
    def Is_Fight_Run(self):
        return self.__IS_FIGHT_GAME

    @Is_Fight_Run.setter
    def Is_Fight_Run(self, value):
        self.__IS_FIGHT_GAME = value



class FileSettings:
    __PATH_TO_SAVE = ""
    fileDictionary = {}
    __saveName=""

    @property
    def saveName(self):
        return self.__saveName

    @saveName.getter
    def saveName(self):
        return self.__saveName

    @saveName.setter
    def saveName(self, value):
        self.__saveName = value

    @property
    def pathToSave(self):
        return self.__PATH_TO_SAVE

    @pathToSave.getter
    def pathToSave(self):
        return self.__PATH_TO_SAVE

    @pathToSave.setter
    def pathToSave(self, value):
        self.__PATH_TO_SAVE = value


    def createFile(self, path):
        open(path, "x")
        f = open(path, "w")
        if f.writable():
            f.write("NAME="+str(self.fileDictionary["NAME"])+"\n")
            f.write("NEXTADV=" + str(self.fileDictionary["NEXTADV"]) + "\n")
            f.write("LEVEL="+str(self.fileDictionary["LEVEL"])+"\n")
            f.write("WEAPON="+str(self.fileDictionary["WEAPON"])+"\n")
            f.write("EXP="+str(self.fileDictionary["EXP"])+"\n")
            f.write("GOLD=" + str(self.fileDictionary["GOLD"]) + "\n")
            f.write("SKILLPOINT="+str(self.fileDictionary["SKILLPOINT"])+"\n")
            f.write("HEALTH="+str(self.fileDictionary["HEALTH"])+"\n")
            f.write("STRONG="+str(self.fileDictionary["STRONG"])+"\n")
            f.write("WITAL=" + str(self.fileDictionary["WITAL"]) + "\n")
            f.write("NAXDAMAGE="+str(self.fileDictionary["NAXDAMAGE"])+"\n")
            f.write("MINDAMAGE="+str(self.fileDictionary["MINDAMAGE"])+"\n")
            f.write("PACKETPOTION1=" + str(self.fileDictionary["PACKETPOTION1"]) + "\n")
            f.write("PACKETPOTION2=" + str(self.fileDictionary["PACKETPOTION2"]) + "\n")
        f.close()


    def removeFile(self, path):
        if self.getFileExist(path):
            os.remove(path)
        else:
            return print("Delete - Nie znaleziono pliku")

    def getFileExist(self, path):
        try:
            fil = open(path, "r")
            fil.close()
        except:
            return False

        return True

    def getFilePlayerName(sefl, path):
        fil = open(path, "r")
        name = ""
        complete = False
        if fil.readable():
            for i in fil:
                pierw = ""
                Scrstr = ""
                for x in i:
                    if i.index("=") != i.index(x) and complete == False:
                        pierw += x
                    else:
                        complete = True
                        if x == "=":
                            continue

                        if i.index("\n") == i.index(x):
                            if pierw == "NAME":
                                name = Scrstr
                                break
                        else:
                            Scrstr += str(x)
                complete = False
            fil.close()

        return name

    def loadFile(self, path):
        Fil = open(path, "r")
        valint = ""
        complete = False
        for i in Fil:
            pierw = ""
            Scrstr = ""
            for x in i:
                if i.index("=") != i.index(x) and complete == False:
                    pierw += x
                else:
                    complete = True
                    if x == "=":
                        continue

                    if i.index("\n") == i.index(x):
                        if pierw == "NAME" or  pierw == "NEXTADV":
                            self.fileDictionary[pierw] = Scrstr
                        else:
                            self.fileDictionary[pierw] = int(Scrstr)
                        break
                    else:
                        Scrstr += str(x)
            complete = False
        Fil.close()

        return valint

    def saveFile(self, path):
        f = open(path, "w")
        if f.writable():
            f.write("NAME=" + str(self.fileDictionary["NAME"]) + "\n")
            f.write("NEXTADV=" + str(self.fileDictionary["NEXTADV"]) + "\n")
            f.write("LEVEL=" + str(self.fileDictionary["LEVEL"]) + "\n")
            f.write("WEAPON=" + str(self.fileDictionary["WEAPON"]) + "\n")
            f.write("EXP=" + str(self.fileDictionary["EXP"]) + "\n")
            f.write("GOLD=" + str(self.fileDictionary["GOLD"]) + "\n")
            f.write("SKILLPOINT=" + str(self.fileDictionary["SKILLPOINT"]) + "\n")
            f.write("HEALTH=" + str(self.fileDictionary["HEALTH"]) + "\n")
            f.write("STRONG=" + str(self.fileDictionary["STRONG"]) + "\n")
            f.write("WITAL=" + str(self.fileDictionary["WITAL"]) + "\n")
            f.write("NAXDAMAGE=" + str(self.fileDictionary["NAXDAMAGE"]) + "\n")
            f.write("MINDAMAGE=" + str(self.fileDictionary["MINDAMAGE"]) + "\n")
            f.write("PACKETPOTION1=" + str(self.fileDictionary["PACKETPOTION1"]) + "\n")
            f.write("PACKETPOTION2=" + str(self.fileDictionary["PACKETPOTION2"]) + "\n")
        f.close()


    def getLastIdSave(self):
        id = 0

        while True:
            savepath = "Save/load0" + str(id) + ".txt"
            try:
                Fil = open(savepath,"r")

            except:
                break

            Fil.close()
            id += 1

        return id

