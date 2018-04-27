# Llamar funciones de clase Game
import game


diego = game.Game("0", "100")

diego.me()


def mean(num1, num2):
    mean_btw = (num1+num2)/2
    return mean_btw


"""def me(minimum, maximum):
    median_number = mean(minimum, maximum)
    simbolo = raw_input("Your number is " + str(median_number) + " ? ")
    if simbolo == "+":
        minimum = median_number-
        me(minimum, maximum)
    elif simbolo == "-":
        maximum = median_number
        me(minimum, maximum)
    elif simbolo == "=":
        print("Awesome! your number is " + str(median_number) + " !!")"""
