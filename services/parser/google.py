from GoogleScraper import scrape_with_config, GoogleSearchError


class Parser:

    def __init__(self, word):
        self._config = {
            'use_own_ip': True,
            'keyword': word,
            'search_engines': ["google"],
            'num_pages_for_keyword': 1,
            'scrape_method': 'http',
            'do_caching': False
        }

    @property
    def attr(self):
        return self._config

    def parse(self):
        return scrape_with_config(self._config)


