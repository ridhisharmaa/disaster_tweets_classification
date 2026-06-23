import re

from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(tag):

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    return wordnet.NOUN


def clean_text(text):

    text = text.lower()

    text = re.sub(
        r'http\S+|www\S+',
        ' URL ',
        text
    )

    text = re.sub(
        r'@(\w+)',
        r'\1',
        text
    )

    text = re.sub(
        r'#(\w+)',
        r'\1',
        text
    )

    text = re.sub(
        r'[^\w\s]',
        ' ',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    ).strip()

    return text


def lemmatize_text(text):

    words = text.split()

    tagged_words = pos_tag(words)

    lemmas = [
        lemmatizer.lemmatize(
            word,
            get_wordnet_pos(tag)
        )
        for word, tag in tagged_words
    ]

    return " ".join(lemmas)


def preprocess_text(text):

    text = clean_text(text)

    text = lemmatize_text(text)

    return text