class Passeggero:
    def __init__(self,codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __repr__(self):
        return (f'{type(self).__name__} '
                f'{self.codice}: Nome: {self.nome} '
                f'Cognome: {self.cognome}')
