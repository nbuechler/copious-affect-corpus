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

@corpus_storage.route('/raw_corpus_collection/<collection>/<order>/')
def get_raw_corpus_collection_with_order(collection, order):
    return controllers.get_mongo_corpus_collection_with_order(collection, order)

@corpus_storage.route('/raw_corpus_collection/<collection>/<order>/flat_list')
def get_flat_lists_for_collection_with_order(collection, order):
    return controllers.get_flat_lists_for_collection_with_order(collection, order)
