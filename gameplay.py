from pokoj import Pokoj
import pickle

class Gameplay:
    def __init__(self):
        self.pokoje = self.createRooms()

    def createRooms(self):
        # zdefinowanie pokojów
        pokoj1 = Pokoj("Wejście", "Jesteś w wejściu do zamku.")
        pokoj2 = Pokoj("Korytarz", "Jesteś na korytarzu.")
        pokoj3 = Pokoj("Zbrojownia", "Jesteś w zbrojowni.")
        pokoj4 = Pokoj("Wyjście", "Znalazłeś wyjście!")

        # zdefiniowanie połaczen pokoi
        pokoj1.addRelation("north", pokoj2)
        pokoj2.addRelation("south", pokoj1)
        pokoj2.addRelation("east", pokoj3)
        pokoj3.addRelation("west", pokoj2)
        pokoj3.addRelation("north", pokoj4)

        return [pokoj1,pokoj2,pokoj3,pokoj4]

    def start(self):
        print("Witaj w grze 'Escaperom'!\nodpowiadaj na zagadki i odnajdz wyjscie!\nnawigacja w grze: north, south, "
              "east, west\n")
        current_room = self.pokoje[0]

        while True:
            print(current_room.description)

            if current_room == self.pokoje[3]:
                break

            if current_room.hasQuest():
                print(f"Zagadka: {current_room.quest.question}")
                answer = input("Twoja odpowiedź: ").strip().lower()
                if current_room.solve_puzzle(answer):
                    print("Zagadkę rozwiązano!")
                    current_room.quest = None  # Usuwamy zagadkę po rozwiązaniu
                else:
                    print("Niepoprawna odpowiedź. Musisz rozwiązać zagadkę, aby przejść dalej.")
                    continue  # Gracz musi ponownie spróbować rozwiązać zagadkę

            command = input("Co chcesz zrobić? ").strip().lower()

            if command in ["north", "south", "east", "west"]:

                next_room = current_room.getRelation(command)

                if next_room:
                    current_room = next_room
                else:
                    print("Nie możesz tam pójść.")
            elif command == "save":
                self.saveGameplay("savegame")
            elif command == "load":
                self = self.loadGameplay("savegame")
            elif command == "quit":
                break
            else:
                print("Nieznana komenda.")

    def saveGameplay(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print("Gra została zapisana.")

    @staticmethod
    def loadGameplay(filename):
        with open(filename, 'rb') as file:
            game = pickle.load(file)
        print("Gra została wczytana.")
        return game