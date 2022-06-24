# Option 0 is left, 1 is right.

class Interactive_story:
    def __init__(self, story: str):
        self._left = None
        self._right = None
        self._story = story

    def augment_story_right(self, new_part: str) -> None:
        if self._right is None:
            self._right = Interactive_story(new_part)
        else:
            self.augment_story_right(self._right, new_part)

    def augment_story_left(self, new_part: str) -> None:
        if self._left is None:
            self._left = Interactive_story(new_part)
        else:
            self.augment_story_left(self._left, new_part)
