import copy


class XExpansion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    def __str__(self):
        return (f"oggetto creato da Samu XEspansion")

    def calcola_list(self, input):
        self.soluzioni_list = []
        self._ricorsione_list([], input)

    # parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione_list(self, parziale: list, rimanenti: str):
        # caso terminale
        if len(rimanenti) == 0:
            # print(parziale)
            self.soluzioni_list.append(copy.deepcopy(parziale))
        # caso ricorsivo
        else:
            if rimanenti[0] == 'X':

                #ciclare sui step possibili
                for c in ["0", "1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])


    def calcola(self, input):
        self.soluzioni = []
        self._ricorsione("", input)

    #parziale è la soluzione parziale
    # rimanenti sono il resto dei caratteri da esaminare
    def _ricorsione(self, parziale: str, rimanenti: str):
        #caso terminale
        if len(rimanenti) ==0:
            #print(parziale)
            self.soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0] == 'X':
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

if __name__ == '__main__':
    sequenza = "X10"
    xexp = XExpansion()

    #metodo con soluzioni parziali rappresentanti come stringhe
    xexp.calcola(sequenza)
    print(xexp.soluzioni)

    #metodo con soluzioni parziali come una lista
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)