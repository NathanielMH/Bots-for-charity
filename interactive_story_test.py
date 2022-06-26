from interactive_story import Interactive_story

S = Interactive_story("Once upon a time there was a lonely wolf, wandering the forest looking for friends. He then "
                      "saw a sheep walking by. He then decided to \n L: Scare the sheep so she would respect him \n "
                      "R: Say something nice about her hat")

S.augment_story("The sheep, who is not one to be scared easily, calmly ignored the wolf. He then \n L: Ran after her "
                "\n "
                "R: abandoned the idea and started crying", "The sheep greeted the "
                                                            "wolf, accepted the "
                                                            "compliment, "
                                                            "and they started to talk. The wolf then \n L: Took "
                                                            "advantage of that to scare her even more \n R: Took the "
                                                            "opportunity and became "
                                                            "friends with her")

S.left.augment_story(
    "The wolf was too lonely to let a potential friend go. He begged the sheep to listen, and she did. \n THE END.",
    "The sheep saw despair in the wolf's eyes and decided to walk up to him. \n THE END.")

S.right.augment_story("The sheep told the wolf that he would not get any friends by being scary, and wandered off. \n "
                      "THE END.",
                      "After a while, the sheep decided to invite the wolf to her house to play. It was the wolf's "
                      "first invitation and he was extremely happy. \n THE END.")

titles_list = ["The wolf and the sheep"]
titles_to_story = {"The wolf and the sheep ": S}
