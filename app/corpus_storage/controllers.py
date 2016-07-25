from flask import jsonify
import json
import requests

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
    mongo_corpus_storage.db['lingustic-affects'].insert_one(result)
    return "Saved!"
