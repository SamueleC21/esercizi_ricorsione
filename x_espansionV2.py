

def x_expansion2(input):
    soluzioni = []

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def ricorsione(parziale: str, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            soluzioni.append(parziale)
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                ricorsione(parziale + '0', rimanenti[1:])
                ricorsione(parziale + '1', rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])

    ricorsione("", input)
    return soluzioni


if __name__ == '__main__':
    sequenza = "01XX"
    print(x_expansion2(sequenza))
