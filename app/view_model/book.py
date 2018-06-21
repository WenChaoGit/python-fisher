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
        self.total = total_data.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in total_data.books]

