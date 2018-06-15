"""
created by 朝文天下 on 

"""
__author__ = '朝文天下'


def is_isbn_or_key(word):
    """
    长度为10或者13,并且字符串由数字组成 isbn
    :param word:
    :return:
    """
    isbn_or_key = 'keyword'
    short_word = word.replace('-', '')
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
