import os
import json
import django
import sys
from datetime import datetime


sys.path.append(os.path.abspath('..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")

django.setup()

from quotes.models import Author, Tag, Post


def list_data(file_name):
    with open(file_name, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


autors_json = "autors.json"
post_json = "quotes.json"

def parse_date(date_str):
    return datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")

def create_author(data):
    born_date = parse_date(data['born_date'])
    author = Author.objects.get_or_create(
        fullname=data['fullname'],
        defaults={
            'born_date': born_date,
            'born_location': data['born_location'],
            'description': data['description'],
        }
    )
    return author

def create_tag(tag_name):
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    return tag


def create_post(data):
    text = data.get("quote")
    tags_list = [create_tag(tag_data) for tag_data in data.get("tags")]
    author = data['author']
    post = Post(quote=text, author=author)
    post.save()
    post.tags.set(tags_list)
    return post

def migrate_data():
    autors = list_data(autors_json)
    for autor in autors:
        create_author(autor)

    posts = list_data(post_json)
    for post in posts:
        create_post(post)


if __name__ == "__main__":
    migrate_data()
