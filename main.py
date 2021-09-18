from time import sleep
from PlayerClass import Player
from GeneralSettingsClass import *
from AdversaryClass import Adv
from ItemClass import *
from random import randint as rand
gs = GeneralSettings()
fs = FileSettings()

adv = []
weaponList = [OneHanded(-1,"test",5,5,5,0),]
weaponShopList = [OneHanded(-1,"test",5,5,5,0),]
potionList = [HealPotion(1,"Heal Potion - Big",100,100),HealPotion(2,"Heal Potion - Medium",50,50),HealPotion(3,"Heal Potion - Low",20,20)]

GAME_NAME = "Test Fighter Game By XorD"

def usesPotion(potion):
    if potion != None:
        del potion

def getPotionEfect(potion):
    return potion.potionEfect

def getPotionId():
    for i in potionList:
        yield i.potionID

def setPotionFromId(POTION_ID):
    if POTION_ID == 0:
        return None
    else:
        for i in potionList:
            if i.potionID == POTION_ID:
                return i



def setWeaponList():
    lvwp = 1
    price = 10
    wl = 1
    weaponList.clear()
    for i in gs.weaponNameList:
        weaponList.append(OneHanded(wl,i,5*wl+5,10*wl+10,lvwp,price))
        wl += 1
        lvwp += 3
        price += (lvwp - rand(1,2)) *10

def setItemToShopList():
    weaponShopList.clear()
    for i in weaponList:
        wpl = i
        if wpl.weaponName == "Legendarny Miecz"or wpl.weaponName  == "Wyjątkowy miecz" or wpl.weaponName == "Miecz oficerski" or wpl.weaponName == "Miecz dyktatora":
           continue
        else:
            weaponShopList.append(wpl)
    for i in potionList:
        weaponShopList.append(i)

def setPlayerAdv(AdvName = "Bill"):

    isadv = False
    adn = AdvName
    sd=0

    if "Undead" in adn:
        lvadv = 50
        adv.clear()
        for i in gs.advnamelist2:
            if adn == i or isadv == True:
                if "Undead Dictator" == i:
                    lvadv = 81
                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)),setAdvWeapon(20)))

                else:
                    lvadv += rand(1, 5)
                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)),setAdvWeapon(rand(16,19))))

                isadv = True
            sd = +1

    else:
        adv.clear()
        lvadv = 5

        for i in gs.advnamelist:
            if adn != i and isadv == False:
                lvadv += 1


                continue
            else:

                if "dictator" == i.lower():
                    lvadv = 64

                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)),setAdvWeapon(16)))
                    break


                if "bill" == i.lower():

                    if rand(0, 1) == 1:
                        adv.append(Adv(i, 100 + lvadv * 10, 1, int(round(5 + lvadv * 0.5)),setAdvWeapon(1)))
                    else:
                        adv.append(Adv(i, 100 + lvadv * 10, 1, int(round(5 + lvadv * 0.5))))
                    continue


                if "sentenz" == i.lower() or "gabir" == i.lower():
                    lvadv += rand(2,5)

                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)),setAdvWeapon(rand(1, 3))))
                    continue

                if "officer sangure" == i.lower() or "officer kingers" == i.lower() or  "capitan harry" == i.lower() or "capitan richard" == i.lower():
                    lvadv = rand(50,60)
                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)), setAdvWeapon(rand(10,14))))
                    continue
                if "general geralt" == i.lower():
                    lvadv += 62
                    adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)), setAdvWeapon(15)))

                lvadv += 1
                adv.append(Adv(i, 100 + lvadv * 10, lvadv, int(round(5 + lvadv * 0.5)),setAdvWeapon(rand(3, 9))))


                isadv = True
            sd =+1



def showAdvList():
    print()
    e = 1
    for i in adv:

        print(str(e) + " - " + i.Name + ", LV " + str(i.Level))


        e+=1

    print()




def giveWeapon(who,WEAPON_ID):
    for i in weaponList:
        if i.weaponID == WEAPON_ID:
            who.playerWeapon = i
            break

def setAdvWeapon(WEAPON_ID):
    for i in weaponList:
        if i.weaponID == WEAPON_ID:
            return i


