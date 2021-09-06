# web-scraping-challenge
Web application that scrapes data from various websites related to the Mission to Mars and displays the information in a HTML page using BeautifulSoup, Splinter  and MongoDB with Flask

# Web Scraping - Mission to Mars

This challenge demonstrates to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

The technologies used in this project are:

` BeautifulSoup | Flask | Selenium | Splinter | MongoDB | Pandas `

Websites scraped:
- [NASA Mars News Site](https://redplanetscience.com/) : Collect the latest News Title and Paragraph Text. 
- [JPL Featured Space Image](https://spaceimages-mars.com/) : Find the image url for the current Featured Mars Image.
- [ Mars Facts webpage](https://galaxyfacts-mars.com/) : Scrape the table containing facts about the planet including Diameter, Mass, etc using Pandas.
- [ Mars Hemispheres](https://marshemispheres.com/) : Obtain high resolution images for each of Mar's hemispheres.


This challenge is done in 2 steps:

## Step 1 - Scraping

Completed initial scraping from various websites using BeautifulSoup, Pandas, and Splinter.

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Created a route called `/scrape` that will import [scrape_mars.py](scrape_mars.py) script and call the `scrape` function.
* Stored the return value in Mongo as a Python dictionary.
* Created a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
* Created a template HTML file called [index.html](index.html) that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

![main_page](static/screenshots/main_page.png)
![Mars_news_img_facts](static/screenshots/Mars_news_img_facts.png)
![Mars_hemisphere_imgs](static/screenshots/Mars_hemisphere_imgs.png)
