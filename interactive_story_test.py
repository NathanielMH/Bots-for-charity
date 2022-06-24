from interactive_story import Interactive_story

S = Interactive_story("Once upon a time there was a lonely wolf, wandering the forest looking for friends. He then "
                      "saw a sheep walking by. He then decided to L: Scare the sheep so she would respect him, "
                      "R: Say something nice about her hat")

S.augment_story("The sheep, who is not one to be scared easily, calmly ignored the wolf. He then L: Ran after her, "
                "R: abandoned the idea and started crying", "The sheep greeted the "
                                                            "wolf, accepted the "
                                                            "compliment, "
                                                            "and they started to talk")

S.left.augment_story(
    "The wolf was too lonely to let a potential friend go. He begged the sheep to listen, and she did.",
    "The sheep saw despair in the wolf's eyes and decided to walk up to him.")

print(S.story, S.left.story, S.left.left.story, sep="\n", end=" THE END")
print()
print(S.story, S.left.story, S.left.right.story, sep="\n", end=" THE END")
print()