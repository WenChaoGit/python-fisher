"""
created by 朝文天下 on 

"""
from app.forms.book import SearchForm
from app.spider.book_model import YuShuBook
from flask import jsonify, request, render_template

from app.libs.helper import is_isbn_or_key
from app.view_model.book import BookCollection
from . import web
import json

__author__ = '朝文天下'


@web.route('/test')
def hello():
    return render_template('test.html', data={
        'name': '文朝',
        'age': 18
    })


@web.route('/book/search')
def search():
    # Request Response
    form = SearchForm(request.args)
    books = BookCollection()
    # 验证失败
    if not form.validate():
        return jsonify(form.errors)
    # 验证成功
    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(q) if isbn_or_key == 'isbn' else yushu_book.search_by_keyword(q, page)
    books.fill(yushu_book, q)
    result = json.dumps(books, default=lambda o: o.__dict__)
    return result
