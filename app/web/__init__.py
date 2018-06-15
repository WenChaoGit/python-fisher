"""
created by 朝文天下 on 

"""
from flask import Blueprint

__author__ = '朝文天下'

web = Blueprint('web', __name__)

from app.web import book
from app.web import user
