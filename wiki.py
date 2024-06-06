import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

soup = BeautifulSoup(page.content, "html.parser")

paragraphs = soup.find_all(['p', 'li'])

for para in paragraphs:
    print(f"\n{para.get_text()}")