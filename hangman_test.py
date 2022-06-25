from hangman import Hangman
import random

words = ['sauce', 'avocado', 'robot', 'house', 'family', 'happy', 'honor', 'dog', 'water', 'patience', 'glass', 'red']
words += ['beard', 'green', 'blue', 'full', 'field', 'santa', 'soccer', 'dance', 'dress', 'hangman', 'shoulder']
words += ['nose', 'hose', 'mouse', 'cat', 'highlight', 'chicken', 'rice', 'pasta', 'chocolate', 'milk', 'ice', 'card']
words += ['set', 'hose', 'pool', 'ball', 'cannon', 'bed', 'table', 'bottle', 'burger', 'tea', 'coffee', 'pudding']
words += ['engineer', 'psychology', 'plane', 'helicopter', 'garden', 'train', 'bus', 'phone', 'television', 'radio']
words += ['python', 'bot', 'tomato', 'soup', 'car', 'race', 'laser', 'microphone', 'sneakers', 'movement', 'money']
words += ['pace', 'maze', 'blaze', 'mouse', 'cube', 'circle', 'mountain', 'computer', 'cockpit', 'key', 'can', 'trash']

l = len(words) - 1
w = random.randint(0, l)
word = words[w]
H = Hangman(word)
while not H.game_over():
    s = input("Input a letter: ")
    print(H.play(s))
