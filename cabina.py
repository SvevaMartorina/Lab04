class Cabina:
    def __init__(self, codice, num_letti, ponte, prezzo):
        self.codice = codice
        self.num_letti = num_letti
        self.ponte = ponte
        self.prezzo = prezzo

        self.cabine = []
    def __repr__(self):
        return (f'{type(self).__name__} '
                f'{self.codice}: {self.num_letti} letti -'
                f'Ponte {self.ponte} - Prezzo {self.prezzo}€ - Disponibile')


class CabinaAnimali(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, num_animali):
        super().__init__(codice,num_letti, ponte, prezzo)
        #sovrapprezzo pari al 10% per ogni animale ammesso
        self.prezzo = float(prezzo) * (1 + 0.10 * int(num_animali))
        self.num_animali = num_animali

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'{self.codice}: {self.num_letti} letti -'
                f'Ponte {self.ponte} - Prezzo {self.prezzo}€ '
                f'- Max animali:{self.num_animali} - Disponibile')

class CabinaDelux(Cabina):
    def __init__(self, codice, num_letti, ponte, prezzo, stile):
        super().__init__(codice, num_letti, ponte, prezzo)
        #sovrapprezzo fisso del 20%
        self.prezzo = float(prezzo) * 1.20

        self.stile = stile

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'{self.codice}: {self.num_letti} letti -'
                f'Ponte {self.ponte} - Prezzo {self.prezzo}€ '
                f'- Stile: {self.stile} - Disponibile')


