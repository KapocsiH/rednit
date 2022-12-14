from data import Rednit
import menu
import os
people = []
# choosenperson = []

def readFile():
    f = open('data.csv', 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

def writeFile():
    f = open('data.csv', 'w', encoding='UTF-8')
    for r in people:
        row = f'{r.name};{r.age};{r.gender};{r.residence};{r.children};{r.sexuality}\n'
        f.write(row)
    f.close()

def newPerson():
    name = input('Teljes név: ')
    age = int(input('Kor: '))
    gender = input('Nem: ')
    residence = input('Lakhely: ')
    children = int(input('Utódok száma: '))
    sexuality = input('Vonzalom: ')
    row = f'{name};{age};{gender};{residence};{children};{sexuality}\n'
    f = open('data.csv', 'a', encoding = 'UTF-8')
    f.write(row)
    f.close
    r = Rednit(row)
    people.append(r)
    input('\nSikeres regisztráció.\n\nEnterrel visszaléphet a menübe.')

def modifyPerson():
    name = input('A változtatni kívánt alany teljes neve: ')
    for r in people:
        if r.name.lower() == name.lower():
            r.gender = input('Nem: ')
            r.residence = input('Lakhely: ')
            r.children = int(input('Utódok száma: '))
            r.sexuality = input('Vonzalom: ')
            writeFile()
            input('\nAz adatok módosultak.\n\nEnterrel visszaléphet a menübe.')
    input('\nIlyen nevű profil nincsen.\n\nEnterrel visszaléphet a menübe.')

def detailsPerson():
    name = input('Név:  ')
    for r in people:
        if name.lower() in r.name.lower():
            print(f'{r.name}, {r.age} éves {r.gender}. Lakhelye {r.residence}, {r.children} utódja van. Szexualitása {r.sexuality}.')
    print(f'Ha nem kapott nevet, akkor {name} nincs a listában.')
    input('\nEnterrel visszaléphet a menübe.')
    

def deletePerson():
    name = input('Teljes név: ')
    for r in people:
        if r.name.lower() == name.lower():
            people.remove(r)
            writeFile()
            os.system('cls')
            menu.menu2()
    input('\nIlyen nevű profil nincsen.\n\nEnterrel visszaléphet a menübe.')

def matchmaker():
    print('\nKis segítség: A Matchmaker funkcióval a felhasználók elvárások alapján kereshetnek kamu profilokat. Az, hogy melyik kamu\nprofil alkalmas az illetőnek, a szűrők alapján dőlik el.\n\nSzűrők:\nkor\nnem\nutódok\nvonzalom\n')
    print('Mi alapján szeretne keresni?\n')
    print('1. Kor, 2. Nem, 3. Utódok száma, 4. Szexualitás\n')
    choice = int(input('Választás:  '))
    while choice < 1 or choice > 4:
        choice = int(input('Választás:  '))
    if choice == 1:
        print('Korkategória:')
        print('1. -25')
        print('2. 26-45')
        print('3. 45-')
        agepreferance = int(input('Választás:  '))
        while agepreferance < 1 or agepreferance > 3:
            agepreferance = int(input('Választás:  '))
        suitable = []
        if agepreferance == 1:
            for r in people:
                if r.age <= 25:
                    suitable.append(f'{r.name}')
        elif agepreferance == 2:
            for r in people:
                if r.age >= 26 and r.age <= 45:
                    suitable.append(r.name)
        elif agepreferance == 2:
            for r in people:
                if r.age >= 26 and r.age <= 45:
                    suitable.append(r.name)
        print('Megfelelő profilok:') 
        print(suitable)
        print('')
    elif choice == 2:
        print('Nemek:')
        print('1. Férfi')
        print('2. Nő')
        print('3. Egyéb')
        genderpreferance = int(input('Választás:  '))
        while genderpreferance < 1 or genderpreferance > 3:
            genderpreferance = int(input('Választás:  '))
        suitable = []
        if genderpreferance == 1:
            for r in people:
                if r.gender == 'férfi':
                    suitable.append(r.name)
        elif genderpreferance == 2:
            for r in people:
                if r.gender == 'nő':
                    suitable.append(r.name)
        elif genderpreferance == 3:
            print('\nNincs ilyen nemű felhasználónk.')
        print('\nMegfelelő profilok:') 
        print(suitable)
    elif choice == 3:
        print('Utódok száma:')
        print('1. Nincs utód')
        print('2. 1')
        print('3. 2')
        print('4. Több')
        childpreferance = int(input('Választás:  '))
        while childpreferance < 1 or childpreferance > 3:
            childpreferance = int(input('Választás:  '))
        suitable = []
        if childpreferance == 1:
            for r in people:
                if r.children == 0:
                    suitable.append(r.name)
        elif childpreferance == 2:
            for r in people:
                if r.children == 1:
                    suitable.append(r.name)
        elif childpreferance == 3:
            for r in people:
                if r.children == 2:
                    suitable.append(r.name)
        elif childpreferance == 4:
            for r in people:
                if r.children > 2:
                    suitable.append(r.name)
        print('Megfelelő profilok:') 
        print(suitable)
        print('')
    elif choice == 4:
        print('Szexualitás:')
        print('1. Heteroszexuális')
        print('2. Homoszexuális')
        print('3. Egyéb')
        sexualitypreferance = int(input('Választás:  '))
        while sexualitypreferance < 1 or sexualitypreferance > 3:
            sexualitypreferance = int(input('Választás:  '))
        suitable = []
        if sexualitypreferance == 1:
            for r in people:
                if r.sexuality == 'Heteroszexuális':
                    suitable.append(r.name)
        elif sexualitypreferance == 2:
            for r in people:
                if r.sexuality == 'Homoszexuális':
                    suitable.append(r.name)
        elif sexualitypreferance == 3:
            for r in people:
                if r.sexuality == 'Egyéb':
                    suitable.append(r.name)
        print('Megfelelő profilok:') 
        print(suitable)
        print('')
    input('\nIn aura est amor.\n\nEnterrel visszaléphet a menübe.')