from random import randint

def AreYouLuckyPunk(whatWins):
    class choice:
        rps = ['rock','paper','scissors']
    
    number = randint(0,2)
    
    result = choice()
    
    thisResult = result.rps[number]
    if thisResult == whatWins:
        print(f"You picked {thisResult} and won!!")
    else:
        print(f"You picked {thisResult} and lost!!")

AreYouLuckyPunk('rock')