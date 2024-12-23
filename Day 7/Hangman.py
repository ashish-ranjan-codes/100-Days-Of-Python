# Let's build Hangman Game

import random
words = ["camel", "game", "sky", "america", "india"]
word = random.choice(words)
str = ''

#placing blank initially
for i in range(len(word)):
    str += '_'

#main program
lives = 5
print("*** Welcome to Hangman Game ***\n\n")
print("Choose a letter to complete your guess. If it matched hidden word, boyah!")
print(str)
print()

choosen_word = []
for i in range(len(word)):
    choosen_word.append('_')


while lives>0 and str != word:
    found = False
    char = input("\nGuess a letter: ").lower()
    
    for i in range(len(word)):
        if word[i] == char:
            choosen_word[i] = char
            found = True

    if found == False:
        lives -= 1
        print("\nWrong! You lost 1 life.")
        print(f"Life left = {lives}/5")
    else:
        str = ''
        for i in range(len(word)):
            str += choosen_word[i]
        print(str)

if lives>0:
    print("\nCongratulations! You won")
else:
    print("\nYou Lost the game!")

