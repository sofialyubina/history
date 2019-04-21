from data_base import Global_Events
from data_base import Sentenses_with_keys
from nltk.tokenize import sent_tokenize
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("russian")
filename = "/home/sofialyubina/PycharmProjects/history/ai_tutor_database.tsv"
filename2 = "/home/sofialyubina/PycharmProjects/history/history_stemmed.txt"
filename3 = "/home/sofialyubina/PycharmProjects/history/history.txt"
events_ = {}

def process_data(data):
    data = data.lower()
    data += " "
    words = data.split(" ")

    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])

    data = " ".join(words)
    return data


with open(filename, "r") as infile:
    header = infile.readline()
    header_column = header.strip().split("\t")
    column_to_index = dict(zip(header_column, range(len(header_column))))
    for line in infile:
        elements = line.strip().split("\t")
        id_ = elements[0]
        event = Global_Events(id_,
                       elements[column_to_index["year"]],
                       elements[column_to_index["month"]],
                       elements[column_to_index["day"]],
                       elements[column_to_index["level"]],
                       elements[column_to_index["event"]],
                       process_data(elements[column_to_index["event"]])
                              )
        events_[id_] = event

with open(filename2, "r") as infile:
    sents = [line.strip() for line in infile.readlines()]

def get_words(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    new_text = text.split(" ")

    return new_text

with open(filename3, "r") as infile:
    sents_original = [line.strip() for line in infile.readlines()]


def matching(true_answer, user_answer):
    user_words = set(user_answer.strip().split(" "))
    true_words = set(true_answer.strip().split(" "))
    if len(user_words) <= 3:
        return len(true_words.intersection(user_words)) == len(user_words)
    else:
        return len(true_words.intersection(user_words)) == 4


sent_with_keys = []
keys = ["причина", "следствие", "итог", "привело"]
for m in range(len(keys)):
    keys[m] = process_data(keys[m])
d = 10
proverka = False
print(len(sents))
print(len(sents_original))

matched_events, matched_condition_events = [], []

for sen in range(len(sents)):
    print("Process sent:", sen)
    for x in events_:
        if matching(sents[sen], events_[x].stemmed_event):
            element = Sentenses_with_keys(
                sen,
                x, " "
            )

            matched_events.append(x)


            for s in sents[(element.sent_number-d):(element.sent_number+d)]:
                for n in range(len(keys)):
                    if matching(s, keys[n]):
                        element.text = element.text + s
                        matched_condition_events.append(x)

            sent_with_keys.append(element)

print(len(set(matched_events)))
print(len(set(matched_condition_events)))

with open("/home/sofialyubina/PycharmProjects/history/sentenses.txt", "w") as outfile:
    for sent_with_key in sent_with_keys:
        print(events_[sent_with_key.event_id].event + "\t" + sents_original[sent_with_key.sent_number] + "\t" + sent_with_key.text, file=outfile)