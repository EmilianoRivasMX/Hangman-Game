# Importing basic libraries
import random
import os

def run():
    DB = ["C", "PYTHON", "JAVASCRIPT", "JAVA", "PHP"]

    HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # Selecting a random word to play
    word = random.choice(DB)

    # Setting the word spaces
    spaces = ["_"] * len(word)

    attemps = 6

    while True:
        os.system("clear")

        # Print the word spaces 
        for character in spaces:
            print(character, end=" ")

        #Print the hangman pics and upper the user letters
        print(HANGMAN_PICS[attemps])
        letter = input("Escribe una letra \n").upper()

        found = False
        
        # Search for the letter and substitude in the correct space
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True
        
        if not found:
            attemps -= 1

        # Won Game
        if "_" not in spaces:
            os.system("clear")
            print("\n Ganaste, Felicidades !")
            break
            input()
                
        # Failed Game
        if attemps == 0:
            os.system("clear")
            print("\n Perdiste UnU")
            break
            input()



if __name__ == "__main__":
    run()