from bs4 import BeautifulSoup

import urllib.request

import nltk

# The urllib library will crawl the web page
response = urllib.request.urlopen('https://www.gutenberg.org/cache/epub/10/pg10.txt')

html = response.read()


# The BeautifulSoup library will 'clean' the page of HTML tags
soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)

# Convert the cleaned text into tokens
tokens = [t for t in text.split()]


# The NLTK library function - "FreqDist" - will count 
# the frequency of each word
freq = nltk.FreqDist(tokens)

print(freq.most_common(50))