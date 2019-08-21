from bs4 import BeautifulSoup
import sys
import urllib.request
import urllib.error as err


def web_crawler(file_type, link, filename):
	if file_type == "image":
		try:
			html_page = urllib.request.urlopen(link)
		except err.URLError:
			print("The post is probably from a private account")
			return
		soup = BeautifulSoup(html_page, 'html.parser')
		image = soup.find("meta",  property="og:image")["content"]
		urllib.request.urlretrieve(str(image), filename)

	if file_type == "video":
		try:
			html_page = urllib.request.urlopen(link)
		except err.URLError:
			print("The post is probably from a private account")
			return
		soup = BeautifulSoup(html_page, 'html.parser')
		image = soup.find("meta",  property="og:video")["content"]
		urllib.request.urlretrieve(str(image), filename)

try:
	web_crawler(sys.argv[1], sys.argv[2], sys.argv[3])
except IndexError:
	print("Usage: python3 save_insta_pic.py <type(image/video)> <link> <file name.jpg/filename.mp4>")
