import yaml


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


if __name__ == '__main__':
    websites = WebsiteUrl()
    params = {'jobs': ['data', 'science', 'python'], 'location': 'krakow'}
    url = websites.gen_url('pl.indeed', params)
    print(url, '\n')

    for tmp in websites.url_gen:
        print(tmp)

