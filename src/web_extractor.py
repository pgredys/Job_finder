from bs4 import BeautifulSoup

from get_html import get_html


def web_extractor(url: str, parser: str = 'html.parser') -> BeautifulSoup:
    htmldata = get_html(url)
    soup = BeautifulSoup(htmldata, parser)

    return soup
