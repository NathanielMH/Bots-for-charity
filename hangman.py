from typing import Dict, List


def update_word(secret_word: str, progress: str, c):
    new_progress = progress
    for i in range(len(secret_word)):
        if secret_word[i] == c:
            new_progress = new_progress[:i] + c + progress[i + 1:]
    return new_progress


class Hangman:
    def __init__(self, word: str) -> None:
        self._secret_word: str = word
        self._misses: int = 0
        self._progress: str = "_" * len(self._secret_word)
        self._letters_used: Dict[str, int] = {}
        self._hangman = "H A N G M A N "

    def play(self, c) -> str:
        if len(c) != 1:
            return "This is not a letter. Please try again with a single character!"
        if c in self._letters_used:
            return "You have already used this letter!"
        else:
            self._letters_used[c] = 1
            if c in self._secret_word:
                self._progress = update_word(self._secret_word, self._progress, c)
                return "Correct! This letter is inside the word. " + "\n" + self.end()
            else:
                self._misses += 1
                return "That letter is not inside the word!" + "\n" + self._hangman[
                                                                      :2 * self._misses] + "\n" + self.end()

    def end(self):
        if self._misses == 7:
            return "Game over! The word you were looking for is " + self._secret_word + ". Better luck next time!"
        elif self._progress == self._secret_word:
            return "Victory! You uncovered the secret word. Congratulations!"
        else:
            return "Keep going! " + self._progress

    def game_over(self) -> bool:
        return self._misses == 7 or self._progress == self._secret_word

# Create a set of words from which you choose one randomly at each game.
