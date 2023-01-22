# from parsel import Selector
import requests
import time
from parsel import Selector


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
    url = selector.css("div.cs-overlay a::attr(href)").get()
    title = selector.css("h2.entry-title a::text").get()
    timestamp = selector.css("ul.post-meta li::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = selector.css("div.post-comments h5::text").get()
    if comments_count is None:
        comments_count = 0
    summary = selector.css("div.entry-excerpt::text").get()
    tags = selector.xpath("//section.post-tags/ul/li/a/text()").getall()
    category = selector.css("a.category-style span.label::text").get()
    dicio = {
        "url": url,
        "title": str(title).rstrip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": int(comments_count),
        "summary": str(summary).strip(),
        "tags": tags,
        "category": str(category),
    }
    print(f"🔥🔥🔥{dicio}")
    return dicio


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
