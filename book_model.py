from request import Http


class YuShuBook:
    url_isbn = 'http://t.yushu.im/v2/book/isbn/{}'
    url_keyword = 'http://t.yushu.im/v2/book/seach?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.url_isbn.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.url_keyword.format(keyword, count, start)
        result = Http.get(url)
        return result
