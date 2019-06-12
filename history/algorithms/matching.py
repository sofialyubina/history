import re
import numpy as np


def load_vectors(path):
    vectors = {}

    with open(path, "r") as infile:
        infile.readline()

        for line in infile:
            elements = line.strip().split(" ")
            word = elements[0]
            vector = []
            for element in elements[1:]:
                vector.append(float(element))

            vectors[word] = np.array(vector)

    return vectors


def clean_text(text):
    text = text.strip().lower()
    text = re.sub("ё", "е", text)
    text = re.sub("[^а-я0-9a-z ]", " ", text)
    return " ".join(text.split())


def get_words(text, min_len=0):
    text = clean_text(text)
    words = text.split()
    words = [word for word in words if len(word) >= min_len]
    return words


def match_with_year(start_year, user_answer):
    start_year = str(start_year)
    for word in get_words(user_answer):
        if word == start_year:
            return True

    return False

def match_with_answer(true_answer, user_answer):
    true_words = get_words(true_answer, 2)
    user_words = get_words(user_answer, 2)

    # logic depends on number of words
    if len(user_words) == 0:
        return False

    if len(true_words) == 1:
        return true_words[0] in user_words

    # Process special case with one user word
    if len(user_words) == 1:
        if len(true_words) == 1:
            return user_words[0] == true_words[0]
        return False

    # check if all words from true_answer in user_answer
    if sum([word in user_words for word in true_words]) == len(true_words):
        return True

    # get all user bi-grams
    user_bigrams = ["_".join((user_words[i], user_words[i + 1])) for i in range(len(user_words) - 1)]
    true_bigrams = ["_".join((true_words[i], true_words[i + 1])) for i in range(len(true_words) - 1)]

    # if at least one bigram in common return True
    for user_bigram in user_bigrams:
        if user_bigram in true_bigrams:
            return True

    # in all other cases return False
    return False

def matching(true_answer, user_answer):
    n = 2

    final_answer = False

    true_words = get_words(true_answer)
    user_words = get_words(user_answer)

    if len(user_words) == 0:
        return False

    if n > len(user_words):
        n = len(user_words)

    if n > 1:
        for i in range(len(true_words) - 1):
            for j in range(len(user_words) - 1):
                if (true_words[i] == user_words[j]) and (true_words[i + 1] == user_words[j + 1]):
                    final_answer = True
    else:
        if true_words[0] == user_words[0]:
            final_answer = True

    return final_answer


def calc_vector_len(vector):
    return np.sqrt(np.sum(vector * vector))


def middle_vector(a, vectors):
    result = np.zeros(300)

    words = get_words(a)
    number = 0

    for n in range(len(words)):
        word = words[n]
        if word in vectors:
            result  = vectors[word] +  result
            number += 1

    if number > 0:
        result /= number

    return result


def calc_vectors_score(first, second, vectors):
    a = middle_vector(first, vectors)
    b = middle_vector(second, vectors)

    score = np.sum(a * b) / calc_vector_len(a) / calc_vector_len(b)
    return score
