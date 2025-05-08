
import random
 

class GameMenu:
    
    def __init__(self):
        self.overall_score = 0
        self.games = {
            '1': {'name': 'Guess Number Game', 'class': GuessNumberGame},
            '2': {'name': 'Rock Paper Scissors', 'class': RockPaperScissorGame},
            '3': {'name': 'Trivia  Quiz', 'class': TriviaQuiz},
            '4': {'name': 'Pokemon Card Binder Manager', 'class': PokemonBinderManager}
        }
        
    def display_menu(self):
        
        print("\n=== Game Menu ===")
        print("Select a game to play:")
        for key, game in self.games.items():
            print(f"{key}. {game['name']}")
        print("5. Check Overall Score")
        print("0. Exit")
        
    def run(self):
        
        while True:
            self.display_menu()
            choice=input(f'\n enter your choice(0-5):')
        
       
            if choice == '5':
              print(f"\nYour overall score: {self.overall_score}")
              input("Press Enter to continue...")
              continue
            elif choice == '0':
               print("\nThanks for playing!")
               break
            elif choice in self.games:
                self.play_game(choice)
            else:
             print("Invalid choice. Please try again.")
    
    def play_game(self, choice):
        
        game_info = self.games[choice]
        print(f"\nStarting {game_info['name']}...")

       
        # For other games, no additional arguments are needed
        
        if choice == '3':  # TriviaQuiz
          while True:
            print("\nSelect a category for the Trivia Quiz:")
            print("1. Object-Oriented Programming (OOP)")
            print("2. Procedural Programming (POP)")
            print("3. Exit to Main Menu")
            category_choice = input("Enter your choice (1/2/3): ").strip()

            if category_choice == '1':
                category_name = "Object-Oriented Programming"
                questions = oop_questions
                answers = oop_answers
                options = oop_options
            elif category_choice == '2':
                category_name = "Procedural Programming"
                questions = pop_questions
                answers = pop_answers
                options = pop_options
            elif category_choice == '3':
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                continue

            # Create an instance of TriviaQuiz with the selected category
            game_instance = game_info['class'](category_name, questions, answers, options)
            score = game_instance.play()
            self.overall_score += score
            print(f"Added {score} points to your overall score")

        elif choice=='4':
          game_instance=game_info['class']()
          game_instance.main_menu()
          
        else:
        # For other games, no additional arguments are needed
           game_instance = game_info['class']()
           score = game_instance.play()
           self.overall_score += score

        input("\nPress Enter to return to the menu...")



class GuessNumberGame():
    def __init__(self):
      self.answer=random.randint(1,30)
      self.attempts=7
      self.highest_score=30
    

    def play(self):
        for attempts in range(1,self.attempts+1):
            
            player=int(input('guess a number between 1 to 30: '))
            print(f'You have {self.attempts - attempts + 1} attempts remaining to guess the right answer.')
            if player <1 or player >30:
              print('invalid input, please enter the number from 1 to 30')
              continue
            player_score=self.highest_score-(attempts -1)
            if player<self.answer:
                print('guess is too low')
            elif player> self.answer:
               print('guess is too high')
            else:
              print(f'congrats, you guessed the correct number in {attempts} attempts')
              print(f'your score is {player_score}')
              return player_score

        print('\nGame over')
        print(f'You ran out of attempts. The correct guess was {self.answer}.')
        return 0


class RockPaperScissorGame:
    def __init__ (self):

        self.options=[' 0 for rock','1 for paper','2 for scissor']
        self.player_wins=0
        self.computer_wins=0
        self.rounds=3
    def play(self):
        for round_number in range(1,self.rounds+1):
            print(f'round{round_number}')
        #computer=random.randint(0,2)
        #print(f'computer chose:{computer}')
           
            player= int(input('Enter your choice(0 for rock,1 for paper or 2 for scissor):'))

            if player not in [0, 1, 2]:
               print("Invalid input. Please enter 0, 1, or 2.")
               continue

            computer=random.randint(0,2)
            print(f'computer chose: {computer}')

        
            if player==computer:
              print('it is a draw')
            elif computer==0 and player ==2:
              print('you lose')
              self.computer_wins +=1

            elif computer==2 and player==0:
              print('congrats, you won!!')
              self.player_wins +=1
            
            elif computer>player:
              print('you lose.')
              self.computer_wins +=1
            else:
              print('congrats,you won')
              self.player_wins +=1

            print(f'\nplayer score:{self.player_wins}')
            print(f'computer score:{self.computer_wins}')

        print('\ngame over')

        if self.player_wins > self.computer_wins:
           print('you won')
        elif self.player_wins < self.computer_wins:
          print('you lose')
        
        else:
          print('its a tie')

        return self.player_wins


from quiz_questions import oop_questions, oop_answers, oop_options, pop_questions, pop_answers, pop_options

class TriviaQuiz():
    def __init__(self, category_name,questions,answers,options):
        self.category= category_name
        self.questions = questions
        self.answers = answers
        self.options = options
        self.score = 0

    def play(self):
        print(f"\nStarting the {self.category} Quiz!")
        for i in range(len(self.questions)):
            print(f"\nQuestion {i + 1}: {self.questions[i]}")
            labels=['a','b','c','d']
            for j, option in enumerate(self.options[i]):
                print(f"{labels[j]}) {option}")  # Dynamically generate labels (a, b, c, d)

            # Get the player's answer
            player_answer = input("Enter your answer (a/b/c/d): ").lower()

            # Check if the answer is correct
            if player_answer == self.answers[i]:
                print("Correct answer!")
                self.score += 1
            else:
                print("Wrong answer!")
                correct_option = self.options[i][ord(self.answers[i]) - 97]
                print(f"The correct answer is: {self.answers[i]}) {correct_option}")

        print(f"\nYou scored {self.score}/{len(self.questions)} in the {self.category} Quiz.")

        return self.score

class PokemonBinderManager:
    def __init__(self):
    
        self.binder = []

    def add_card(self):
    
        card_name = input("Enter the Pokemon Card Name: ").strip()
        self.binder.append(card_name)
        print(f"{card_name} is added to the Binder.")

    def reset_binder(self):

        self.binder.clear()
        print(" reset is done.")

    def view_binder(self):
        if not self.binder:
            print("Binder is empty.")
        else:
            print("Current Pokemon cards in binder:")
            for index, card in enumerate(self.binder, 1):
                print(f"{index}. {card}")

    def main_menu(self):
    
        print("Welcome to Pokemon Card Binder manager")
        while True:
            print("\nMain Menu")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. exit")
            option = input("Enter Your option: ").strip()

            if option == "1":
                self.add_card()
            elif  option== "2":
                self.reset_binder()
            elif option == "3":
                self.view_binder()
            elif option == "4":
                print("thank you for playing pokemon card binder!")
                break
            else:
                print("Invalid option. Please select from 1-4.")
    

        



if __name__ == "__main__":
    menu = GameMenu()
    menu.run()
        
