import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.decathlon.ma/4896-homme')

def main(page) :
    src  = page.content
    soup = BeautifulSoup(src, "lxml")
    print(soup)

main(page)