def getAdvWeapon(who):
    if who.advWeapon != None:
        return who.advWeapon.weaponName

    return "Brak"



def printMenu():
    print()
    print(GAME_NAME)
    print()
    print("G - Graj")
    print("L - Wczytaj")
    print("E - Wyjście")
    print()



def saveStats(WHOM):

    if fs.getFileExist(fs.pathToSave):
        fs.fileDictionary.clear()

        fs.fileDictionary = {"NAME": WHOM.Name,
                             "NEXTADV": WHOM.NextAdv,
                             "LEVEL": WHOM.Level,
                             "WEAPON": 0,
                             "EXP": WHOM.Exp,
                             "GOLD": WHOM.gold,
                             "SKILLPOINT":WHOM.SkillPonint,
                             "HEALTH":  WHOM.Health,
                             "STRONG": WHOM.Strong,
                             "WITAL": WHOM.wital,
                             "NAXDAMAGE": WHOM.MaxDamage,
                             "MINDAMAGE": WHOM.MinDamage,
                             "PACKETPOTION1": 0,
                             "PACKETPOTION2": 0}
        if WHOM.playerWeapon != None:
            fs.fileDictionary["WEAPON"] = WHOM.playerWeapon.weaponID
        if WHOM.packetToPotion1 != None:
            fs.fileDictionary["PACKETPOTION1"] = WHOM.packetToPotion1.potionID
            print(fs.fileDictionary["PACKETPOTION1"])
        if WHOM.packetToPotion2 != None:
            fs.fileDictionary["PACKETPOTION2"] = WHOM.packetToPotion1.potionID
            print(fs.fileDictionary["PACKETPOTION2"])

        fs.saveFile(fs.pathToSave)
    else:
        fs.fileDictionary.clear()
        fs.fileDictionary = {"NAME": WHOM.Name,
                             "NEXTADV": "Bill",
                             "LEVEL": 1,
                             "WEAPON": 0,
                             "EXP": 1,
                             "GOLD": 5,
                             "SKILLPOINT": 5,
                             "HEALTH": 150,
                             "STRONG": 5,
                             "WITAL": 5,
                             "NAXDAMAGE": 5,
                             "MINDAMAGE": 5,
                             "PACKETPOTION1": 0,
                             "PACKETPOTION2": 0}

        fs.createFile(fs.pathToSave)


def loadStats(WHOM):
    fs.loadFile(fs.pathToSave)
    WHOM.Name = fs.fileDictionary["NAME"]
    WHOM.NextAdv = fs.fileDictionary["NEXTADV"]
    WHOM.Level = fs.fileDictionary["LEVEL"]
    giveWeapon(WHOM, fs.fileDictionary["WEAPON"])
    WHOM.Exp = fs.fileDictionary["EXP"]
    WHOM.gold = fs.fileDictionary["GOLD"]
    WHOM.ExpToNextLv = WHOM.Level * 50
    WHOM.SkillPonint = fs.fileDictionary["SKILLPOINT"]
    WHOM.Health = fs.fileDictionary["HEALTH"]
    WHOM.Strong = fs.fileDictionary["STRONG"]
    WHOM.wital = fs.fileDictionary["WITAL"]
    WHOM.packetToPotion1 = setPotionFromId(fs.fileDictionary["PACKETPOTION1"])
    WHOM.packetToPotion2 = setPotionFromId(fs.fileDictionary["PACKETPOTION2"])

    if WHOM.playerWeapon != None:
        WHOM.MaxDamage =  WHOM.playerWeapon.weaponMaxDamage
        WHOM.MinDamage =  WHOM.playerWeapon.weaponMinDamage
    else:
        WHOM.MaxDamage = fs.fileDictionary["NAXDAMAGE"]
        WHOM.MinDamage = fs.fileDictionary["MINDAMAGE"]
    WHOM.MAX_PLAYER_HEALT = 100 + player.wital * 10

