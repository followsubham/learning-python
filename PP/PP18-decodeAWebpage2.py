# Using the requests and BeautifulSoup Python libraries, print to the screen the
# full text of the article on this website:
url= http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read the full
# article without having to click any buttons.
import requests
from bs4 import BeautifulSoup

r=requests.get(url)
read=BeautifulSoup(r.text)
all_p_cn_text_body = read.select("div.parbase.cn_text > div.body > p")
for elem in all_p_cn_text_body[7:]:
  print(elem.text)