"""
created by 朝文天下 on 

"""
from flask import Blueprint

__author__ = '朝文天下'

web = Blueprint('web', __name__)

from app.web import book
# from app.web import user
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web import auth
