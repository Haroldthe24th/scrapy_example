import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd

# read url from input
original_url = input("Enter the website url: ") 

# to save urls to be scraped
unscraped = deque([original_url])

# to save scraped urls
scraped = set()

# to save fetched emails
emails = set()


while len(unscraped):
    # move unsraped_url to scraped_urls set
    url = unscraped.popleft()  # popleft(): Remove and return an element from the left side of the deque
    scraped.add(url)