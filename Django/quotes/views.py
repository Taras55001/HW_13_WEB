from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Author, Post, Tag
from users.models import Quote as UserPost, Author as UserAuthor
from .forms import GenerateQuoteForm

from bson import ObjectId
import openai
import random
import time
import subprocess

def main(request, page=1):
    per_page = 10

    user_quotes = UserPost.objects.all()
    other_quotes = Post.objects.all()

    quotes = list(user_quotes) + list(other_quotes)
    quotes.sort(key=lambda q: q.id)

    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def quotes_by_tag(request, tag_name):
    user_quotes = UserPost.objects.filter(tags__name=tag_name)
    other_quotes = Post.objects.filter(tags__name=tag_name)

    quotes = list(user_quotes) + list(other_quotes)
    quotes.sort(key=lambda q: q.id)

    return render(request, 'quotes/index.html', {'quotes': quotes})


def author_detail_view(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        author = UserAuthor.objects.get(id=author_id)
    return render(request, 'authors/author_detail.html', {'author': author})


def generate_quote(author_name):
    prompt = f"Generate a quote by {author_name}: "
    #time.sleep(34) # Якщо використовуємо безкоштовну підписку
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=200
        )
    quote = response['choices'][0]['text'].strip()

    return quote


def generate_quote_view(request):
    if request.method == 'POST':
        form = GenerateQuoteForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            quote_text = generate_quote(author.fullname)
            quote = Post.objects.create(author=author, quote=quote_text)

            num_tags = random.randint(1, 5)
            all_tags = Tag.objects.all()
            random_tags = random.sample(list(all_tags), num_tags)

            for tag in random_tags:
                quote.tags.add(tag)
            return render(request, 'quotes/quote.html', {'quote': quote})
    else:
        form = GenerateQuoteForm()
    return render(request, 'quotes/generate_quote.html', {'form': form})


def feel_site(request):
    import quotes.scrap as scrap
    scrap.feel()
    return render(request, 'quotes/feel_site.html')


def show_quote_view(request, quote):

    return render(request, 'quotes/quote.html', {'quote': quote})
