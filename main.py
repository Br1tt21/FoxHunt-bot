import os
from math import sin, cos, sqrt, atan2, radians, pi, degrees
from dotenv import load_dotenv

import telebot
from telebot import types

# Bot V 2.4

# Token aquired over Telegram, see API for more info
BotToken  = os.getenv('TELEGRAM_BOT_TOKEN')

class question:
    def __init__(self, key, question, answers, correctAnswer, textHint, photoHint, long, lat):
        self.key = key

        self.question = question
        self.answers = answers
        self.correctAnswer = correctAnswer

        self.textHint = textHint
        self.photoHint = photoHint

        self.long = long
        self.lat = lat
    # 0 unanswered; 1 correct; 2 incorrect
    correct = 0

class quiz:
    sadFaces = []

    questions = []

    questions.append(question(
        # punt 1
        # Key
        "forecast",
        # Question
        "What is the name of this activity?",
        # Answers
        ["Foxhunt!",
        "Cathunt",
        "Doghunt"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "0",
        # Text hint
        "",
        # Photo hint
        "pictures/point1.jpg",
        # GPS hint
        # Long
        51.390488,
        # Lat
        5.554589
    ))

    questions.append(question(
        # punt 10
        # Key
        "neighbour",
        # Question
        "What role did Volundr have in Norse mythology? He/it was :",
        # Answers
        ["A blacksmith who crafted wings",
        "King Ragnar Lothbrok's hammer", 
        "A self-proclaimed holy man"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "0",
        # Text hint
        "",
        # Photo hint
        "pictures/point10.jpg",
        # GPS hint
        # Long
        51.389648,
        # Lat
        5.551176
    ))

    questions.append(question(
        # punt 4
        # Key
        "pledge",
        # Question
        "What is the total capacitance when two capacitors with a capacitance of 100uF are placed in parallel?",
        # Answers
        ["50uF",
        "100uF",
        "200uF",
        "400uF"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "2",
        # Text hint
        "",
        # Photo hint
        "pictures/point4.jpg",
        # GPS hint
        # Long
        51.388279,
        # Lat
        5.552619
    ))

    questions.append(question(
        # punt 14
        # Key
        "drawing",
        # Question
        "Which of the following units of measurement is NOT real?",
        # Answers
        ["Tesla",
        "Siemens",
        "Philips",
        "Pascal"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "2",
        # Text hint
        "",
        # Photo hint
        "pictures/point14.jpg",
        # GPS hint
        # Long
        51.387615,
        # Lat
        5.550548
    ))

    questions.append(question(
        # punt 16
        # Key
        "attitude",
        # Question
        "What frequency does the 5G network use?",
        # Answers
        ["4.9-5.1GHz",
        "24-47 GHz",
        "2-3GHz",
        "5GHz"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "1",
        # Text hint
        "",
        # Photo hint
        "pictures/point16.jpg",
        # GPS hint
        # Long
        51.386436,
        # Lat
        5.550095
    ))

    questions.append(question(
        # punt 19
        # Key
        "judgement",
        # Question
        "What does IEEE stand for?",
        # Answers
        ["Institute of Electrical and Electronics Engineers",
        "International Electrical Engineering Expo",
        "Institute of Electrical and Electronics Expo",
        "Institute of Electrical and Electronical Engineering"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "0",
        # Text hint
        "",
        # Photo hint
        "pictures/point19.jpg",
        # GPS hint
        # Long
        51.385052,
        # Lat
        5.548051
    ))

    questions.append(question(
        # punt 20
        # Key
        "mother",
        # Question
        "Which electrical engineer and entrepreneur cofounded Apple Inc alongside Steve Jobs?",
        # Answers
        ["Bill Gates",
        "Larry Page",
        "Elon Musk",
        "Steve Wozniak"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "3",
        # Text hint
        "",
        # Photo hint
        "pictures/point20.jpg",
        # GPS hint
        # Long
        51.384529,
        # Lat
        5.550787
    ))

    questions.append(question(
        # punt 22
        # Key
        "forestry",
        # Question
        "In the Marvel comics and movies, what is the name of the material that Thor's hammer is made of?",
        # Answers
        ["Vibranium",
        "Adamantium",
        "Promethium",
        "Uru"],
        # Correct Answer
        # a = 0     b = 1   c = 2   d = 3
        "3",
        # Text hint
        "This is the final location! Search for fire and you will find the treasure!",
        # Photo hint
        "pictures/point22.jpg",
        # GPS hint
        # Long
        51.382748,
        # Lat
        5.549260
    ))

    # questions.append(question(
    #     # punt 2
    #     # Key
    #     "pottery",
    #     # Question
    #     "What role did Volundr have in Norse mythology? He/it was :",
    #     # Answers
    #     ["A blacksmith who crafted wings",
    #     "King Ragnar Lothbrok's hammer", 
    #     "A self-proclaimed holy man"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "0",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point2.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 3
    #     # Key
    #     "minimize",
    #     # Question
    #     "Which of the following units of measurement is NOT real?",
    #     # Answers
    #     ["Tesla",
    #     "Siemens",
    #     "Philips",
    #     "Watt"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "2",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point3.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 5
    #     # Key
    #     "leadership",
    #     # Question
    #     "What frequency does the 5G network use?",
    #     # Answers
    #     ["4.9-5.1GHz",
    #     "24-47 GHz",
    #     "2-3GHz",
    #     "5GHz"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point5.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 6
    #     # Key
    #     "temptation",
    #     # Question
    #     "What does IEEE stand for?",
    #     # Answers
    #     ["Institute of Electrical and Electronics Engineers",
    #     "International Electrical Engineering Expo",
    #     "Institute of Electrical and Electronics Expo",
    #     "Institute of Electrical and Electronical Engineering"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "0",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point6.jpg",
    #     # GPS hint
    #     # Long
    #     51.388668,
    #     # Lat
    #     5.550944
    # ))

    # questions.append(question(
    #     # punt 7
    #     # Key
    #     "detective",
    #     # Question
    #     "Which electrical engineer and entrepreneur co-founded Apple Inc. alongside Steve Jobs?",
    #     # Answers
    #     ["Bill Gates",
    #     "Larry Page",
    #     "Elon Musk",
    #     "Steve Wozniak"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "3",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point7.jpg",
    #     # GPS hint
    #     # Long
    #     51.389198,
    #     # Lat
    #     5.550808
    # ))

    # questions.append(question(
    #     # TODO: beetje matie vraag
    #     # punt 8
    #     # Key
    #     "genuine",
    #     # Question
    #     "In electrical engineering, what does the term \"ground\" typically refer to?",
    #     # Answers
    #     ["The connection to the Earth in an electrical circuit",
    #     "A type of insulating material",
    #     "The highest potential point in a circuit",
    #     "A safety mechanism to prevent electric shock"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "0",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point8.jpg",
    #     # GPS hint
    #     # Long
    #     51.389198,
    #     # Lat
    #     5.550808
    # ))

    # questions.append(question(
    #     # punt 9
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point9.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 11
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point11.jpg",
    #     # GPS hint
    #     # Long
    #     51.388161,
    #     # Lat
    #     5.551170
    # ))

    # questions.append(question(
    #     # punt 12
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point12.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 13
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point13.jpg",
    #     # GPS hint
    #     # Long
    #     0,
    #     # Lat
    #     0
    # ))

    # questions.append(question(
    #     # punt 15
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point15.jpg",
    #     # GPS hint
    #     # Long
    #     51.387184,
    #     # Lat
    #     5.550110
    # ))

    # questions.append(question(
    #     # punt 17
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point17.jpg",
    #     # GPS hint
    #     # Long
    #     51.386188,
    #     # Lat
    #     5.548547
    # ))

    # questions.append(question(
    #     # punt 18
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point18.jpg",
    #     # GPS hint
    #     # Long
    #     51.385658,
    #     # Lat
    #     5.549006
    # ))

    # questions.append(question(
    #     # punt 21
    #     # Key
    #     "genuine",
    #     # Question
    #     "vraag",
    #     # Answers
    #     ["1",
    #     "2",
    #     "3",
    #     "4"],
    #     # Correct Answer
    #     # a = 0     b = 1   c = 2   d = 3
    #     "1",
    #     # Text hint
    #     "",
    #     # Photo hint
    #     "pictures/point21.jpg",
    #     # GPS hint
    #     # Long
    #     51.383633,
    #     # Lat
    #     5.550105
    # ))

    @classmethod
    def nrQuestions(cls):
        return len(cls.questions)

    @classmethod
    def correctQuestions(cls):
        numberCorrect = 0
        for i in range(quiz.nrQuestions()):
            if cls.questions[i].correct == 1:
                numberCorrect = numberCorrect + 1
        return numberCorrect

    @classmethod
    def answeredQuestions(cls):
        numberAnswered = 0
        for i in range(quiz.nrQuestions()):
            if cls.questions[i].correct > 0:
                numberAnswered = numberAnswered + 1
        return numberAnswered

    @classmethod
    # Finding the index of the item in the list to pass it into question array
    def getQuestionIndex(cls, submittedKey):
        index = None
        for i in range(cls.nrQuestions()):
            if(cls.questions[i].key == submittedKey.lower()):
                index = i
                break
        return index

quiz = quiz()

# Create instance of telebot - using Markdown for passing tekst format
VolundrBot = telebot.TeleBot(BotToken, parse_mode="MarkdownV2")

welcomeMessage = "*Welcome to the FoxHunt Quiz by Volundr* \U0001F98A \U0001F44B \n\
If you have found a key \U0001F511, submit it for a question using /key _key_\. \
You can then answer this question using /answer _key_ _answer_\. \
Sometimes we do care about you\U00002757 We _might_ give you a hint after a correct answer\. \
Check your _stats_\U0001F4C8 with the /stats command\. \n\n\
There is a total of *" + str(quiz.nrQuestions()) + "* questions but get you started, we will provide you the first key\: *" + quiz.questions[0].key + "*\n\n\
Good Luck \U0001F340\, may the best team win \.\.\.\."

# Command w/o args
# See how to use the bot when typing /help
@VolundrBot.message_handler(commands=['help','start'])
def startMessage(message):
    VolundrBot.send_chat_action(message.chat.id, 'typing')
    VolundrBot.reply_to(message, welcomeMessage)
    foxPhoto = open('./pictures/FoxHunt.jpeg', 'rb')
    VolundrBot.send_photo(message.chat.id, foxPhoto)

    uFirstName, uLastName, uID = str(message.from_user.first_name), str(message.from_user.last_name), str(message.from_user.id)
    print("Action by " + uFirstName + " " + uLastName + " ID " + uID + ": Started the Quiz \n")

# Command with args
# So that you can get the question that belongs to a key. Usage /key <key>
@VolundrBot.message_handler(commands=['key'])
def submitKey(message):
    subKey = "NOKEY"
    VolundrBot.send_chat_action(message.chat.id, 'typing')
    args = message.text.split(' ')[1:]
    if len(args) == 1:
        subKey = args[0]
        questionNr = quiz.getQuestionIndex(subKey)
        if(questionNr != None) and (quiz.questions[questionNr].correct == 0):
            sendQuestion(questionNr, message)
            debug = None
        elif(questionNr == None):
            response = "Sorry\, " + subKey + " is not a valid \U0001F511\.\.\."
            debug = "invalid key"
            VolundrBot.send_message(message.chat.id, response)
        else:
            response = "Sorry\, you have already answered \U0001F511 " + subKey + " \.\.\."
            debug = "already answered"
            VolundrBot.send_message(message.chat.id, response)

    elif len(args) < 1:
        response = "Invallid call\! Was expecting *more* args \U0001F972"
        debug = "invalid call, too little args"
        VolundrBot.send_message(message.chat.id, response)
    else:
        response = "Invallid call\! Was expecting *less* args \U0001FAE3"
        debug = "invalid key, too many args"
        VolundrBot.send_message(message.chat.id, response)

    if debug != None:
        uFirstName, uLastName, uID = str(message.from_user.first_name), str(message.from_user.last_name), str(message.from_user.id)
        print("Action by " + uFirstName + " " + uLastName + " ID " + uID + ": Submitted key " + str(subKey) + " and yielded " + debug)
        print("STATS :: Total Questions: " + str(quiz.nrQuestions()) + " - Answered questions: " + str(quiz.answeredQuestions()) + " - Correct Questions: " + str(quiz.correctQuestions()) + "\n")


def sendQuestion(questionNr, message):
    response = "Valid \U0001F511 submitted\n *Question\:* " + quiz.questions[questionNr].question
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(quiz.questions[questionNr].answers)):
        button = types.InlineKeyboardButton(quiz.questions[questionNr].answers[i], callback_data = str(i))
        keyboard.add(button)

    VolundrBot.arbitrary_callback_data = questionNr
    VolundrBot.send_message(message.chat.id, text=response, reply_markup=keyboard)

@VolundrBot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    questionNr = VolundrBot.arbitrary_callback_data
    VolundrBot.answer_callback_query(callback_query_id=call.id, text='Answer submitted!')

    if call.data == str(quiz.questions[questionNr].correctAnswer):
        response = "This was the correct answer"
        quiz.questions[questionNr].correct = 1
        VolundrBot.send_message(call.message.chat.id, response)
        VolundrBot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    else:
        response = "This answer was incorrect"
        quiz.questions[questionNr].correct = 2
        VolundrBot.send_message(call.message.chat.id, response)
        VolundrBot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    if quiz.answeredQuestions() == quiz.nrQuestions():
        finalizeQuizClient(call.message.chat.id)
    elif quiz.questions[questionNr].textHint != "" or quiz.questions[questionNr].textHint != "" or quiz.questions[questionNr].long != 0 or quiz.questions[questionNr].lat != 0:
            giveHint(call.message.chat.id, questionNr)

    uFirstName, uLastName, uID = str(call.from_user.first_name), str(call.from_user.last_name), str(call.from_user.id)
    print("Action by " + uFirstName + " " + uLastName + " ID " + uID + ": Answered Question " + str(questionNr) + " and yielded " + str(quiz.questions[questionNr].correct) + " points added")

    print("NEW STATS :: Total Questions: " + str(quiz.nrQuestions()) + " - Answered Questions: " + str(quiz.answeredQuestions()) + " - Correct Questions: " + str(quiz.correctQuestions()) + "\n")

# Command w/o args
# See the stats of the player
@VolundrBot.message_handler(commands=['stats'])
def sendStats(message):
	VolundrBot.send_message(message.chat.id,
    "\U00002192*STATS* \U0001F4C8  \nCorretly answered questions\: "
	+ str(quiz.correctQuestions()) + " \/ *" + str(quiz.nrQuestions()) + "*\n  " + progressBar())

# Command that's useful for developing the bot
# Resets the correctness parameter of all the questions to 0 so I don't have to reboot the bot everytime I test it.
@VolundrBot.message_handler(commands=['reset'])
def resetCorrectness(message):
	for i in range(quiz.nrQuestions()):
		quiz.questions[i].correct = 0
	response = "Bot has been reset, nrQuestions\: " + str(quiz.nrQuestions()) + " \nHave fun\!"
	VolundrBot.reply_to(message, response)

# Make the progress bar with emoji's
def progressBar():
	progress = []
	for i in range(quiz.nrQuestions()):
        # Not answered
		if quiz.questions[i].correct == 0:
			progress.append("\U00002B1C")
        # Correct
		elif quiz.questions[i].correct == 1:
			progress.append("\U0001F7E9")
        # Incorrect
		elif quiz.questions[i].correct == 2:
			progress.append("\U0001F7E5")
	return ''.join(progress)

def giveHint(chatID, questionNr):
    response = "We're also giving you a *hint*\: \n\n"
    if quiz.questions[questionNr].textHint != "":
        response = response + quiz.questions[questionNr].textHint

    VolundrBot.send_message(chatID, response)

    if quiz.questions[questionNr].photoHint != "":
        hintPhoto = open(quiz.questions[questionNr].photoHint, 'rb')
        VolundrBot.send_photo(chatID, hintPhoto)

    if quiz.questions[questionNr].long != 0 or quiz.questions[questionNr].lat != 0:
        try:
            print(f"INFO: Calculating distance and direction for question {questionNr}")

            distance, angle = get_direction_and_distance((quiz.questions[questionNr].long, quiz.questions[questionNr].lat), (quiz.questions[questionNr + 1].long, quiz.questions[questionNr + 1].lat))

            VolundrBot.send_message(chatID, f"The next point is {distance} meter away at a {angle} degree angle".replace(".", "\\."))
        except Exception as error:
            print(f"ERROR: {error}")
            VolundrBot.send_location(chatID, quiz.questions[questionNr].lat, quiz.questions[questionNr].long)

# Calculate the direction and distance between start and end point, hulde aan ChatGPT
def get_direction_and_distance(start, end):
    # Convert coordinates from degrees to radians
    start_lat, start_lon = map(radians, start)
    end_lat, end_lon = map(radians, end)

    # Radius of the Earth in kilometers
    radius = 6371.0

    # Calculate differences in longitude and latitude
    delta_lon = end_lon - start_lon
    delta_lat = end_lat - start_lat

    # Haversine formula
    a = sin(delta_lat / 2) ** 2 + cos(start_lat) * cos(end_lat) * sin(delta_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance between the points
    distance = radius * c

    # Calculate the bearing
    y = sin(delta_lon) * cos(end_lat)
    x = cos(start_lat) * sin(end_lat) - sin(start_lat) * cos(end_lat) * cos(delta_lon)
    bearing = atan2(y, x)

    # Convert the bearing to degrees
    bearing = (bearing + 2 * 3.14159) % (2 * 3.14159)
    bearing = degrees(bearing)

    return round(distance * 1000), round(bearing)

def finalizeQuizClient(chatID):
    VolundrBot.send_message(chatID, "*You've completed the FoxHunt*\U0001F38A\U0001F38A\U0001F38A \n\n Final stats: \n" + progressBar())
    foxPhoto = open('./pictures/WinningFox.jpeg', 'rb')
    VolundrBot.send_photo(chatID, foxPhoto)

# Restart entire bot and go over
VolundrBot.infinity_polling()
