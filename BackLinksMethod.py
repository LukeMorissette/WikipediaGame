import requests
import gensim
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import re



def get_backlinks(page_title):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "backlinks",
        "bltitle": page_title,
        "bllimit": "500"
    }

    backlinks = set()
    try:
        while True:
            response = S.get(url=URL, params=PARAMS)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()

            for bl in data['query']['backlinks']:
                title = bl['title']
                # Replace spaces with underscores and encode non-ASCII characters
                safe_title = requests.utils.quote(title.replace(' ', '_'))
                url = f"https://en.wikipedia.org/wiki/{safe_title}"
                backlinks.add(url)

            if 'continue' not in data:
                break
            PARAMS['blcontinue'] = data['continue']['blcontinue']

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Data parsing failed: {e}")

    return backlinks

def get_links(page_url):
    # print(f"Fetching page: {page_url}")
    response = requests.get(page_url)
        # print(f"Finished fetching page: {page_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
        # print(f"All links found: {all_links}")
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
        # print(f"Found {len(links)} links on page: {page_url}")
    return links


def find_path(start_page, finish_page):
    start_time = time.time()
    name_url_part = start_page.replace(' ', '_')
    start_page = f'https://en.wikipedia.org/wiki/{name_url_part}'
    print(start_page)
    queue = [(start_page, [start_page], 0)]
    discovered = set()
    logs = []
    backlinks = list(get_backlinks(finish_page))
    print(backlinks[:10])
    name_url_part = finish_page.replace(' ', '_')
    finish_link = f'https://en.wikipedia.org/wiki/{name_url_part}'
    backlinks.append(finish_link)
    print(finish_page)

    # breadth first search
    while queue:  
        (vertex, path, depth) = queue.pop(0)
        for next in set(get_links(vertex)) - discovered:
            if next in backlinks:
                print(f"Found: {next}")
                logs.append(log)
                logs.append(f"Discovered pages: {len(discovered)}")
                end_time = time.time()
                output = next
                if next != finish_link:
                    output += f", {finish_link}"
                print(f"Path found: {path + [output]}")
                print(f"Time taken: {end_time - start_time} seconds")
                return path + [output], logs, len(discovered) # return with success
            else:
                log = f"Adding link to queue: {next} (depth {depth})"
                logs.append(log)
                discovered.add(next)
                queue.append((next, path + [next], depth + 1))
        logs.append(f"Discovered pages: {len(discovered)}")


while(True):
    input1 = input('Please enter your starting article: ')
    input2 = input('Please enter your final: ')
    find_path(input1, input2)
