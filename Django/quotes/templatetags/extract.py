from django import template

from bson.objectid import ObjectId

from ..utils import get_mongodb
from utils.models import Autor

register = template.Library()


def get_author(id_):
    get_mongodb()
    author = Autor.objects(id=ObjectId(str(id_))).first()
    return author.fullname


register.filter('author', get_author)