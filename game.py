from random import randint as rn

# Definir la clase


class Game():
    def __init__(self, minimum, maximum):
        self.minimum = int(minimum)
        self.maximum = int(maximum)
        self.random_num = rn(int(minimum), int(maximum))

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

        # Creacion funcion guess
    def guess(self):
        cpu_number = self.random_num
        user_answer = raw_input(
            "Choose a number from " + str(self.minimum) + " to " + str(self.maximum) + ": ")
        user_answer = int(user_answer)
        if user_answer == cpu_number:
            print ("congrats, that's my number")
        elif user_answer > cpu_number:
            print ("smaller...")
            self.guess()
        elif user_answer < cpu_number:
            print("say one greater...")
            self.guess()
