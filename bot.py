from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from hangman import Hangman
import random
from arithmetic_game import operators, levels
from interactive_story_test import titles_list, titles_to_story

b_size = [2, 3, 3, 4, 5]


def random_word() -> str:
    words = ['sauce', 'avocado', 'robot', 'house', 'family', 'happy', 'honor', 'dog', 'water', 'patience', 'glass',
             'red', 'beard', 'green', 'blue', 'full', 'field', 'santa', 'soccer', 'dance', 'dress', 'hangman',
             'shoulder', 'nose', 'hose', 'mouse', 'cat', 'highlight', 'chicken', 'rice', 'pasta', 'chocolate', 'milk',
             'ice',
             'card', 'set', 'hose', 'pool', 'ball', 'cannon', 'bed', 'table', 'bottle', 'burger', 'tea', 'coffee',
             'pudding', 'engineer', 'psychology', 'plane', 'helicopter', 'garden', 'train', 'bus', 'phone',
             'television',
             'radio', 'python', 'bot', 'tomato', 'soup', 'car', 'race', 'laser', 'microphone', 'sneakers', 'movement',
             'money', 'pace', 'maze', 'blaze', 'mouse', 'cube', 'circle', 'mountain', 'computer', 'cockpit', 'key',
             'can',
             'trash', 'neuron', 'heist', 'home', 'hijack', 'sumo', 'sum', 'crumble', 'cookie', 'chalk', 'board', 'boa',
             'tiger', 'elephant', 'dog', 'hog', 'rider', 'tent', 'lake', 'world', 'video', 'picture', 'heist', 'mind'
                                                                                                               'color',
             'fright', 'fry', 'deep', 'money', 'constant', 'trolley', 'trousers', 'shirt', 'bin', 'keyboard']
    w = random.randint(0, len(words) - 1)
    return words[w]


def start(update, context) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello! I am your telegram bot. Let's play! 😃")
    # Hangman
    context.user_data['hangman'] = None
    # Math
    context.user_data['math_streak'] = 0
    context.user_data['math'] = None
    context.user_data['level'] = None
    # Story
    context.user_data['story'] = None
    # Battleship
    context.user_data['grid'] = None
    context.user_data['grid_id'] = None
    context.user_data['id'] = None
    context.user_data['lives'] = None
    context.user_data['e_grid'] = None
    context.user_data['e_grid_id'] = None
    context.user_data['e_id'] = None
    context.user_data['e_lives'] = None


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Here are my commands: \n \n To play Hangman, first type the /hangman command to "
                                  "start "
                                  "the game. \n Then, to guess a letter type the /hangman command and type the letter "
                                  "afterwards. \n \n To play the math game, first type /math with your level (1-3). \n "
                                  "Then type /math to receive a question, and after you receive it type /answer "
                                  "followed by your answer. \n \n To play the interactive story game, first type "
                                  "/story "
                                  "to see the stories available. Then type /story followed by the title of the story "
                                  "you would like to experience. To make a decision, type /story followed by either "
                                  "L or R depending on what you want to do. \n \n Have fun!")


def result(op1: int, op: str, op2: int):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    else:
        return op1 // op2


def start_battleship(update, context):
    context.user_data['grid'] = [["🌊" for i in range(10)] for i in range(10)]
    context.user_data['grid_id'] = [[-1 for i in range(10)] for i in range(10)]
    context.user_data['id'] = 0
    context.user_data['lives'] = [2, 3, 3, 4, 5]
    context.user_data['e_grid'] = [["🌊" for i in range(10)] for i in range(10)]
    context.user_data['e_grid_id'] = [[-1 for i in range(10)] for i in range(10)]
    context.user_data['e_id'] = 0
    context.user_data['e_lives'] = [2, 3, 3, 4, 5]


def battleship(update, context):
    try:
        start_battleship(update, context)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def new_boat(update, context):
    boat_size = [2, 3, 3, 4, 5]
    boat_num = context.user_data['id']
    k = boat_size[boat_num]
    orientation = context.args[0]
    x = int(context.args[1])
    y = int(context.args[2])
    try:
        if orientation not in ['H', 'V']:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error orientation")
        elif x + k > 10 and orientation == "V":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error size")
        elif y + k > 10 and orientation == "H":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error size")
        else:
            if orientation == 'HOR':
                for j in range(k):
                    if context.user_data['grid'][x][y + j] == "🛥️":
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Error occupied")
                    context.user_data['grid'][x][y + j] = "🛥️"
                    context.user_data['grid_id'][x][y + j] = context.user_data['id']
                    context.user_data['e_grid'][x + j][y] = "🛥️"
                    context.user_data['e_grid_id'][x + j][y] = context.user_data['e_id']

            else:
                for j in range(k):
                    if context.user_data['grid'][x + j][y] == "🛥️":
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Error occupied")
                    context.user_data['grid'][x + j][y] = "🛥️"
                    context.user_data['grid_id'][x + j][y] = context.user_data['id']
                    context.user_data['e_grid'][x][y + j] = "🛥️"
                    context.user_data['e_grid_id'][x][y + j] = context.user_data['e_id']
        context.user_data['id'] += 1
        context.user_data['e_id'] += 1
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Check that you "
                                                                        "are not adding an extra boat nad restart the "
                                                                        "bot.")


