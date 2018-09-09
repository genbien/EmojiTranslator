import json
import fastText
import numpy as np
from stopwords import stopwords
from operator import itemgetter
from sklearn.metrics.pairwise import cosine_similarity


model = fastText.load_model('wiki.en.bin')


def vectorize_text(text):
    sent = []
    text_split = text.split(' ')
    for tok in text_split:
        vec = np.array(model.get_word_vector(tok))
        sent.append(vec)
    if sent:
        return np.average(sent, axis=0)
    return []


with open('moji.json', 'r') as f:
    mojis = json.load(f)

processed_mojis = {}

for moji in mojis:
    emoji_text = ' '.join(
        [
            moji['description'],
            moji['category'],
            ' '.join(moji['aliases']),
            ' '.join(moji['tags'])
        ]
    ).lower().replace('_', ' ')
    emoji_vec = vectorize_text(emoji_text).reshape(1, -1)
    processed_mojis[moji['emoji']] = {"text": emoji_text, "vector": emoji_vec}

input_text = ""

while input_text != "exit()":

    input_text = input("Text to be translated:\n>> ")
    if input_text == 'exit()':
        break

    translated = []
    text_split = input_text.split(' ')
    for tok in text_split:
        if tok.lower() not in stopwords:
            input_vec = model.get_word_vector(tok).reshape(1, -1)
            similarities = []
            for pm in processed_mojis:
                similarity = cosine_similarity(input_vec, processed_mojis[pm]["vector"])
                similarities.append((pm, similarity[0][0]))
            most_similar = max(similarities, key=itemgetter(1))
            if most_similar[1] > 0.0:
                translated.append(most_similar[0])

    print("TRANSLATED:", ' '.join(translated))
