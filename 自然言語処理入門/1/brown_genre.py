import nltk
from nltk.corpus import brown

genre_word = [
    (genre,word)
    for genre in ['news','romance']
    for word in brown.words(categories=genre)
]

cdf = nltk.ConditionalFreqDist(genre_word)
print cdf['romance']['could']
