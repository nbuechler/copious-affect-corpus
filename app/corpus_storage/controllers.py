from flask import jsonify
import json
import requests
import ast

from datetime import datetime

from bson.json_util import loads, dumps

def default():
    print 'Here'
    return 'Thanks controller, hello corpus_storage!'
'''
********************************************************************************

This is a way to keep all the corpus database stuff in one file. I might this refactor later.

======
This section is for databases
======

********************************************************************************
'''

from app import app
from flask.ext.pymongo import PyMongo

app.config['MONGOCORPUSRAW_DBNAME'] = 'affect-corpus'
mongo_corpus = PyMongo(app, config_prefix='MONGOCORPUSRAW')

app.config['MONGOCORPUSSTORAGE_DBNAME'] = 'affect-synopsis'
mongo_corpus_storage = PyMongo(app, config_prefix='MONGOCORPUSSTORAGE')


'''
The aim of corpus_storage python files are to store a list of synonyms for each order of the word.

{
  "word": <added by what word> # i.e. trust
  "utc": <utc date>
  "order-1": <list of all words (syn/ant of verb/noun) for this word>
  "order-2": <list of all words (syn/ant of verb/noun) for this word>
  "order-3": <list of all words (syn/ant of verb/noun) for this word>
}

There are three orders, where the next order is the same operation on each word in the previous order
and where order-1 is uses the word. This makes it easily referencable for Natural Language Processing (NLP).

This object is stored in a collection, and is gernerated from the information stored in affect-corpus database.

'''

'''
_for_collection_with_order
'''

emotionml_inspired_affects = ['acceptance', 'admiration', 'affection', 'amusement', 'anger', 'anticipation', 'anxiety', 'appreciation', 'arousal', 'arrogance', 'awe', 'blame', 'boredom', 'calmness', 'compassion', 'compromise', 'concern', 'confidence', 'confusion', 'contempt', 'contentment', 'curiosity', 'denial', 'depression', 'desire', 'despair', 'disappointment', 'disgust', 'dissonance', 'distress', 'dread', 'ecstasy', 'edginess', 'embarrassment', 'enjoyment', 'enthusiasm', 'envy', 'eroticism', 'excitement', 'exuberance', 'fear', 'grace', 'gratification', 'gratitude', 'grief', 'happiness', 'harmony', 'hate', 'hope', 'humility', 'indifference', 'interest', 'irritation', 'jealousy', 'joy', 'love', 'lunacy', 'lust', 'mania', 'melancholy', 'pain', 'panic', 'patience', 'perturbation', 'pity', 'pleasure', 'pride', 'rage', 'relief', 'remorse', 'reproach', 'resentment', 'resignation', 'sadness', 'satisfaction', 'shame', 'shock', 'stress', 'surprise', 'triumph', 'trust', 'wonder', 'worry']
all_affects = ['abandonment', 'abhorrence', 'abomination', 'absorption', 'abstinence', 'acceptance', 'admiration', 'adoration', 'affection', 'affectionateness', 'affliction', 'aggravation', 'aggressiveness', 'agony', 'alarm', 'alienation', 'aliveness', 'aloofness', 'alteration', 'amazement', 'ambiance', 'amusement', 'anger', 'angst', 'anguish', 'animation', 'anticipation', 'antipathy', 'anxiety', 'apathy', 'appraisal', 'appreciation', 'arousal', 'arrogance', 'assimilation', 'astonishment', 'attraction', 'audaciousness', 'aversion', 'avoidance', 'awareness', 'awe', 'awfulness', 'awkwardness', 'badness', 'bashfulness', 'belief', 'bewilderment', 'bitterness', 'blame', 'blessedness', 'boldness', 'boredom', 'bravery', 'brightness', 'calmness', 'capableness', 'cautiousness', 'certainty', 'chastity', 'cheerfulness', 'cleverness', 'closeness', 'cloudiness', 'coercion', 'coldness', 'compassion', 'composure', 'compromise', 'compulsion', 'concern', 'confidence', 'conformity', 'confusion', 'consciousness', 'consideration', 'consonance', 'contempt', 'content', 'contentment', 'contrariness', 'courage', 'courageousness', 'covetousness', 'criticalness', 'crossness', 'curiosity', 'darkness', 'decency', 'defeat', 'defiance', 'delight', 'denial', 'depression', 'desire', 'desolation', 'despair', 'despicableness', 'determination', 'devastation', 'devotion', 'diffidence', 'diligence', 'dimension', 'disappointment', 'disbelief', 'disdain', 'disgrace', 'disgust', 'disillusionment', 'dislike', 'dismay', 'disorientation', 'disrespect', 'dissonance', 'distance', 'distress', 'distrust', 'disturbance', 'dominance', 'doubt', 'doubtfulness', 'dread', 'dullness', 'eagerness', 'earnestness', 'easiness', 'ecstasy', 'edginess', 'ego', 'elation', 'embarrassment', 'empathy', 'emptiness', 'encouragement', 'endurance', 'engagement', 'engrossment', 'enjoyment', 'enlightenment', 'enragement', 'enthusiasm', 'envy', 'eroticism', 'euphoria', 'exasperation', 'excitation', 'excitement', 'exhaustion', 'exploitation', 'exuberance', 'familiarity', 'fascination', 'fate', 'fatigue', 'fear', 'festivity', 'flatness', 'fondness', 'foolishness', 'forgiveness', 'fortune', 'freedom', 'fright', 'friskiness', 'frustration', 'fulfillment', 'furiousness', 'fury', 'gallantry', 'gayness', 'glee', 'gloominess', 'gluttony', 'goodness', 'grace', 'gratification', 'gratitude', 'greatness', 'greed', 'grief', 'guilt', 'happiness', 'hardiness', 'harmony', 'hate', 'helplessness', 'hesitance', 'hesitancy', 'honor', 'hope', 'hopefulness', 'horror', 'hostility', 'hotness', 'humbleness', 'humiliation', 'humility', 'hurt', 'ignorance', 'importance', 'impulse', 'impulsiveness', 'inadequacy', 'inadequateness', 'incapableness', 'indifference', 'inducement', 'indulgence', 'infatuation', 'infection', 'inferiority', 'inflammation', 'infuriation', 'innocence', 'inquisitiveness', 'insecurity', 'insignificance', 'inspiration', 'insult', 'intensity', 'intentness', 'interest', 'intimacy', 'intrigue', 'invulnerability', 'irritation', 'isolation', 'jealousy', 'joy', 'jubilance', 'keenness', 'kindness', 'liberality', 'liberation', 'lifelessness', 'liveliness', 'lividness', 'loathing', 'loneliness', 'loss', 'lousiness', 'love', 'luck', 'luckiness', 'lunacy', 'lust', 'mania', 'melancholy', 'merriness', 'misery', 'modesty', 'motivation', 'mournfulness', 'negation', 'negativeness', 'neglect', 'nervousness', 'neutrality', 'nonchalance', 'nostalgia', 'numbness', 'obsession', 'offensiveness', 'openness', 'optimism', 'outrage', 'pain', 'panic', 'paralysis', 'passion', 'passionateness', 'patience', 'peacefulness', 'permanence', 'perplexity', 'persuasion', 'perturbation', 'pessimism', 'petrification', 'pity', 'playfulness', 'pleasantness', 'pleasure', 'positiveness', 'potency', 'power', 'powerfulness', 'powerlessness', 'preoccupation', 'pride', 'provocation', 'quietness', 'quirkiness', 'rage', 'reassurance', 'rebellion', 'rebelliousness', 'reception', 'receptiveness', 'reenforcement', 'regret', 'reinforcement', 'rejection', 'relaxation', 'reliability', 'relief', 'reluctance', 'remorse', 'reproach', 'resentment', 'reservation', 'resignation', 'resistance', 'respect', 'restlessness', 'revulsion', 'ridicule', 'sadness', 'safety', 'saltiness', 'sarcasm', 'satisfaction', 'scorn', 'sensitivity', 'serenity', 'seriousness', 'shakiness', 'shame', 'shock', 'shyness', 'skepticism', 'sloth', 'snoopiness', 'sobriety', 'sourness', 'spirit', 'spiritedness', 'spite', 'stolidity', 'straightness', 'strength', 'stress', 'stubbornness', 'stupidity', 'submission', 'subversion', 'sulkiness', 'sulky', 'sullenness', 'sunniness', 'sureness', 'surprise', 'suspicion', 'sweetness', 'sympathy', 'tearfulness', 'tenaciousness', 'tenacity', 'tenderness', 'tenseness', 'terribleness', 'terror', 'thoughtfulness', 'threat', 'thrill', 'tolerance', 'tragedy', 'triumph', 'trust', 'uncertainty', 'understanding', 'uneasiness', 'unhappiness', 'unification', 'uniqueness', 'unity', 'unpleasantness', 'unpredictability', 'uselessness', 'valence', 'validation', 'vanity', 'veneration', 'vengefulness', 'victimization', 'vigor', 'vileness', 'vulnerability', 'warmness', 'weariness', 'withdrawal', 'withdrawnness', 'woe', 'woefulness', 'wonder', 'wonderfulness', 'worry', 'worthlessness', 'wrath']


