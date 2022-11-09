from data import Rednit

people = []

def readFile():
    f = open('Munkafuzet.csv', 'r', encoding='UTF-8')
    f.readline()
    for row in f:
        r = Rednit(row.strip())
        people.append(r)
    f.close()

def writeFile():
    f = open('Munkafuzet.csv', 'w', encoding='UTF-8')
    for r in people:
        row = f'{r.name};{r.age};{r.gender};{r.residence};{r.children};{r.sexuality}\n'
        f.write(row)
    f.close()
    

def whichPerson():
        name = input('Keresés: ')
        index = 0
        for i in people:
            if name.lower() != people[i].lower():
                index += 1

        print(f'Kiválasztásra került: {people[index]}')
        
        return people[index]


def newPerson():
    name = input('Név: ')
    age = int(input('Kor: '))
    gender = input('Nem: ')
    residence = input('Lakhely: ')
    children = int(input('Utódok száma: '))
    sexuality = input('Vonzalom: ')
    row = f'{name};{age};{gender};{residence};{children};{sexuality}\n'
    f = open('Munkafüzet1.csv', 'a', encoding = 'UTF-8')
    f.write(row)
    f.close
    r = Rednit(row)
    people.append(r)

def modifyPerson():
    name = input('Név: ')
    for p in people:
        if p.name.lower() == name.lower():
            p.age = int(input('Kor: '))
            p.gender = input('Nem: ')
            p.residence = input('Százalék: ')
            p.children = int(input('Utódok száma: '))
            p.sexuality = input('Vonzalom: ')
            writeFile()
            return
    input('Ilyen nevű felhasználó nincs.')

def detailsPerson():
    name = input('Név:  ')
    for r in people:
        if name.lower() in r.name.lower():
            print(f'{r.name}, {r.age} éves {r.gender}. Lakhelye {r.residence}, {r.children} utódja van. Szexualitása {r.sexuality}. ')
    
    input('')



def deletePerson():
    name = input('Név: ')
    for r in people:
        if r.name.lower() == name.lower():
            people.remove(r)
            writeFile()
            return
    input('Ilyen nevű profil nincsen')

def registration():
    pass

def matchmaker():
    pass