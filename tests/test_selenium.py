import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")

driver = webdriver.Edge(options=options)
driver.get("https://pl.indeed.com/jobs?q=data+science+internship+python&l=krakow")

print(driver.page_source)
driver.quit()
