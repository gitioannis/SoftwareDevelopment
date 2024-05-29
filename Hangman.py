# import the random module to randomly generate a word from the list
import random
import time
import os

# List of words
words = ['variable', 'string', 'integer', 'selection', 'iteration', 'loop', 'operator']
#words = ['']

def main():
    os.system("cls")
    print ("==================")
    print ("WELCOME TO HANGMAN")
    print ("==================\n\n")
    print ("    Main Menu\n\n")
    print (" 1) Play Game")
    print (" 2) Add New Word")
    print (" 3) Exit\n\n")
    print ("==================\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        Add_word()
    elif Choice == "3":
        os._exit(0)
    else:
        input("Please Input Valid Option")
    main()

def Add_word():
    os.system("cls")
    print("Old word list: ", ", ".join(words))
    New_word = input('Input New word: ')
    if len(New_word) > 0:
        words.append(New_word)
    os.system("cls")
    print("New word list", ", ".join(words))
    input("Press ENTER to continue...")

def splash():
    os.system("cls")
    # introduction to the game
    delay = 3
    while delay:
        print ('  ===================')
        print ('  LET\'S PLAY HANGMAN')
        print ('  ', delay, "secs to start")
        print ('  ===================\n\n')
        print('''
        _______
        |/    |
        |     O
        |   \_|_/
        |     |
        |    / \\
        |   /   \\
    ____|____
    \n''')
        print ('  ===================')
        time.sleep(1)
        delay = delay - 1
        os.system("cls")

def game():
    #Randomly choose a word from the list
    global secret
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_'*len(secret)
    l = list(placed)
    done = 0

    while turns:

        while True:
            os.system("cls")
            hang(turns)
            print("\n\nSecret Word.....:",' '.join(l))
            print("\n\nLetters Used....:",guessed)
            print("\n\nTries to go.....: ",turns)
            typed = input("\n\nGuess a Letter..: ")
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) > 1:
                input("Single Upper Case Letters ONLY!. Press ENTER to continue...")
            else:
                break

        turns = 7
        if typed not in guessed:
            guessed = guessed + typed
        g = list(guessed)
        s = list(secret)

        for k in range(len(g)):
            kstr = guessed[k]
            if kstr in s:
                for i in range(len(s)):
                    if kstr == s[i]:
                        l[i] = kstr
            else:
                turns = turns - 1

        if l == s:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("CONGRATULATIONS! YOU GUESSED: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break

        if turns == 0:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("GAME OVER! SECRET WORD: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break

def hang(turn):
    if turn < 7:
        print('   _______   ')
        print('   |/    |   ')
    else:
        print('   _______   ')
        print('   |/        ')

    if turn < 6:
        print('   |     O   ')
    else:
        print('   |         ')

    if turn < 5:
        print('   |   \_|_/ ')
    else:
        print('   |         ')

    if turn < 4:
        print('   |     |   ')
    else:
        print('   |         ')

    if turn < 3:
        print('   |    / \\ ')
    else:
        print('   |         ')

    if turn < 2:
        print('   |   /   \\')
    else:
        print('   |         ')

    print(' __|____')

if __name__ == '__main__':
    main()


