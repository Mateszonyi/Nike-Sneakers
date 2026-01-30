from pprint import pprint


def beker():
    print('Válassz, melyik szempont alapján rendezzem a cipőket?')
    print('1 - title')
    print('2 - color')
    print('3 - full price')
    print('4 - current price')
    print('5 - publish date')
    valasz = int(input('Add meg a lehetőség számát! '))
    print('')
    return valasz


def osszcipo():
    with open('Nike_shoes_2023-04-16.csv', 'r', encoding='utf-8') as forrasfajl:
        next(forrasfajl)
        cipok = []
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            cipo = {
                'color': adatok[4],
                'current_price': float(adatok[6]),
                'full_price': float(adatok[5]),
                'publish_date': adatok[9],
                'title': adatok[1]
            }
            cipok.append(cipo)
    return cipok


def main():
    adatlista = osszcipo()
    valasztott_szam = beker()

    if valasztott_szam == 1:
        keresesi_ertek = 'title'
    elif valasztott_szam == 2:
        keresesi_ertek = 'color'
    elif valasztott_szam == 3:
        keresesi_ertek = 'full_price'
    elif valasztott_szam == 4:
        keresesi_ertek = 'current_price'
    else:
        keresesi_ertek = 'publish_date'

    pprint(sorted(adatlista, key=lambda szures: szures[keresesi_ertek]))


main()