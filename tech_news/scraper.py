# from parsel import Selector
import requests


# Requisito 1
def fetch(url):
    for _ in range(15):
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=1
            )
        if response.status_code == 200:
            print(response.status_code)
            return response
            # time.sleep(1)
        else:
            return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
