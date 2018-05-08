# Llamar funciones de clase Game
import game
welcome = "Welcome to the Guess Number Game!!!\n"
select_mode = "Type \"guess\" if you want to guess a number. Othewise, I will guess a number: "
start_number = 0
finish_number = 100

# Object assignment
guess_number_game = game.Game(start_number, finish_number)

print(welcome)
selection = raw_input(select_mode)
if selection == "guess":
    guess_number_game.guess()
else:
    guess_number_game.me()
