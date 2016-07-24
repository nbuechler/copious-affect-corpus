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
