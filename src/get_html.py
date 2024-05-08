from selenium import webdriver
from selenium.webdriver.edge.options import Options


def get_html(url):
    options = Options()
    options.headless = True

    driver = webdriver.Edge(options=options)
    driver.get(url)
    html_page = driver.page_source
    print('data collected')
    driver.quit()

    return html_page
