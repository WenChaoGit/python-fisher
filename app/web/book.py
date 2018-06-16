"""
created by 朝文天下 on 

"""
from app.forms.book import SearchForm
from app.spider.book_model import YuShuBook
from flask import jsonify, request

from app.libs.helper import is_isbn_or_key
from . import web

__author__ = '朝文天下'


@web.route('/book/search')
def search():
    # Request Response
    form = SearchForm(request.args)
    # 验证失败
    if not form.validate():
        return jsonify(form.errors)
    # 验证成功
    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    result = YuShuBook.search_by_isbn(q) if isbn_or_key == 'isbn' else YuShuBook.search_by_keyword(q, page)
    # if isbn_or_key == 'isbn':
    #     result = YuShuBook.search_by_isbn(q)
    # else:
    #     result = YuShuBook.search_by_keyword(q, page)
    return jsonify(result)