def move(y, x, context, update) -> str:
    try:
        if x > 9 or y > 9:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Error! Wrong position")
        elif context.user_data['grid'][x][y] == "🛥️":
            context.user_data['grid'][x][y] = "💥"
            context.user_data['lives'][context.user_data['grid_id'][x][y]] -= 1
            if context.user_data['lives'][context.user_data['grid_id'][x][y]] == 0:
                return "SUNK"
            else:
                return "HIT"
        else:
            return "MISS"
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def move_enemy(x, y, context, update):
    if context.user_data['e_grid'][x][y] == "🛥️":
        context.user_data['e_grid'][x][y] = "💥"
        context.user_data['e_lives'][context.user_data['e_grid_id'][x][y]] -= 1
        if context.user_data['e_lives'][context.user_data['e_grid_id'][x][y]] == 0:
            return "SUNK"
        else:
            return "HIT"
    else:
        return "MISS"


def get_attacked(update, context):
    try:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Enemy attacks " + str(x) + str(y))
        m = "HIT"
        while m == "HIT" or m == "SUNK":
            m = move_enemy(x, y, context, update)
            if context.user_data['e_lives'] == [0, 0, 0, 0, 0]:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="You lose!")
                return "L"
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Enemy" + m)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def attack(update, context):
    try:
        x = int(context.args[0])
        y = int(context.args[1])
        if get_attacked(update, context) == "L":
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="You lost!")
        m = "HIT"
        while m == "HIT" or m == "SUNK":
            m = move(x, y, context, update)
            if context.user_data['lives'] == [0, 0, 0, 0, 0]:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="You win!")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=m)

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def play(update, context, h: Hangman):
    try:
        c = context.args[0]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=h.play(c))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def hangman(update, context):
    try:
        if context.user_data['hangman'] is None or context.user_data['hangman'].game_over():
            context.bot.send_message(chat_id=update.effective_chat.id, text="Starting new game...")
            context.user_data['hangman'] = Hangman(random_word())
        else:
            play(update, context, context.user_data['hangman'])
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def answer(update, context):
    try:
        n = int(context.args[0])
        if context.user_data['math'] is None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Please ask for a math question before answering :)")
        else:
            ans = int(context.user_data['math'])
            context.user_data['math'] = None
            if n == ans:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Correct! Keep going.")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Wrong! The answer was " + str(ans) + ". Keep practicing!")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def math(update, context):
    try:
        if context.user_data['level'] is None:
            level = int(context.args[0])
            context.user_data['level'] = level
        else:
            level = context.user_data['level']
        op1 = random.randint(0, levels[level])
        op2 = random.randint(0, levels[level])
        op_num = random.randint(0, 3)
        op = operators[op_num]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=str(op1) + " " + str(op) + " " + str(op2))
        context.user_data['math'] = result(op1, op, op2)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def story_titles(update, context):
    try:
        text = "These are the stories I have: \n"
        for title in titles_list:
            text += "- " + title + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


def story(update, context):
    try:
        if context.user_data['story'] is None:
            if len(context.args) == 0:
                story_titles(update, context)
            else:
                title = ""
                for i in range(len(context.args)):
                    title += context.args[i] + " "
                if title in titles_to_story.keys():
                    context.user_data['story'] = titles_to_story[title]
                    context.bot.send_message(chat_id=update.effective_chat.id, text=context.user_data['story'].story)
                else:
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Please select a valid title for "
                                                                                    "a story!")
        else:
            decision = context.args[0]
            if decision == 'L':
                context.user_data['story'] = context.user_data['story'].left
                if context.user_data['story'] is not None:
                    context.bot.send_message(chat_id=update.effective_chat.id, text=context.user_data['story'].story)
                if context.user_data['story'].left is None:
                    context.user_data['story'] = None
            elif decision == 'R':
                context.user_data['story'] = context.user_data['story'].right
                if context.user_data['story'] is not None:
                    context.bot.send_message(chat_id=update.effective_chat.id, text=context.user_data['story'].story)
                if context.user_data['story'].left is None:
                    context.user_data['story'] = None
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Please select a valid decision!")

    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops. Something went wrong. Please restart "
                                                                        "the bot!")


# declares a constant with the access token retrieved from token.txt
TOKEN = open('token.txt').read().strip()

# creates objects to work with Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indicates that when the bot recieves the command /start, the start function is executed
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('hangman', hangman))
dispatcher.add_handler(CommandHandler('math', math))
dispatcher.add_handler(CommandHandler('answer', answer))
dispatcher.add_handler(CommandHandler('story', story))
dispatcher.add_handler(CommandHandler('battleship', battleship))

# starts the bot
updater.start_polling()
updater.idle()
