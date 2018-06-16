from app.libs.request import Http
from flask import current_app


class YuShuBook:
    url_isbn = 'http://t.yushu.im/v2/book/isbn/{}'
    url_keyword = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.url_isbn.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        start = cls.calculate_start(page)
        url = cls.url_keyword.format(keyword, current_app.config['PER_PAGE'], start)
        result = Http.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']