def gameMenu():
    if gs.Is_Fight_Run == True:
        if player.playerWeapon == None:
            print("R - Uderz prawą ręką ")
            print("L - Uderz lewa ręką ")
        else:
            print("M - Mocny atak ")
            print("S - Słaby atak ")

        if player.packetToPotion1 != None or player.packetToPotion2 != None:
            print("P - Użyj Miksutre")
        print("U - Uciekaj ")
    else:
        print("C - Wyzwij kogoś na pojedynek ")
        if player.packetToPotion1 != None or player.packetToPotion2 != None:
            print("P - Użyj Miksutre")
        print("S - Sprawdź statystyki ")
        print("A - Sprawdź liste rywali ")
        print("B - Idz do sklepu")
        print("E - Wróc do menu głównego ")




while gs.Is_Program_Run:
    setWeaponList()
    setItemToShopList()
    setPlayerAdv()

    if gs.Is_Game_Run:


        print()
        sleep(2)
        player = Player("Null")
        if fs.getFileExist(fs.pathToSave) == False:
            print("Podaj nazwę: ")
            odp = input(">> ")
            print()
            fs.pathToSave = "Save/load0" + str(fs.getLastIdSave())+".txt"
            player.Name = odp
            saveStats(player)
            loadStats(player)
            print("Witaj w grze " + GAME_NAME)
            print("Twoja postać nazywa sie "+ player.Name)
            print()
        else:

            loadStats(player)
            print("Witaj",player.Name)
            print()


        print(player.NextAdv)

        while gs.Is_Game_Run:
            while gs.Is_In_Stats:
                print()
                player.checkstats()
                print()
                if player.SkillPonint > 0:

                    print("W All - Rozdaj wszystkie punkty umiejetnosci w Witalność")

                    if player.SkillPonint >= 100:
                        print("W 100 - Rozdaj 100 punkty umiejetnosci w Witalność")

                    if player.SkillPonint >= 50:
                        print("W 50 - Rozdaj 50 punkty umiejetnosci w Witalność")

                    if player.SkillPonint >= 10:
                        print("W 10 - Rozdaj 10 punkty umiejetnosci w Witalność")

                    print("W - Rozdaj punkt umiejetnosci w Witalność")
                    print()
                    print("S All - Rozdaj wszystkie punkty umiejetnosci w Siłe")

                    if player.SkillPonint >= 100:
                        print("S 100 - Rozdaj 100 punkty umiejetnosci w Siłe")
                    if player.SkillPonint >= 50:
                        print("S 50 - Rozdaj 50 punkty umiejetnosci w Siłe")
                    if player.SkillPonint >= 10:
                        print("S 10 - Rozdaj 10 punkty umiejetnosci w Siłe")

                    print("S - Rozdaj punkt umiejetnosci w Siłe")
                    print()
                    print("E - Wróć")
                    print()
                    odp = input(">> ")
                    if "w" in odp.lower():
                        if "all" in odp.lower():
                            player.wital += player.SkillPonint
                            player.SkillPonint = 0
                        elif "100" in  odp.lower():
                            if  player.SkillPonint >= 100:
                                player.wital += 100
                                player.SkillPonint -= 100
                        elif "50" in  odp.lower():
                            if player.SkillPonint >= 50:
                                player.wital += 50
                                player.SkillPonint -= 50
                        elif "10" in  odp.lower():
                            if player.SkillPonint >= 10:
                                player.wital += 10
                                player.SkillPonint -= 10
                        else:
                            player.wital += 1
                            player.SkillPonint -= 1

                        player.MAX_PLAYER_HEALT += (player.SkillPonint * 10)
                        player.Health = player.MAX_PLAYER_HEALT

                    if  "s" in odp.lower():
                        if "all" in odp.lower():

                            player.Strong += player.SkillPonint
                            player.SkillPonint = 0
                        elif "100" in odp.lower():
                            if player.SkillPonint >= 100:
                                player.Strong += 100
                                player.SkillPonint -= 100
                        elif "50" in odp.lower():
                            if player.SkillPonint >= 50:
                                player.Strong += 50
                                player.SkillPonint -= 50
                        elif "10" in odp.lower():
                            if player.SkillPonint >= 10:
                                player.Strong += 10
                                player.SkillPonint -= 10
                        else:
                            player.Strong += 1
                            player.SkillPonint -= 1

                    if odp.lower() == "e":
                        saveStats(player)
                        loadStats(player)
                        gs.Is_In_Stats = False
                else:
                    gs.Is_In_Stats = False
            while gs.Is_In_Shop:
                shw = []
                shid = []
                s = 1
                p = 1
                idw = ""
                print()
                potionboll = False
                shw.clear()
                for i in weaponShopList:
                    try:
                        print(str(i.weaponID) + " - Kup (" + str(i.weaponPrice) + " Gold) " + i.weaponName +
                              " LV: " + str(i.weaponLevel) + " DMG: " + str(i.weaponMinDamage) +
                              " - " + str(i.weaponMaxDamage) + "")
                    except:
                        print("P" +str(i.potionID) + " - Kup (" + str(i.potionPrice) + " Gold) " + i.potionName)
                        shw.append("P" + str(p))
                    s += 1
                    p += 1
                print()
                print("E - Wróc")
                print()
                print("Co chcesz zrobić")
                odp = input(">> ")
                try:
                    idw = int(odp)
                except:
                    if "p" in odp.lower():
                        potionboll = True
                    elif odp.lower() == "e":
                        gs.Is_In_Shop = False
                        break
                    else:
                        continue

                if potionboll == True:
                    fail = False

                    for i in potionList:
                        for x in odp.lower():
                            if x.lower() == "p":
                                continue
                            else:
                                try:
                                    idw = int(x)
                                except:
                                    fail = True
                                    break
                    if fail == True:
                        print("Wystąpił bład")
                        continue
                    for i in potionList:
                        if i.potionID == idw:
                            if player.gold < i.potionPrice:
                                print()
                                print("Masz za mało golda!")
                                print()
                                break
                            if player.packetToPotion1 != None and player.packetToPotion2 != None:
                                print()
                                print("Nie masz miejsca na kolejne mikstury!")
                                print()
                                break
                            else:

                                print("Kupiłes miksture " + i.potionName + " za " + str(
                                    i.potionPrice) + " golda!")
                                player.gold -= i.potionPrice
                                if player.packetToPotion1 == None:
                                    player.packetToPotion1 = i
                                elif player.packetToPotion2 == None:
                                    player.packetToPotion2 = i
                                break
                else:
                    for i in weaponList:
                        if i.weaponID == idw:
                            if player.gold < i.weaponPrice:
                                print()
                                print("Masz za mało golda!")
                                print()
                                break
                            elif player.Level < i.weaponLevel:
                                print()
                                print("Masz za niski poziom!")
                                print()
                                break
                            else:
                                if player.playerWeapon != None:
                                    cash = player.playerWeapon.weaponPrice *0.5
                                    print("Sprzedałes broń " + player.playerWeapon.weaponName + " za " + cash + " golda!")
                                    weaponShopList.append(player.playerWeapon)
                                    player.playerWeapon = None
                                    player.MinDamage = 1
                                    player.MaxDamage = 5
                                    print()


                                print("Kupiłes broń " + i.weaponName + " za " + str(i.weaponPrice) + " golda!")
                                player.gold -= i.weaponPrice
                                player.playerWeapon = i
                                weaponShopList.remove(i)
                                player.MinDamage = i.weaponMinDamage
                                player.MaxDamage = i.weaponMaxDamage
                                saveStats(player)
                                loadStats(player)
                                break

            if player.NextAdv != adv[0].Name:
                setPlayerAdv(player.NextAdv)
            if gs.Is_Game_Run == False:
                break

            bre = ""
            if adv[0].advWeapon == None:
                bre = " Brak"
            else:
                bre = adv[0].advWeapon.weaponName

            print("Twój kolejny przeciwnik " + adv[0].Name + " |HP: " + str(adv[0].Health) + ",  LV: " + str(
                adv[0].Level) +", Broń " + bre +"|")
            print()
            if player.playerWeapon == None:
                bre = " Brak"
            else:
                bre = player.playerWeapon.weaponName
            print(player.Name + " |HP: " + str(player.Health) + ",  LV: " + str(player.Level) + ",  GOLD: " + str(
                player.gold) + ", Broń " +bre+"|")
            print()

            gameMenu()
            print()
            print("Co chcesz zrobić?")
            odp = input(">> ")
            print()


            if odp.lower() == "c":

                gs.Is_Fight_Run = True
                while gs.Is_Fight_Run:

                    if player.Health <= 0:

                        if potionList[1].potionPrice > player.gold:
                            print("Przegrałes! Ilość Twojego golda nie wystarczy na zakup nowych mikstur")
                            print("Czy chcesz zakonczyć gre? Twój zapis zostanie usunięty")
                            print("T - Tak, N - Nie")
                            odp = input(">> ")
                            if odp.lower() == "t":
                                fs.removeFile(fs.pathToSave)
                            elif odp.lower() == "n":
                                pass
                            else:
                                continue
                        ex = rand(1, int(round(player.gold * 0.5,0)))
                        sleep(2)
                        if player.gold >= ex:
                            player.gold = player.gold - ex
                            adv[0].stealGold = adv[0].stealGold + ex
                            print("Zemdlałeś od obrażeń! " + adv[0].Name + " zabiera  " + str(ex) + " Golda")
                        elif player.gold < ex:
                            adv[0].stealGold = adv[0].stealGold + player.gold
                            player.gold = 0
                            print("Zemdlałeś od obrażeń! " + adv[0].Name + " zabiera cały Twój gold")
                        player.Health = 1
                        saveStats(player)
                        loadStats(player)
                        gs.Is_Fight_Run = False
                        break
                    if adv[0].Health <= 0:
                        if adv[0].Name == "Undead Dictator":
                            print("To juz koniec tej gry :)")
                            gs.Is_In_Stats = False
                            gs.Is_Fight_Run = False
                            gs.Is_In_Shop = False
                            gs.Is_Game_Run = False
                            gs.Is_Program_Run = False
                            print("Dziekuje za uwagę")
                            break


                        ex = player.Level*10 + adv[0].Level*10
                        sleep(2)
                        if adv[0].stealGold > 0:
                            gl = adv[0].stealGold + (adv[0].Level*10 - rand(1,5))
                        else:
                            gl = adv[0].Level * 10 - rand(1, 5)


                        player.Exp = player.Exp + ex
                        player.gold = player.gold +gl
                        player.checklevelup()

                        try:
                            player.NextAdv = adv[1].Name
                        except:
                            player.NextAdv = "Undead Bill"

                        if player.playerWeapon.weaponMaxDamage < adv[0].advWeapon.weaponMaxDamage:
                            if player.playerWeapon != None:
                                player.gold += player.playerWeapon.weaponPrice * 0.5
                                print("Sprzedałes swoją broń " + player.playerWeapon.weaponName + " za " + str(
                                    player.playerWeapon.weaponPrice * 0.5))
                            player.playerWeapon = None
                            player.playerWeapon = adv[0].advWeapon
                            adv[0].advWeapon = None
                            print("Odebrałes broń " + adv[0].advWeapon.weaponName)

                        print("Wygrałes! Otrzymujesz " + str(ex) + " Expa i " + str(gl) + " Golda")
                        saveStats(player)
                        loadStats(player)
                        setPlayerAdv(player.NextAdv)

                        gs.Is_Fight_Run = False
                        break
                    advr = rand(0,3)
                    if advr == 0:
                        if adv[0].advWeapon != None:
                            adv[0].advWeapon.advHardAtack(player,adv[0].Strong)
                        else:
                            adv[0].atackRightHand(player)
                    elif advr == 1:
                        if adv[0].advWeapon != None:
                            adv[0].advWeapon.advLowAtack(player,adv[0].Strong)
                        else:
                            adv[0].atackLeftHand(player)

                    else:
                        pass
                    if adv[0].advWeapon != None:
                        print(player.Name +" |HP: " + str(player.Health) + ",  LV: " + str(player.Level) + "| " + adv[0].Name + " |HP: " + str(adv[0].Health) + ",  LV: " + str(adv[0].Level) +", Broń: " + str(adv[0].advWeapon.weaponName) + "|")
                    else:
                        print(player.Name +" |HP: " + str(player.Health) + ",  LV: " + str(player.Level) + "| " + adv[0].Name + " |HP: " + str(adv[0].Health) + ",  LV: " + str(adv[0].Level) +", Broń: Brak|")

                    print()
                    gameMenu()
                    print()
                    print("Co chcesz zrobić?")
                    odp = input(">> ")
                    print()
                    if odp.lower() == "r":
                        if player.playerWeapon == None:
                            player.atackRightHand(adv[0])
                    elif odp.lower() == "l":
                        if player.playerWeapon == None:
                            player.atackLeftHand(adv[0])
                    elif odp.lower() == "m":
                        if player.playerWeapon != None:
                            player.playerWeapon.hardAtack(adv[0],player.Strong)
                    elif odp.lower() == "s":
                        if player.playerWeapon != None:
                            player.playerWeapon.lowAtack(adv[0], player.Strong)
                    elif odp.lower() == "p":
                        if player.Health < player.MAX_PLAYER_HEALT:
                            if player.packetToPotion2 != None:

                                if (getPotionEfect(player.packetToPotion2) + player.Health) > player.MAX_PLAYER_HEALT:
                                    player.Health = player.MAX_PLAYER_HEALT

                                else:
                                    player.Health += getPotionEfect(player.packetToPotion2)

                                usesPotion(player.packetToPotion2)
                                player.packetToPotion2 = None
                                print("Uleczyłeś się!")
                                print()
                            elif player.packetToPotion1 != None:

                                if (getPotionEfect(player.packetToPotion1) + player.Health) > player.MAX_PLAYER_HEALT:
                                    player.Health = player.MAX_PLAYER_HEALT

                                else:
                                    player.Health += getPotionEfect(player.packetToPotion1)

                                usesPotion(player.packetToPotion1)
                                player.packetToPotion1 = None
                                print("Uleczyłeś się!")
                                print()
                            else:
                                print("Brak mikstur!")
                                print()
                        else:
                            print("Masz makasymalna liczbę punktów zdrowia!")
                            print()
                    elif odp.lower() == "u":
                        gs.Is_Fight_Run= False

            elif odp.lower() == "s":
                gs.Is_In_Stats = True
            elif odp.lower() == "a":
                showAdvList()
            elif odp.lower() == "p":
                if player.Health < player.MAX_PLAYER_HEALT:
                    if player.packetToPotion2 != None:
                        print(getPotionEfect(player.packetToPotion2))
                        if (getPotionEfect(player.packetToPotion2) + player.Health) > player.MAX_PLAYER_HEALT:
                            player.Health = player.MAX_PLAYER_HEALT

                        else:
                            player.Health += getPotionEfect(player.packetToPotion2)

                        usesPotion(player.packetToPotion2)
                        player.packetToPotion2 = None
                        print("Uleczyłeś się!")
                    elif player.packetToPotion1 != None:

                        if (getPotionEfect(player.packetToPotion1) + player.Health) > player.MAX_PLAYER_HEALT:
                            player.Health = player.MAX_PLAYER_HEALT

                        else:
                            player.Health += getPotionEfect(player.packetToPotion1)

                        usesPotion(player.packetToPotion1)
                        player.packetToPotion1 = None
                        print("Uleczyłeś się!")
                    else:
                        print("Brak mikstur!")
                else:
                    print("Masz makasymalna liczbę punktów zdrowia!")

            elif odp.lower() == "b":
                gs.Is_In_Shop = True
            elif odp.lower() == "e":
                saveStats(player)
                gs.Is_Game_Run = False
                break





    else:
        printMenu()
        print("Co chcesz zrobić?")
        odp = input(">> ")

        if odp.lower() == "g":
            fs.pathToSave = ""
            gs.Is_Game_Run = True
            continue
        elif odp.lower() == "l":
            sew = []
            e=0
            issave= False
            avepath = ""
            print()
            print("Twoje zapisy:")
            print()
            while True:
                sew.append("S" +str(e))
                try:
                    avepath = "Save/load0" + str(e) + ".txt"
                    Fil = open(avepath,"r")
                    print(sew[e], "- " + fs.getFilePlayerName(avepath))
                    issave = True
                except:
                    break

                e += 1

            print()
            if issave == False:
                print("Brak zapisów")
                print()
                continue
            print("Który save chcesz załądować?")

            odp = input(">> ")
            for i in sew:

                if odp.lower() == i.lower():
                    for x in odp:
                        if x.lower() == "s":
                            continue
                        else:
                            fs.pathToSave ="Save/load0"+str(x)
                            gs.Is_Game_Run = True

            fs.pathToSave += ".txt"

        elif odp.lower() == "e":
            gs.Is_Program_Run = False
            break
        else:
            continue