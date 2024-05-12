import yaml

from web_extractor import extract_data, web_extractor


class WebsiteUrl:
    def __init__(self):
        with open('config.yaml', 'r') as f:
            try:
                self.cfg = yaml.safe_load(f)
                self.websites = self.cfg['websites']

            except yaml.YAMLError as exc:
                print(exc)

        self.url_gen = self.next_url()

    def gen_url(self, name: str, args: dict[str, str | list[str]]) -> str:
        if type(args['jobs']) is list:
            args['jobs'] = '+'.join(args['jobs'])

        return self.websites[name]['template_url'].format(**args)

    def next_url(self):
        # print(self.websites.keys())
        for website in list(self.websites):
            yield website

    def parse_data(self, name, source):
        data = {}
        for item in self.websites[name]['parse']:
            data[item] = extract_data(source, *self.websites[name]['parse'][item])
        return data


if __name__ == '__main__':
    websites = WebsiteUrl()
    params = {'jobs': ['data', 'science', 'python'], 'location': 'krakow'}
    url = websites.gen_url('pl.indeed', params)
    print(url, '\n')

    soup = web_extractor(url)

    collected_data = websites.parse_data('pl.indeed', soup)
    print(collected_data, '\n')
