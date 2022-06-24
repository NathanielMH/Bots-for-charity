from typing import Dict, List


def update_word(secret_word: str, progress: str, c: str):
    for i in range(len(secret_word)):
        if secret_word[i] == c:
            progress[i] = c
    return progress


class Hangman:
    def __init__(self, word: str) -> None:
        self._secret_word: str = word
        self._misses: int = 0
        self._progress: str = "_______"
        self._letters_used: Dict[str, int] = {}
        self._hangman = "HANGMAN"

    def play(self, c: str) -> str:
        if len(c) != 1:
            return "This is not a letter. Please try again with a single character!"
        if c in self._letters_used:
            return "You have already used this letter!"
        else:
            self._letters_used[c] = 1
            if c in self._secret_word:
                self._progress = update_word(self._secret_word, self._progress, c)
                return "Correct! This letter is inside the word. You are getting closer..." + self._progress
            else:
                self._misses += 1
                return "That letter is not inside the word! Keep trying..." + self._hangman[:self._misses]

    def end(self):
        if self._misses == 7:
            return "Game over! The word you were looking for is " + self._secret_word + ". Better luck next time!"
        if self._progress == self._secret_word:
            return "Victory! You uncovered the secret word. Congratulations!"
