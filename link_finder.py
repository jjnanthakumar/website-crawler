from bs4 import BeautifulSoup
import requests, ssl
import re

# Ignore SSL certificate errors
g_url = input('Enter URL to Crawl - ')

if not bool(re.search(r'^http', g_url)):
    raise ValueError("Please provide a Valid URL :(")



def crawl(url, prev_data=set()):
    try:
        calls = int(input("How many times should the crawl occur repeatedly ? -> "))
        ctx = ssl.create_default_context()

        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        # use any free apis find here->https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup('title')[0].text
        title = title.split()[0]
        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            link = tag.get('href', None)
            if link is not None and bool(re.search(r'^https://', link)):
                prev_data.add(link)
        c = 0
        print("Please be patient :) It takes more time to crawl all links if call input is more than 100!")
        while (list(prev_data)[c]):
            ctx = ssl.create_default_context()
            url = list(prev_data)[c]
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            # use any free apis find here->https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')

            # Retrieve all of the anchor tags
            tags = soup('a')
            for tag in tags:
                link = tag.get('href', None)
                if link is not None and bool(re.search(r'^https://', link)):
                    prev_data.add(link)
            c += 1
            if c > calls:
                raise EOFError

    except:
        import random, os
        fname = f'crawles{title}'
        with open(f'websites/{fname}.txt', 'w') as f:
            f.write('\n'.join(prev_data))
            print(f"The site {globals()['g_url']}  has been successfully Crawled :)")
            print("Find Crawled links here: " + os.path.abspath(fname))


crawl(g_url)
