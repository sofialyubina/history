from nltk.tokenize import sent_tokenize

from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("russian")

word = "красивая идти в горы"
print(stemmer.stem(word))

