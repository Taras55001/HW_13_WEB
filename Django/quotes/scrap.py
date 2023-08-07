from bs4 import BeautifulSoup
import requests
from datetime import datetime
from .models import Author, Post, Tag


def parse_author(response, **kwargs):
    content = response.select_one(".author-details")
    fullname = content.select_one('.author-title').get_text().strip()
    date_born = content.select_one('.author-born-date').get_text().strip()
    location_born = content.select_one('.author-born-location').get_text().strip()
    bio = content.select_one('.author-description').get_text().strip()

    born_date = datetime.strptime(date_born, "%B %d, %Y").strftime("%Y-%m-%d")
    name = 'Alexandre Dumas fils' if fullname == 'Alexandre Dumas-fils' else fullname
    author = Author.objects.get_or_create(
        fullname=name,
        defaults={
            'born_date': born_date,
            'born_location': location_born,
            'description': bio,
        }
    )
    return author



def feel():
    start_url = "http://quotes.toscrape.com/"
    response = requests.get(start_url)

    while True:
        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text().strip()
            tags = [tag.get_text().strip() for tag in quote.select(".tags a")]
            tags_list = []
            for item in tags:
                tag, created = Tag.objects.get_or_create(name=item)
                tags_list.append(tag)
            author_link = start_url + quote.select_one('span a')['href']
            author_response = requests.get(author_link)
            author_soup = BeautifulSoup(author_response.text, 'html.parser')
            author, created = parse_author(author_soup)

            post, created = Post.objects.get_or_create(
                quote=text,
                author=author,
            )
            if created:
                post.tags.set(tags_list)

        next_link = soup.select_one('li.next a')
        if next_link:
            response = requests.get(start_url + next_link['href'])
        else:
            break


if __name__ == "__main__":
    feel()
