points = 0


def get_words(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    new_text = text.split(" ")

    return new_text


def matching(true_answer, user_answer):
    points = 0
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
                    points = points + 50
    else:
        if true_words[0] == user_words[0]:
            final_answer = True
            points = 100

    if final_answer:
        return points
    else:
        return 0
