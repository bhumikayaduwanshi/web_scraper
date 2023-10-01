import json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

# fetch contents from pages
def get_div_tags_from_page(no_of_pages=5):
    div_tags_with_links = []
    for i in range(1, no_of_pages+1):
        page = session.get(f"https://www.lawinsider.in/page/{i}")
        soup = BeautifulSoup(page.html.html, 'lxml')
        div_tags = soup.find_all('div', class_='read-title')
        div_tags_with_links.append(div_tags)
    return div_tags_with_links

# extract links from page contents
def get_links(div_tags):
    links = []
    for div_tags_with_links in div_tags:
        for div_tag in div_tags_with_links:
            link = div_tag.find('a').attrs['href']
            links.append(link)
    return links

# extract title and content from links in json format
def get_articles_from_links(links):
    articles = dict()
    for link in links:
        try:
            page = session.get(link)
            soup = BeautifulSoup(page.html.html, 'lxml')

            title = soup.find('h1', class_='entry-title').text
            article_content_tag = soup.find('div', class_='entry-content')

            p_tags = article_content_tag.find_all('p')

            content = ""
            for p_tag in p_tags:
                content += p_tag.text

            articles[title] = content

        except Exception as e:
            continue

    return articles

# Save title and contents in json file
def save_articles_in_json(articles):
    articles_json = json.dumps(articles, )
    with open('articles.json', 'w') as f:
        f.write(articles_json)


def main():
    print('Starting extraction...')

    div_tags_with_links = get_div_tags_from_page()
    links = get_links(div_tags_with_links)
    articles = get_articles_from_links(links)
    save_articles_in_json(articles)

    print('Extraction completed')

if __name__=='__main__':
    main()