import re

from bs4 import BeautifulSoup

from get_html import get_html


def web_extractor(url: str, parser: str = 'html.parser') -> BeautifulSoup:
    htmldata = get_html(url)
    soup = BeautifulSoup(htmldata, parser)

    return soup


def extract_data(source, name, css_class, atr):
    extracted_data = []
    if css_class == 'class_':
        for item in source.find_all(name, class_=atr):
            extracted_data.append(item.get_text())
    if css_class == 'attrs':
        for item in source.find_all(name, attrs=atr):
            extracted_data.append(item.get_text())
    if css_class == 'class_link':
        for item in source.find_all(name, class_=atr):
            extracted_data.append(item.get('href'))

    return extracted_data
