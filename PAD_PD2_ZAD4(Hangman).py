import random
import string

class Game():

    def _play(self):
        self.number_of_players()          
        print("Wybrales liczbe graczy = {}, zacznijmy gre".format(self.players_number))

    def number_of_players(self):
        players_number = None
        while (players_number is not type(int) and players_number not in range(1,3)):           
            try:
                players_number = int(input("Wybierz liczbe graczy (maks. 2)\n"))
                if(players_number not in range(1,3)):
                    print("Liczba graczy musi byc rowna 1 lub 2")
                else:
                    self.players_number = players_number
            except:
                print("Napisz liczbe graczy")

class Hangman(Game):

    def choose_word(self):
        words = ['kokos', 'ananas', 'jablko', 'cytryna'.upper()]
        word = random.randint(1,len(words))
        return words[word]

    def __init__(self):
        super().__init__()
        print("Wybierz poziom trudnosci: 1 - podstawowy 2 - sredni 3 - zaawansowany")
        while True:
            try:
                self.difficulty = int(input())
            except ValueError:
                print('Wybierz inna wartosc')
            else:
                if 1<= self.difficulty <=3:
                    break
                else:
                    print('Bledna wartosc')
        if self.difficulty == 1:
            self.chances_left = 8
        elif self.difficulty == 2:
            self.chances_left = 5
        elif self.difficulty == 3:
            self.chances_left = 3

    def _play(self):
        super()._play()
        if self.players_number == 1:
            word = self.choose_word().upper()
        else:
            print("Wpisz slowo, ktorego bedzie szukal drugi gracz:")
            word = input().upper()
        word = list(word)
        letters = []
        for i in range(0,len(word)):
            letters.append("_")
        print(F"Slowo do odgadniecia:\n{letters}")
        while True:
            try:
                print("Wpisz litere: ")
                letter = str(input()).upper()
                assert len(letter) == 1
                assert letter.isalpha()
            except AssertionError:
                print("Wpisz tylko jedna litere\n")
            else:
                if letter in word:
                    for i in range (0,len(word)):
                        if letter == word[i]:
                            letters[i] = letter
                    
                else:
                    self.chances_left -= 1
                    print(F'Wybrana litera nie znajduje sie w slowie')
                    
            print(F"Slowo do odgadniecia:\n{letters}\nLiczba pozostalych szans wynosi: {self.chances_left}")
            if self.chances_left == 0:
                print(F'Przegrana\nSlowem do odgadniecia bylo {word}')
                break
            if "_" not in letters:
                print('Wygrana')
                break
            

game = Hangman()
game._play()
