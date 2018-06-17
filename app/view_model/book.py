"""
created by 朝文天下 on 2018/6/17

"""
__author__ = '朝文天下'


class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.author = ', '.join(data['author'])
        self.publisher = data['publisher']
        self.price = data['price']
        self.pages = data['pages']
        self.summary = data['summary']
        self.image = data['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, total_data, keyword):
        self.total = total_data['total']
        self.keyword = keyword
        self.books = [BookViewModel() for book in total_data.books]


class _BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = 1
            result['books'] = [cls.__cut_data(data)]
        return result

    @classmethod
    def package_collection(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['books'] = [cls.__cut_data(data) in data]
            result['total'] = data['total']
        return result

    @classmethod
    def __cut_data(cls, data):
        result = {
            'title': data['title'],
            'author': data['author'],
            'publisher': data['publisher'],
            'price': data['price'],
            'pages': data['pages'],
            'summary': data['summary'],
            'image': data['image']
        }
        return result
