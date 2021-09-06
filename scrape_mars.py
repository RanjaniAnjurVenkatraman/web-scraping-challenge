

from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape():
	
	# Setup splinter
	executable_path = {'executable_path': ChromeDriverManager().install()}
	browser = Browser('chrome', **executable_path, headless=False)
	
	# 1 NASA Mars News
	url = 'https://redplanetscience.com/'
	browser.visit(url)

	# To print latest News and Paragraph

	html = browser.html
	soup = bs(html, 'html.parser')
	
	news_title = soup.find_all('div', class_='content_title')[0].text
	news_p = soup.find_all('div', class_="article_teaser_body")[0].text
	
	# 2 JPL Mars Space Images	
	
	mars_img_url = "https://spaceimages-mars.com/"	
	browser = Browser('chrome', **executable_path, headless=False)
	browser.visit(mars_img_url)
	time.sleep(4)
	
	html= browser.html
	soup=bs(html, "lxml")

	result_url=soup.find_all("img")[1]["src"]
	featured_image_url="https://spaceimages-mars.com/"+result_url

	# 3 To retrieve mars facts
	facts_url = 'https://galaxyfacts-mars.com/'
	tables = pd.read_html(facts_url)
	
	mars_facts_df = tables[1]
	mars_facts_df.columns = ["Description", "Value"]

	#Convert dataframe to html

	mars_facts_html_table = mars_facts_df.to_html()

	#To remove \n
	mars_facts_html_table.replace('\n', '')

	# 4 Mars Hemispheres Images

	# Mars hemisphere name and image to be scraped
	base_url = 'https://marshemispheres.com/'
	hemispheres_url = 'https://marshemispheres.com/'

	browser.visit(hemispheres_url)

	hemispheres_html = browser.html

	hemispheres_soup = bs(hemispheres_html, 'html.parser')
	
	# Mars hemispheres products data
	all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
	mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')

	hemisphere_image_urls = []

	for i in mars_hemispheres:
        # Collect Title
        	hemisphere = i.find('div', class_="description")
        	title = hemisphere.h3.text        
        # Collect image link by browsing to hemisphere page
        	hemisphere_link = hemisphere.a["href"]    
        	browser.visit(base_url + hemisphere_link)        
        	image_html = browser.html
        	image_soup = bs(image_html, 'html.parser')        
        	image_link = image_soup.find('div', class_='downloads')
        	image_url = image_link.find('li').a['href']
        # Create Dictionary to store title and url info
        	image_dict = {}
        	image_dict['title'] = title
        	image_dict['img_url'] = base_url + image_url        
        	hemisphere_image_urls.append(image_dict)

	browser.quit()

	mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,       
        "fact_table": str(mars_facts_html_table),
        "hemisphere_images": hemisphere_image_urls
    	}
	
	
	
	return mars_dict 

