# Feature extraction

from urllib import parse
from typing import List
import re


class UrlFeatureExtractor:
    chars = [('upper_alphabets', '[A-Z]'), ('lower_alphabets', '[a-z]'), ('digits', '[0-9]'),
             ('slash', '/'), ('colon', ':'), ('semicolon', ';'), ('dot', '.'), ('hash', '#'),
             ('dollar', '$'), ('percent', '%'), ('and', '&'), ('star', '*'), ('hyphen', '-'),
             ('underscore', '_'), ('plus', '+'), ('equals', '=')]

    def __init__(self):
        self.feature_dict = {}

    def extract_features(self, urls: List[str]):
        self.urls = urls
        self.feature_dict.update(self.get_lengths(self.urls))
        self.feature_dict.update(self.get_char_counts(self.urls))
        return self.feature_dict

    @staticmethod
    def parse_url(url: str) -> dict:
        """
        Split URL into: protocol, host, path, params, query and fragment.
        """
        if not parse.urlparse(url.strip()).scheme:
            url = 'http://' + url
        protocol, host, path, params, query, fragment = parse.urlparse(url.strip())

        result = {
            'url': host + path + params + query + fragment,
            'protocol': protocol,
            'host': host,
            'path': path,
            'params': params,
            'query': query,
            'fragment': fragment
        }
        return result

    @staticmethod
    def get_lengths(urls: List[str]) -> dict:
        lengths_dict = {
            'length_url': [],
            'length_host': [],
            'length_path': [],
            'length_params': [],
            'length_query': [],
            'length_fragment': []
        }
        for url in urls:
            try:
                result = UrlFeatureExtractor.parse_url(url)
                lengths_dict['length_url'].append(len(result['url']))
                lengths_dict['length_host'].append(len(result['host']))
                lengths_dict['length_path'].append(len(result['path']))
                lengths_dict['length_params'].append(len(result['params']))
                lengths_dict['length_query'].append(len(result['query']))
                lengths_dict['length_fragment'].append(len(result['fragment']))
            except Exception as e:
                lengths_dict['length_url'].append(-1)
                lengths_dict['length_host'].append(-1)
                lengths_dict['length_path'].append(-1)
                lengths_dict['length_params'].append(-1)
                lengths_dict['length_query'].append(-1)
                lengths_dict['length_fragment'].append(-1)
        return lengths_dict

    @staticmethod
    def get_char_counts(urls: List[str]) -> dict:
        char_counts_dict = {}
        for c in UrlFeatureExtractor.chars:
            char_counts_dict[f'qty_{c[0]}_url'] = []
            char_counts_dict[f'qty_{c[0]}_host'] = []
            char_counts_dict[f'qty_{c[0]}_path'] = []
            char_counts_dict[f'qty_{c[0]}_params'] = []
            char_counts_dict[f'qty_{c[0]}_query'] = []
            char_counts_dict[f'qty_{c[0]}_fragment'] = []
        for url in urls:
            try:
                result = UrlFeatureExtractor.parse_url(url)
                for i, c in enumerate(UrlFeatureExtractor.chars):
                    if i in [0, 1, 2]:
                        char_counts_dict[f'qty_{c[0]}_url'].append(len(re.findall(c[1], result['url'])))
                        char_counts_dict[f'qty_{c[0]}_host'].append(len(re.findall(c[1], result['host'])))
                        char_counts_dict[f'qty_{c[0]}_path'].append(len(re.findall(c[1], result['path'])))
                        char_counts_dict[f'qty_{c[0]}_params'].append(len(re.findall(c[1], result['params'])))
                        char_counts_dict[f'qty_{c[0]}_query'].append(len(re.findall(c[1], result['query'])))
                        char_counts_dict[f'qty_{c[0]}_fragment'].append(len(re.findall(c[1], result['fragment'])))
                    else:
                        char_counts_dict[f'qty_{c[0]}_url'].append(result['url'].count(c[1]))
                        char_counts_dict[f'qty_{c[0]}_host'].append(result['host'].count(c[1]))
                        char_counts_dict[f'qty_{c[0]}_path'].append(result['path'].count(c[1]))
                        char_counts_dict[f'qty_{c[0]}_params'].append(result['params'].count(c[1]))
                        char_counts_dict[f'qty_{c[0]}_query'].append(result['query'].count(c[1]))
                        char_counts_dict[f'qty_{c[0]}_fragment'].append(result['fragment'].count(c[1]))
            except:
                result = UrlFeatureExtractor.parse_url(url)
                for i, c in enumerate(UrlFeatureExtractor.chars):
                    char_counts_dict[f'qty_{c[0]}_url'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_host'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_path'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_params'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_query'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_fragment'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_url'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_host'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_path'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_params'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_query'].append(-1)
                    char_counts_dict[f'qty_{c[0]}_fragment'].append(-1)
        return char_counts_dict
