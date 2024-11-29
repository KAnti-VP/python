vers = """Milyen volt szőkesége, nem tudom már,
De azt tudom, hogy szőkék a mezők,
Ha dús kalásszal jő a sárguló nyár
S e szőkeségben újra érzem őt."""

def szavakhossza(text):
    hosszak = {}
    szavak = text.split()
    for szo in szavak:
        hossz = len(szo)

        if szo[-1] in ',.':
            hossz -= 1

        if hossz in hosszak:
            hosszak[hossz] += 1
        else:
            hosszak[hossz] = 1

    return hosszak

def betudarabszam(text):
    betuk = {}
    for kar in text.lower(): # 
        if kar not in ',. \n':
            if kar in betuk:
                betuk[kar] += 1
            else:
                betuk[kar] = 1
    return betuk

def kiiratas(dikt):
    key_list = sorted(dikt.keys())
    data = '{'
    for key in key_list:
        data += f' {key}: {dikt[key]},'
    print(data[:-1] + ' }')


eredmeny = szavakhossza(vers)
kiiratas(eredmeny)

kiiratas(betudarabszam(vers))
