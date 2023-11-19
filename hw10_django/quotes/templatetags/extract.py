from bson.objectid import ObjectId

from django import template

from ..utils import connect

register = template.Library()

def get_author(_id):
    db = connect()
    author = db.authors.find_one({'_id': ObjectId(_id)})
    return author['fullname']

register.filter('author', get_author)