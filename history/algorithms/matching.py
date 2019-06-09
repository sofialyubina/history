import re


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
