import requests
from bs4 import BeautifulSoup
import codecs
import re

eastchester_scrape = requests.get("https://www.eufsdk12.org/domain/76")
soup = BeautifulSoup(eastchester_scrape.text,"html.parser")