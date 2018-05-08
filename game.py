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

     # increaseMe y decreaseMe se utilizan para aumentar y disminuir el numero que se intenta adivinar.
    def increaseMe(self):
        self.minimum = self.mean()

    def decreaseMe(self):
        self.maximum = self.mean()

     # Funcion me, adivina numero que esta pensando el usuario
    def me(self):
        median_number = self.mean()
        answer = raw_input("Your number is " + str(median_number) + " ? ")
        if answer == "+":
            median_number = self.increaseMe()
            self.me()
        elif answer == "-":
            median_number = self.decreaseMe()
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
