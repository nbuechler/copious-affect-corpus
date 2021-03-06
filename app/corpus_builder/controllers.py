from flask import jsonify
import json
import requests

from datetime import datetime

def default():
    print 'Here'
    return 'Thanks controller, hello corpus_builder!'

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

app.config['MONGOCORPUS_DBNAME'] = 'affect-corpus'
mongo_corpus = PyMongo(app, config_prefix='MONGOCORPUS')


'''
********************************************************************************
********************************************************************************
'''

'''
The aim of corpus_builder python files are to build a corpus of synonyms around a primary word.

i.e.
Affect (order-0)
  it has synonyms/antonyms (order-1)
     those synonyms/antonyms have synonyms/antonyms (order-2)... orders after 3 is likely where begin to stop caring so we don't make another order of requests.

But,
We do print the 4th order to the terminal. We could store this.


Moreover, the words will be stored as follows:

{
  "word": <added by what word>
  "response": <json response from bighugelabs>
  "utc": <utc date>
  "flat-list": <list of all words (syn/ant of verb/noun) for this word>
}

This gets stored in a mongo database. Collections are named after the inital parent.
In this case that parent is 'Affect'. To be clear, this is probably not the best way
to build a corpus, but it is a quick and effective way for getting started.
'''

import logging

logging.basicConfig(level=logging.INFO, filename="logfile", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

def test_logging():
    logging.info("hello")

def verify_bhl_api(api_key):
    r = requests.get('http://words.bighugelabs.com/api/2/' + api_key + '/affect/json')
    if(r.raise_for_status()):
        return 'error'
    else:
        return jsonify(r.json())

def get_single_word(api_key, word):
    r = requests.get('http://words.bighugelabs.com/api/2/' + api_key + '/' + word + '/json')
    # TODO: Figure out how to handle 500 error
    if(r.raise_for_status()):
        return 404
    else:
        return r.json()

def handle_next_level(raw_response, include_syn, include_ant):
    print '*************************************'
    print 'next-level'
    print '*************************************'
    va = []
    vs = []
    na = []
    ns = []
    if(raw_response.get('verb')):
        if(include_ant):
            va = raw_response.get('verb').get('ant') if raw_response.get('verb').get('ant') is not None else []
            # print va
        if(include_syn):
            vs = raw_response.get('verb').get('syn') if raw_response.get('verb').get('syn') is not None else []
            # print vs
    if(raw_response.get('noun')):
        if(include_ant):
            na = raw_response.get('noun').get('ant') if raw_response.get('noun').get('ant') is not None else []
            # print na
        if(include_syn):
            ns = raw_response.get('noun').get('syn') if raw_response.get('noun').get('syn') is not None else []
            # print ns
    print '*************************************'
    flat_list = va + vs + na + ns
    print '*-----------------------------------*'
    return flat_list

def save_word(word, raw_response, collection, inc_syn, inc_ant):
    # print word
    print '======' + word + '======'
    flat_list = handle_next_level(raw_response, inc_syn, inc_ant)
    result = {
              "word": word,
              "response": raw_response,
              "utc": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
              "flat_list": flat_list,
             }
    stored_result = mongo_corpus.db[collection].insert_one(result)
    # print raw_response
    print stored_result.inserted_id
    print raw_response
    print '------------------'
    return result


def get_word_or_words(word_length, api_key, words, collection, inc_syn, inc_ant):
    if api_key and words and len(words) == int(word_length):
        all_flat_lists = []
        # Level One
        for word in words:
            try:
                raw_response = get_single_word(api_key, word)
                if(raw_response != '404'): # Save things if there wasn't a 404 error
                    data = save_word(word, raw_response, collection, inc_syn, inc_ant)
                    print json.dumps(data.get('flat_list'))
                    all_flat_lists = all_flat_lists + data.get('flat_list')
            except:
                pass
        set_of_flat_lists = set(all_flat_lists)
        unique_flat_lists = list(set_of_flat_lists)
        print unique_flat_lists
        print len(unique_flat_lists)
        logging.info("=====NEW !!UNIQUE!! FLAT LIST=====")
        logging.info(unique_flat_lists)
        logging.info("=====END FLAT LIST=====")
        logging.info("Length of list is:")
        logging.info(len(all_flat_lists))
        logging.info("Length of setlist is:")
        logging.info(len(unique_flat_lists))
        logging.info("***************************")
        return unique_flat_lists # return just the unique words in the set, no duplicates!
    else:
        print 'MESSAGE: No valid input, sorry'
        return '' # Return an empty string becaus this gets used in the event of there not being a valid words list to gracefully fail

def get_two_levels(k, w, c):
    # get level one
    flat_list_one = get_word_or_words(len(w), k, w, c, 1, 1)
    print type(flat_list_one)
    # get level two
    get_word_or_words(len(flat_list_one), k, flat_list_one, (c + '-order-2'), 1, 1)

    return 'Success'

def generic_get_levels(k, w, c, list_number, inc_syn, inc_ant):
    logging.info("***************************")
    logging.info("List is in the following mongo collection:")
    logging.info(c + '-order-' + str(list_number))
    output_flat_list_set = get_word_or_words(len(w), k, w, (c + '-order-' + str(list_number)), inc_syn, inc_ant)
    return output_flat_list_set

def get_undetermined_levels(k, w, c, remaining_levels, total_levels, inc_syn, inc_ant):

    if remaining_levels == 1:
        word_list = generic_get_levels(k, w, c, (total_levels - remaining_levels + 1), inc_syn, inc_ant)
    else :
        word_list = generic_get_levels(k, w, c, (total_levels - remaining_levels + 1), inc_syn, inc_ant)
        get_undetermined_levels(k, word_list, c, (remaining_levels - 1), total_levels, inc_syn, inc_ant)

    return 'Success'
