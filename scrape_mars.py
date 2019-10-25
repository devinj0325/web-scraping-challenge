#Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
import pandas as pd

# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
#!which chromedriver

# Set Executable Path & Initialize Chrome Browser
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    mars_data = {}
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


## NASA Mars News

def marsNews():
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    print(news_title)
    print(news_p)

## JPL Mars Space Images -> Featured Image
def marsImage():
#JPL Mars Space Images
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image = soup.find("img")["src"]
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/assets/images/logo_nasa_trio_black@2x.png" + image

    print(featured_image_url)
# # Mars Weather
def marsWeather():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

#Save the tweet text for the weather report as a variable called mars_weather
    target_user = "MarsWxReport"
#latest tweet
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')
    latest_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    latest_tweet


## Mars Facts
def marsFacts():

    mars_df = pd.read_html("https://space-facts.com/mars/")[0]
    print(mars_df)

#HTML Table
    mars_df.columns=["Description", "Mars", "Earth"]

    mars_df.set_index("Description", inplace=True)
    mars_df


## Mars Hemispheres
def marsHemispheres():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

hemisphere_image_urls = []

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]


    
hemisphere_image_urls