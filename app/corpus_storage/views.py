from flask import Blueprint
from flask import render_template, redirect, url_for, jsonify

import controllers

corpus_storage = Blueprint('corpus_storage', __name__)

@corpus_storage.route('/')
def default():
    return 'Hello corpus_storage!'

@corpus_storage.route('/alt/')
def controller_default():
    return controllers.default()

@corpus_storage.route('/raw_corpus_collection/<collection>')
def get_raw_corpus_collection(collection):
    return 'Remember to specifiy an order to get back data for collection: ' + collection

'''
_for_collection_with_order
'''
@corpus_storage.route('/raw_corpus_collection/<collection>/<order>/')
def get_raw_corpus(collection, order):
    return controllers.get_mongo_corpus(collection, order)

@corpus_storage.route('/raw_corpus_collection/<collection>/<order>/flat_list')
def get_flat_lists(collection, order):
    for_web = True
    return controllers.get_flat_lists(collection, order, for_web)

'''
_for_collection
'''
@corpus_storage.route('/complete_object/<collection>/')
def get_complete_object(collection):
    for_web = True
    return controllers.get_storage_object(collection, for_web)

@corpus_storage.route('/save_complete_object/<collection>/')
def save_complete_object(collection):
    return controllers.save_storage_object(collection)

'''
_for_all_collections
'''
@corpus_storage.route('/save_complete_object/all/')
def save_all_complete_object():
    return controllers.save_all_storage_objects()
