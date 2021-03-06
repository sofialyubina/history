from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize
stemmer = SnowballStemmer("russian")
import re

filename2 = "/home/sofialyubina/books/main_book.processed"


def process_data(data):
    # data = data.lower()
    # data += " "
    words = data.split(" ")

    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])

    data = " ".join(words)
    # data = re.sub("ё", "е", data)
    # data = re.sub("[^а-я0-9a-z ]", " ", data)
    return data


with open(filename2, "r") as infile:
    sents = []
    for line in infile:
        sents.append(line.strip())

original_sents = []
for x in range(len(sents)):
    original_sents.append(sents[x])
    sents[x] = process_data(sents[x])


with open("/home/sofialyubina/books/main_book.stemmed", "w") as outfile:
    for sent_with_key in sents:
        print(sent_with_key, file=outfile)

