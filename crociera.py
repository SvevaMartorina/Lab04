import csv
from logging import exception

from cabina import Cabina, CabinaAnimali, CabinaDelux
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome

        self.cabine = []
        self.passeggeri = []
        self.abbinamenti = [] #lista di tuple, coppie

    """Aggiungere setter e getter se necessari"""
    @property
    #Getter restituisce il numero
    def nome(self):
        return self._nome

    @nome.setter
    #Setter imposta il nuovo nome, deciso dall'utente
    def nome(self, valore):
        self._nome = valore

#sistemare gli indici con if line < 4...
    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with (open(file_path, 'r', encoding='utf-8') as f):
                reader = csv.reader(f)
                for line in reader:
                    #for el in line:
                        #el.strip() #pulisco i vari campi, per evitare errori nei controlli successivi
                    if not line: #se la linea è vuota la salto
                        continue
                    if len(line) == 4: #se ha 4 campi è una cabina
                        if line[0].startswith("CA"):  # se il primo campo inizia per CA è una cabina
                            nuova_cabina = Cabina(line[0], line[1], line[2], line[3])
                            self.cabine.append(nuova_cabina)

                    elif len(line) == 5: #se ha 5 campi è una cabina della sottoclasse
                        if line[4].isdigit(): # se il quinto campo è un numero indica il numero di animali
                                nuova_cabina = CabinaAnimali(line[0], line[1], line[2], line[3], line[4])
                                self.cabine.append(nuova_cabina)
                        elif line[4].isalpha(): # se il quinto campo è una stringa, allora è una cabina deluxe
                            nuova_cabina = CabinaDelux(line[0], line[1], line[2], line[3], line[4])
                            self.cabine.append(nuova_cabina)

                    elif len(line) == 3: #se ha 3 campi è un passeggero
                        if line[0].startswith("P"): # se il primo carattere inizia con P è un passeggero
                            nuovo_passeggero = Passeggero(line[0], line[1], line[2])
                            self.passeggeri.append(nuovo_passeggero)
        except FileNotFoundError:
            print("File non trovato")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        #verifico che passeggero e cabina selezionati esistano
        cabina_esiste = False
        for cab in self.cabine:
            if cab.codice == codice_cabina:
                cabina = cab
                cabina_esiste = True
        if not cabina_esiste:
            raise Exception('La cabina non esiste')
        passeggero_esiste = False
        for pas in self.passeggeri:
            if pas.codice == codice_passeggero:
                passeggero_esiste = True
        if not passeggero_esiste:
            raise Exception('Il passeggero non esiste')

        #verifico che il passeggero e la cabina non hanno altri accoppiamenti
        for abbinamento in self.abbinamenti:
            if codice_cabina == abbinamento[0]:
                raise Exception('la cabina è già occupata')

            if codice_passeggero == abbinamento[1]:
                raise Exception('al passeggero è già stata assegnata una cabina')

        # se cabina e passeggero non sono abbinati
        nuovo_abbinamento = [codice_cabina, codice_passeggero]
        self.abbinamenti.append(nuovo_abbinamento)
        cabina.occupata = True
        return

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        lista_ordinata = sorted(self.cabine, key = lambda cab: float(cab.prezzo))
        return lista_ordinata

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for pas in self.passeggeri:
            trovato = False
            for abbinamento in self.abbinamenti:
                if pas.codice == abbinamento[1]:
                    trovato = True
                    print( f'{pas}, {abbinamento[0]}')
                    break
            if not trovato:
                print(pas)
        return