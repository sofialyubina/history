from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize
stemmer = SnowballStemmer("russian")


filename2 = "/home/sofialyubina/tools/word2vec/bin/very_big_book.processed"


def process_data(data):
    data = data.lower()
    data += " "
    words = data.split(" ")
    for i in range(len(words)):
        words[i] = stemmer.stem(words[i])
    return data

lines =[]
with open(filename2, "r") as infile:
    for line in infile:
        words = line.split(" ")
        for i in range(len(words)):
            words[i] = stemmer.stem(words[i])
        line = " ".join(words)
        lines.append(line)


with open("/home/sofialyubina/tools/word2vec/bin/very_big_book.stemmed", "w") as outfile:
    for sent_with_key in lines:
        print(sent_with_key, file=outfile)
