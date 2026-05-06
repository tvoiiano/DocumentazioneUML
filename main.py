from personaggio import Personaggio
from data import dati_personaggi, dati_domande
from domanda import Domanda
from game import Game

lista_personaggi = []
for p in dati_personaggi:
    lista_personaggi.append(Personaggio(p["nome"], p["professione"], p["nazionalita"], p["epoca"], p["genere"]))

lista_domande = []
for d in dati_domande:
    lista_domande.append(Domanda(d["testo"], d["attributo"], d["valore_atteso"]))

game = Game(lista_personaggi, lista_domande)

game.play()