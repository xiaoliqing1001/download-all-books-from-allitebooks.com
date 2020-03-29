# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:52:31 2020

@author: Liqing XIAO
@email: xiaoliqing1001@aliyun.com

"""

import fileinput, json, re, requests, shutil
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
    pattern = re.compile('<a.*?href="http://file.allitebooks.com/(.*?)".*?>.*?</a>', re.S)
    items = re.findall(pattern, html)
    return items

def write_to_file(content):
    with open('2ebooks.txt', 'a', encoding = 'utf-8') as f:
        f.write(json.dumps(content, ensure_ascii = False) + '\n')

if __name__ == '__main__':
    shutil.copy(u'1url.txt',u'1url_bak.txt')
    for line in fileinput.input("1url.txt", inplace = 1):
        line = line.replace('"http', 'http')
        line = line.replace('/"', '/')
        print(line, end = "")

    file = open("1url.txt")
    page = 1
    while True:
        url = file.readline()
        if len(url) >= 28:
            print(page)
            write_to_file(page)
            html = get_one_page(url)
            for item in parse_one_page(html):
                print("http://file.allitebooks.com/" + item)
                write_to_file("http://file.allitebooks.com/" + item)
            page += 1
        else:
            break
    file.close()
