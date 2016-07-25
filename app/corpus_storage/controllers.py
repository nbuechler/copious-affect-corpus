from flask import jsonify
import json
import requests

from datetime import datetime

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

app.config['MONGOCORPUSSTORAGE_DBNAME'] = 'affect-synopsis'
mongo_corpus_storage = PyMongo(app, config_prefix='MONGOCORPUSSTORAGE')

app.config['MONGOCORPUS_DBNAME'] = 'affect-corpus'
mongo_corpus = PyMongo(app, config_prefix='MONGOCORPUS')

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
