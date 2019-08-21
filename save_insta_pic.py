from bs4 import BeautifulSoup
import sys
import urllib.request


def web_crawler(link, folder):
	html_page = urllib.request.urlopen(link)
	soup = BeautifulSoup(html_page, 'html.parser')
	image = soup.find("meta",  property="og:image")["content"]
	urllib.request.urlretrieve(str(image), folder)

try:
	web_crawler(sys.argv[1], sys.argv[2])
except IndexError:
	print("Usage: python3 save_insta_pic.py <link> <file name.jpg>")
