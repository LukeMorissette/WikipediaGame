"""
Wikipedia Path Finder

This script allows users to find a path between two Wikipedia articles using backlinks and breadth-first search.

Usage:
1. User provides a starting Wikipedia article.
2. User provides a final Wikipedia article.
3. The script finds a path between the two articles and prints the path along with the number of discovered pages and time taken.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import threading

# Function to retrieve backlinks for a given Wikipedia page
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

def find_path_threaded(start_page, finish_page):
    thread = threading.Thread(target=find_path, args=(start_page, finish_page))
    thread.start()

# Function to retrieve links from a given Wikipedia page
def get_links(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
    return links

# Function to find a path between two Wikipedia articles
# Function to find a path between two Wikipedia articles
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

    # Breadth-first search
    while queue:  
        (vertex, path, depth) = queue.pop(0)
        log = ""  # Initialize log here
        for next_page in set(get_links(vertex)) - discovered:
            if next_page in backlinks:
                print(f"Found: {next_page}")
                logs.append(log)
                logs.append(f"Discovered pages: {len(discovered)}")
                end_time = time.time()
                output = next_page
                if next_page != finish_link:
                    output += f", {finish_link}"
                print(f"Path found: {path + [output]}")
                print(f"Time taken: {end_time - start_time} seconds")
                return path + [output], logs, len(discovered)  # Return with success
            else:
                log = f"Adding link to queue: {next_page} (depth {depth})"
                logs.append(log)
                discovered.add(next_page)
                queue.append((next_page, path + [next_page], depth + 1))
        logs.append(f"Discovered pages: {len(discovered)}")
        
while True:
    input1 = input('Please enter your starting article: ')
    input2 = input('Please enter your final: ')
    find_path_threaded(input1, input2)