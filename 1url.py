# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:50:23 2020

@author: Liqing XIAO
@email: xiaoliqing1001@aliyun.com

"""

import json, re, requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<h2.*?href="(.*?)".*?>.*?</h2>', re.S)
    items = re.findall(pattern, html)
    return items

def write_to_file(content):
    with open('1url.txt', 'a', encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii = False) + '\n')

def main(page):
    url = 'http://www.allitebooks.com/page/' + str(page)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    last_page = 852
    # http://www.allitebooks.org/page/852/ , last page of today
    for i in range(1, last_page + 1):
        main(page = i)
