from __future__ import division
import nltk,re,pprint

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return float(len(content)) / len(text)

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
    stem,suffix = re.findall(regexp,word)[0]
    return stem

def segment(text,segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == 1:
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

def evalute(text,segs):
    words = segment(text,segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size
