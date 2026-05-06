import random

class Game:
    def __init__(self, lista_personaggi, lista_domande):
        self.lista_personaggi = lista_personaggi
        self.lista_domande = lista_domande
        self.personaggio_segreto = None
        self.numero_domanda = 0
    
    def scegli_personaggio(self):
        self.personaggio_segreto = random.choice(self.lista_personaggi)
        
    def next_question(self):
        random.shuffle(self.lista_domande)
        
        attributi = []
        choices = []
        
        for d in self.lista_domande:
            if d.attributo not in attributi:
                choices.append(d)
                attributi.append(d.attributo)
            
        print("\nScegli una domanda (0 per indovinare):")
        
        i = 1
        for x in choices:
            print(f"{i}. {x.testo}")
            i += 1
        
        scelta = int(input("> "))
        if scelta == 0:
            return None
        while scelta >= 5:
            scelta = int(input("Input non valido. Prova ancora\n> "))
        self.numero_domanda += 1

        return choices[scelta-1]
        
    def check_answer(self, domanda):
        isCorrect = domanda.controlla(self.personaggio_segreto)
        
        if isCorrect:
            print("Risposta: Si")
        else:
            print("Risposta: No")
        
    def guess_personaggio(self):
        guess = input("\nChi pensi che sia?\n> ")
        answer = self.personaggio_segreto.nome.lower()
        
        if(guess in answer):
            print("\nCorretto! Hai indovinato il personaggio!")
            return True
        else:
            print("\nSbagliato! Non hai indovinato il personaggio!")
            return False
    
    def play(self):
        print('Bnevenuto al gioco "Chi è il Personaggio?"\nHo scelto un personaggio segreto. Cerca di indovinare chi è!\n')
        
        self.scegli_personaggio()
        inGame = True
        
        # print(self.personaggio_segreto.nome       #test correct answer
        
        while inGame:
            domanda = self.next_question()
            
            if domanda == None:
                self.guess_personaggio()
                inGame = False
            
            if inGame:
                self.check_answer(domanda)
                
            #controllo di tentativi
            if self.numero_domanda >= 10:
                inGame = False
                print("\nHai esaurito i tentativi!")

        print(f"\nHai fatto {self.numero_domanda} domande.\nIl personaggio segreto era {self.personaggio_segreto.nome}.")