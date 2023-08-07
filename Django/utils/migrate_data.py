import os
import django
import json
from datetime import datetime

# Встановити налаштування Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from django.core.management.base import BaseCommand
from quotes.models import Author, Post, Tag

autors_json = "../autors.json"
post_json = "../quotes.json"


def list_data(file_name):
    with open(file_name, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def create_autor(data):
    autor = Author(
        fullname=data['fullname'],
        born_date=datetime.strptime(data['born_date'], "%B %d, %Y"),
        born_location=data['born_location'],
        description=data['description']
    )
    autor.save()


def create_tag(data):
    tag_name = data['name']
    tag, _ = Tag.objects.get_or_create(name=tag_name)
    return tag


def create_post(data):
    text = data.get("quote")
    tags_list = [create_tag(tag_data) for tag_data in data.get("tags")]
    autor = Author.objects.get(fullname=data.get("author"))
    post = Post(quote=text, author=autor)
    post.save()
    post.tags.set(tags_list)


class Command(BaseCommand):
    help = 'Migrate data from MongoDB to SQLite'

    def handle(self, *args, **options):
        autors = list_data(autors_json)
        for autor in autors:
            create_autor(autor)

        posts = list_data(post_json)
        for post in posts:
            create_post(post)

        self.stdout.write(self.style.SUCCESS('Data migration completed successfully.'))