def get_mongo_corpus(collection, order):
    return dumps(mongo_corpus.db[collection + '-corpus-only-syn-unq-order-' + order].find())

def get_flat_lists(collection, order, for_web):
    flat_lists = []
    for doc in mongo_corpus.db[collection + '-corpus-only-syn-unq-order-' + order].find():
        flat_lists += (doc['flat_list'])
    if for_web:
        return dumps(set(flat_lists))
    else:
        return list(set(flat_lists))

'''
_for_collection
'''
def get_storage_object(collection, for_web):
    # TODO: Make so it can take more than the 3
    storage_object = {
                      "word": collection,
                      "utc": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
                      "order-1": get_flat_lists(collection, '1', False),
                      "order-2": get_flat_lists(collection, '2', False),
                      "order-3": get_flat_lists(collection, '3', False),
                     }
    if for_web:
        return dumps(storage_object)
    else:
        return storage_object

def save_storage_object(collection):
    result = get_storage_object(collection, False)
    mcs = mongo_corpus_storage.db['lingustic-affects'].find({'word': collection})
    if len(ast.literal_eval(dumps(mcs))) > 0:
        mongo_corpus_storage.db['lingustic-affects'].remove({'word': collection})
    mongo_corpus_storage.db['lingustic-affects'].insert_one(result)
    return "Saved!"

'''
_for_all_collections
'''
def save_all_storage_objects():
    #TODO: Error handling, like what happens if this fails!?
    print ('Total Affects: ' + str(len(all_affects)))
    for affect in all_affects:
        save_storage_object(affect)
    return "Saved All Affects!"
