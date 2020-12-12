#!/usr/bin/env python
# coding: utf-8

# # NASA Article Scraping

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
#url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


#set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# # NASA Image Scraping

# In[8]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[14]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


browser.quit()


# In[17]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[18]:


# Set the executable path and initialize the chrome browser in splinter
crome_path = "C:/Users/aksha/Downloads/chromedriver_win32/chromedriver.exe"
browser = Browser("chrome", executable_path=crome_path, headless=True)
#executable_path = {'executable_path': '../aksha/Downloads/chromedriver_win32/'}
#browser = Browser('chrome', **executable_path)


# ### Visit the NASA Mars News Site

# In[19]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[20]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[21]:


slide_elem.find("div", class_='content_title')


# In[22]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[23]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[24]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[25]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[26]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[28]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[29]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[30]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[31]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[32]:


df.to_html()


# ### Mars Weather

# In[33]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[34]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[35]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[36]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[37]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
html = browser.html
news_soup = soup(html, 'html.parser')
table = news_soup.find('div', attrs='collapsible results')


for row in table.findAll('div',attrs={'class':'item'}):
    
    title = row.find('h3').text
    #print(title)
    link_tags = row.findAll('a', attrs={'class':'itemLink product-item'})
    uri = row.find("a")
    image_url = 'https://astrogeology.usgs.gov'+ uri['href']
    browser.visit(image_url)
    
    sub_html_string = browser.html
    sub_soup = soup(sub_html_string, 'lxml')
    
    image_url='https://astrogeology.usgs.gov' + str(sub_soup.find('img','wide-image')['src'])
    #print(image_url)

    hemispheres = {"img_url": image_url,"title": title}
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    
print(hemisphere_image_urls)


# In[38]:


# 4. Print the list of dictionary items.
hemisphere_image_urls


# In[39]:


# 5. Quit the browser
browser.quit()


# In[ ]:




