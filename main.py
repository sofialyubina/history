from question import Question
from dates_and_events import Events
from answers import Answers
words = ["a", "b"]
events = []
years = []
string = ' '
filename = "/home/sofialyubina/PycharmProjects/history/dates.csv"
filename2 = "/home/sofialyubina/PycharmProjects/history/questions.csv"
filename3 = "/home/sofialyubina/PycharmProjects/history/answers.csv"
import random


def get_words(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    new_text = text.split(" ")

    return new_text


def get_event_by_year(year):
    for id_ in events_:
        e = events_[id_]
        if e.date == year:
            return e.event


def get_year_by_event(event):
    for id_ in events_:
        e = events_[id_]
        if e.event == event:
            return e.date


def matching(true_answer, user_answer):
    n = 2
    final_answer = False
    true_words = get_words(true_answer)
    user_words = get_words(user_answer)
    if n > len(true_words):
        n = len(true_words)
    if n > len(user_words):
        n = len(user_words)
    if n > 1:
        for i in range(len(true_words)-1):
            for j in range(len(user_words)-1):
                if (true_words[i] == user_words[j]) & (true_words[i+1] == user_words[j+1]):
                    final_answer = True
    else:
        if true_words[0] == user_words[0]:
            final_answer = True

    return final_answer


questions = {}
with open(filename2, "r") as infile:
    for line in infile:
        elements = line.strip().split("\t")
        id_ = elements[0]
        question = Question(id_,
                            elements[1],
                            elements[2],
                            elements[3])
        questions[id_] = question


def get_result(got_id):
    if got_id in questions:
        question_ = questions[got_id]
        event_ = events_[question_.event_id]
        answer_ = answers[question_.question_id]
    else:
        raise ValueError("No such ID in DATABASE")
    if question_.get_type() == "E":
        print(event_.event)
        print(answer_.answer)
        result = matching(event_.event, answer_.answer)
    else:
        print(answer_.answer)
        print(event_.date)
        if answer_.answer == event_.date:
            result = True
        else:
            result = False

    return result


events_ = {}
with open(filename, "r") as infile:
    for line in infile:
        elements = line.strip().split("\t")
        elements = elements[0].split(',')
        id_ = elements[0]
        event = Events(id_,
                       elements[1],
                       elements[2])
        events_[id_] = event


answers = {}
with open(filename3, "r") as infile:
    for line in infile:
        elements = line.strip().split("\t")
        id_ = elements[0]
        answer = Answers(id_,
                         elements[1],
                         elements[2])
        answers[id_] = answer

while (1):
    x = random.randint(1, 9)
    print(questions[x.__str__()].question)
    user_answer = input()
    if user_answer == "STOP":
        break
    else:
        answers[questions[x.__str__()].question_id].answer = user_answer
        print(get_result(x.__str__()))