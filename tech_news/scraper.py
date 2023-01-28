# from parsel import Selector
import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        time.sleep(1)
        if response.status_code != 200:
            return None
        else:
            return response.text

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    posts_links = selector.css("div.cs-overlay a::attr(href)").getall()
    return posts_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    news_pages = selector.css("div.nav-links a.next::attr(href)").get()
    return news_pages


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.xpath('//link[@rel="canonical"]/@href').get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("ul.post-meta li::text").get()
    writer = selector.css("span.author a::text").get()

    comments_count = selector.css("div.post-comments h5::text").get()
    if comments_count is None:
        comments_count = 0

    summary = selector.xpath('//div[@class="entry-content"]/p[1]').get()
    summary = selector.xpath('string(//p[1])').getall()
    summary_formatted = " ".join(summary)

    tags = selector.xpath(
        '//section[@class="post-tags"]/ul/li/a/text()'
    ).getall()

    category = selector.css("span.label::text").get()
    dicio = {
        "url": url,
        "title": str(title).rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments_count),
        "summary": str(summary_formatted).strip(),
        "tags": tags,
        "category": str(category),
    }
    return dicio


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    url = "https://blog.betrybe.com/"
    page_news = fetch(url)
    list_of_news = scrape_updates(page_news)
    next_link = scrape_next_page_link(page_news)

    while len(list_of_news) < amount:
        next_fetch = fetch(next_link)
        next_link = scrape_next_page_link(next_fetch)
        list_of_news.extend(scrape_updates(next_fetch))

    for item in list_of_news[:amount]:
        next_fetch = fetch(item)
        tech_news.append(scrape_news(next_fetch))

    create_news(tech_news)

    return tech_news
