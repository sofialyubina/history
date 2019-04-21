from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize
stemmer = SnowballStemmer("russian")


filename2 = "/home/sofialyubina/PycharmProjects/history/history_from_rurik.txt"


def process_data(data):
    data = data.lower()
    data += " "
    words = data.split(" ")

    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])

    data = " ".join(words)
    return data


with open(filename2, "r") as infile:
    data = " ".join(infile.read().split())
    sents = sent_tokenize(data)

original_sents = []
for x in range(len(sents)):
    original_sents.append(sents[x])
    sents[x] = process_data(sents[x])


with open("/home/sofialyubina/PycharmProjects/history/history_stemmed.txt", "w") as outfile:
    for sent_with_key in sents:
        print(sent_with_key, file=outfile)


with open("/home/sofialyubina/PycharmProjects/history/history.txt", "w") as outfile:
    for sent_with_key in original_sents:
        print(sent_with_key, file=outfile)