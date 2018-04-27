from random import randint as rn

# Definir la clase


class Game():
    def __init__(self, minimum, maximum):
        self.minimum = int(minimum)
        self.maximum = int(maximum)

     # Busca la mitad entre dos numeros, lo cual acelerara el proceso de busqueda.
    def mean(self):
        mean_btw = (self.minimum+self.maximum)/2
        return mean_btw

     # Funcion me, adivina numero que esta pensando el usuario
    def me(self):
        median_number = self.mean()
        answer = raw_input("Your number is " + str(median_number) + " ? ")
        if answer == "+":
            self.minimum = median_number
            self.me()
        elif answer == "-":
            self.maximum = median_number
            self.me()
        elif answer == "=":
            print("Awesome! your number is " + str(median_number) + " !!")
        else:
            print("Sorry, that's not an answer, please answer using + , - or = ")
            self.me()
