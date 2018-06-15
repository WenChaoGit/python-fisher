"""
created by 朝文天下 on 

"""
from book_model import YuShuBook
from flask import jsonify, request

from helper import is_isbn_or_key
from . import web

__author__ = '朝文天下'


@web.route('/book/search')
def search():
    # Request Response
    q = request.args['q']
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
