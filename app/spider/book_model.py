from app.libs.request import Http
from flask import current_app


class YuShuBook:
    url_isbn = 'http://t.yushu.im/v2/book/isbn/{}'
    url_keyword = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.url_isbn.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        start = self.calculate_start(page)
        url = self.url_keyword.format(keyword, current_app.config['PER_PAGE'], start)
        result = Http.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
