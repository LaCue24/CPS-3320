import requests
from bs4 import BeautifulSoup

url = "https://api.phish.net/v3/setlists/latest?apikey=0869595E156BE41D7700"

payload = "{}"
response = requests.request("GET", url, data=payload)

# Print the raw unformatted data
# print(response.text)

# Parse the data as HTML, then print it in a nice formatted style
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('a')

# Create for loop to print out all link names
# for i in item:
#     print(i.prettify())



# Instead of printing the entire link and its tag, we’ll print the list of children
for j in items:
    print(j.contents[0])

