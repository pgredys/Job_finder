import pandas as pd

from gen_url import WebsiteUrl
from web_extractor import web_extractor

params = {'jobs': ['data', 'science', 'python'], 'location': 'krakow'}

websites = WebsiteUrl()
for website in websites.url_gen:

    url = websites.gen_url(website, params)
    web = web_extractor(url)

    collected_data = websites.parse_data(website, web)

collected_data['link'] = [url.rsplit("/", 1)[0] + i for i in collected_data['link']]

data = pd.DataFrame.from_dict(collected_data)
data.to_csv('data.csv')
