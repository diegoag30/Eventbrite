import game

# Unittesting, que utiliza increase me y decrease me hasta que se adivina el numero del usuario.
currentGame = game.Game(0, 100)
userNumber = 66
while userNumber != currentGame.mean():
    currentGameNumber = currentGame.mean()
    if currentGameNumber > userNumber:
        currentGame.decreaseMe()
    elif currentGameNumber < userNumber:
        currentGame.increaseMe()
print(currentGame.mean() == userNumber)
print ("User number is: " + str(currentGame.mean()))
