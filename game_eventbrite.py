# Llamar funciones de clase Game
import game


diego = game.Game("0", "100")


print("Welcome to the Guess Number Game!!!\n")
selection = raw_input(
    "Type \"guess\" if you want to guess a number. Othewise, I will guess a number: ")
if selection == "guess":
    diego.guess()
else:
    diego.me()
