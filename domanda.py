class Domanda:
    def __init__(self, testo, attributo, valore_atteso):
        self.testo = testo
        self.attributo = attributo
        self.valore_atteso = valore_atteso
        
    def controlla(self, personaggio):
        if self.attributo == "professione":
            return self.valore_atteso == personaggio.professione
        elif self.attributo == "nazionalita":
            return self.valore_atteso == personaggio.nazionalita
        elif self.attributo == "epoca":
            return self.valore_atteso == personaggio.epoca
        elif self.attributo == "genere":
            return self.valore_atteso == personaggio.genere