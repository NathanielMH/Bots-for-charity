from hangman import Hangman

H = Hangman("sauce")
while not H.game_over():
    s = input("Input a letter: ")
    print(H.play(s))
