def get_words(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    new_text = text.split(" ")

    return new_text
