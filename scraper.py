import random
import requests
import datetime
import time
from urls import urls
from bs4 import BeautifulSoup

# initialising my headlines list to be populated by dictionary objects
headlines = []
fail = "Currently unable to get headlines for "

primicia_url = "https://primicia.com.ve/tag/femicidio/"


guardian_url = "https://www.theguardian.com/uk"
times_url = "https://www.thetimes.co.uk/"
telegraph_url = "https://www.telegraph.co.uk/"
dailymail_url = "https://www.dailymail.co.uk/home/index.html"
dailymirror_url = "https://www.mirror.co.uk/"
dailyexpress_url = "https://www.express.co.uk/"
independent_url = "https://www.independent.co.uk/news/uk"
financialtimes_url = "https://www.ft.com/"
inews_url = "https://inews.co.uk/"
morningstar_url = "https://morningstaronline.co.uk/"
dailystar_url = "https://www.dailystar.co.uk/"
sun_url = "https://www.thesun.co.uk/"
eveningstandard_url = "https://www.standard.co.uk/"
irishsun_url = "https://www.thesun.ie/"
herald_url = "https://www.heraldscotland.com/"
metro_url = "https://metro.co.uk/"

def scrape(url):
  
  randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

  headers = {
    'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Referer': random.choice(randomUrls) 
    }

  results = requests.get(url, headers=headers, allow_redirects=False)

  # beautiful soup methods are now available to clean this data response
  soup = BeautifulSoup(results.text, "html.parser")

  if url == primicia_url:
    paper = "Primicia"
    headline_html = soup.find('h5', class_='card-title title-thumb')
    link = url
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

  time_stamp = datetime.datetime.now()
  date_stamp = time_stamp.strftime("%H:%M:%S (%Y-%m-%d)")
 
  # here i create the dictionary object, populating it with the following key/value pairs
  # these key/value pairs will be available on the front end app to display
  myDictObj = { "paper": paper, "headline": headline, "updated": date_stamp, "link": link }
  # once the dictionary object is created, each one goes into my headlines list
  headlines.append(myDictObj)