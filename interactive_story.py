# Option 0 is left, 1 is right. Make 8 scenarios per story : 3 decisions
class Interactive_story:
    def __init__(self, story: str):
        self.left = None
        self.right = None
        self.story = story

    def _augment_story_right(self, new_part: str) -> None:
        if self.right is None:
            self.right = Interactive_story(new_part)
        else:
            self.augment_story_right(self.right, new_part)

    def _augment_story_left(self, new_part: str) -> None:
        if self.left is None:
            self.left = Interactive_story(new_part)
        else:
            self.augment_story_left(self.left, new_part)

    def augment_story(self, opt1: str, opt2: str) -> None:
        self._augment_story_right(opt2)
        self._augment_story_left(opt1)
