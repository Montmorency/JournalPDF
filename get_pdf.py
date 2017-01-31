import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="url for article", type=str, default="")
args = parser.parse_args()
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
if args.url == "":
  url    = "http://www.sciencedirect.com/science/article/pii/0001616070900787"
else:
  url = args.url
r        = requests.get(url, headers=header)
soup     = BeautifulSoup(r.text, "lxml")
pdf_link = soup.find(class_="pdf")
pdfurl   = 'http:'+pdf_link.attrs['pdfurl']
print pdfurl

r = requests.get(pdfurl, headers=header)
with open("paper.pdf", 'wb') as f:
  f.write(r.content)
