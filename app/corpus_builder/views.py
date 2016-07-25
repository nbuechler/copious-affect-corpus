from flask import Blueprint
from flask import render_template, redirect, url_for, jsonify, request
import requests
from datetime import datetime

import controllers

corpus_builder = Blueprint('corpus_builder', __name__)

@corpus_builder.route('/')
def default():
    return 'Hello corpus_builder!'

@corpus_builder.route('/alt/')
def controller_default():
    return controllers.default()

'''
********************************************************************************
********************************************************************************
'''

'''
Flask views below as an endpoint
'''

@corpus_builder.route('/log/')
def log_test():
    controllers.test_logging()
    return 'Success'

'''
A human can build a corpus manulally by passing a word list of unknown count
to the method:

unknown_count_word_view()

Make sure to pass three paramaters via a form -- (api_key for BHT, words list, and a collection name)
Then the human can use the flattened list of each of the lists created to generate the next level.
This should also be automated. :-)
'''

# This automated as <root>/y .... unknown_count_word_view_with_level() :-)
@corpus_builder.route('/x', methods=['GET', 'POST'])
def unknown_count_word_view():
    r = request.get_json()
    k = r.get('key')
    w = r.get('words')
    c = r.get('collection')
    return controllers.get_word_or_words(len(w), k, w, c)

@corpus_builder.route('/y', methods=['GET', 'POST'])
def unknown_count_word_view_with_level():
    r = request.get_json()
    k = r.get('key') # String
    w = r.get('words') # List of Strings
    c = r.get('collection') # String
    inc_syn = int(r.get('include_synonyms')) # String, really it is a string representation of a 0 or 1, 0 - don't include, 1 - include
    inc_ant = int(r.get('include_antonyms')) # String, really it is a string representation of a 0 or 1, 0 - don't include, 1 - include
    levels = int(r.get('levels')) # how many levels. 1 is just the inital array in addition to the flat_list(s) of the intital array
    return controllers.get_undetermined_levels(k, w, c, levels, levels, inc_syn, inc_ant)

@corpus_builder.route('/1', methods=['GET', 'POST'])
def one_word_view():
    r = request.get_json()
    k = r.get('key')
    w = r.get('words')
    c = r.get('collection')
    return controllers.get_word_or_words(1, k, w, c)

@corpus_builder.route('/10', methods=['GET', 'POST'])
def ten_words_view():
    r = request.get_json()
    k = r.get('key')
    w = r.get('words')
    c = r.get('collection')
    return controllers.get_word_or_words(10, k, w, c)

@corpus_builder.route('/100', methods=['GET', 'POST'])
def hundred_words_view(words=None):
    r = request.get_json()
    k = r.get('key')
    w = r.get('words')
    c = r.get('collection')
    return controllers.get_word_or_words(100, k, w, c)

@corpus_builder.route('/500', methods=['GET', 'POST'])
def five_hundred_words_view(words=None):
    r = request.get_json()
    k = r.get('key')
    w = r.get('words')
    c = r.get('collection')
    return controllers.get_word_or_words(500, k, w, c)
