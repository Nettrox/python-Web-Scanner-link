import requests
from bs4 import BeautifulSoup
#first you need download "pip install bs4" 

url = input("Link here: ")
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    print(link.get("href"))

input("Close!")
