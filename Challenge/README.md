# Challenge 10 - Mission to Mars Web scraping

## Summary
In this Challenge we will use Splinter to automate the web browser of Mars’s hemispheres, BeautifulSoup to parse and extract full-resolution images of Mars’s hemispheres and the titles of those images, and MongoDB to hold the data that has been gathered.This data that is collected in Momgodb is then displayed on a web browser.

We have used the folowing version of softwares and dependencies.
Splinter - selenium-3.141.0 splinter-0.14.0
Web-Driver Manager-configparser-5.0.1 crayons-0.4.0 webdriver-manager-3.2.2
BeautifulSoup bs4-0.0.1
pymongo - pymongo-3.11.2
Mongo DB shell version - v4.4.2
ChromeDriver 87.0.4280.88 
scraping-0.0.3
flask-pymongo-2.3.0
python 3.7.7

## Results
### Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles.
#### a. Visit the url
The below code will visit the url
```
	# 1. Use browser to visit the URL 
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url)
```
#### b. Create a list to hold the images and titles.
```
	hemisphere_image_urls = []
```

#### c. Write code to retrieve the image urls and titles for each hemisphere.
The below code will look up for data in the required html tags and append the above list hemisphere_image_urls with the image url and tittle.
```
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
	
#### d. The final screen shot for the list hemisphere_image_urls which contains 4 dictionaries that have the respective image url and title.
[Image][1]

#### e. After the data is scraped we can check this information in the mongo db.

### Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
#### a. We export the Mission_to_Mars_Challenge.ipynb file to Mission_to_Mars_Challenge.py file. 

#### b. In the scraping.py file we create a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image.
```
	data = {
            "news_title": news_title,
            "news_paragraph": news_paragraph,
            "featured_image": featured_image(browser),
            "facts": mars_facts(),
            "last_modified": dt.datetime.now(),
            "hemisphere_data": hemisphere_scrape(browser) 
            } 
```
#### c. We create a function called hemisphere_scrape() which will scrape the hemisphere data and At the end of the function, return the scraped data as a list of dictionaries with the URL string and title of each hemisphere image.
```
	def hemisphere_scrape(browser) :
    		# 1. Use browser to visit the URL 
    		url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    		browser.visit(url)    

    		# 2. Create a list to hold the images and titles.
    		hemisphere_image_urls = []

    		# 3. Write code to retrieve the image urls and titles for each hemisphere.
    		browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    		html = browser.html
    		news_soup = soup(html, 'html.parser')
    		table = news_soup.find('div', attrs='collapsible results')

    		for row in table.findAll('div',attrs={'class':'item'}):
       		 	title = row.find('h3').text
        		print(title)
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
        
    	return hemisphere_image_urls 
```
#### d. After running the app.py file we get the data saved in the mars collection inside the mars_app mongodb 

[Image][2]

#### e. We finally loop the list in our index.html file to get all the images displayed.
```
	{% for hemisphere in mars.hemisphere_data %}
        <div class="col-md-6">
          <div class="thumbnail">
            <img src="{{hemisphere.img_url | default('static/images/error.png', true)}}" alt="...">
             <div class="caption">
              <h3>{{hemisphere.title}}</h3>
            </div>
          </div>
        </div>
        {% endfor %}


```

#### f. After scraping the data, the webpage has the full-resolution images and the titles of the four hemisphere images.
[final website][3]

### Deliverable 3: Add Bootstrap 3 Components

#### 1. Mobile Responsive
	Having the colums as " col-xs-*" from the Bootstrap 3 grid system, we have the web browser mobile responsive. This responsivness can be checked by 	right clicking the web page and choosing inspect. The inspect page will have the mobile icon on the left top corner and different responsiveness can 	be selected.
	However choosing the xs from the Bootstrap 3 grid system scales up to bigger versions.

#### 2 . Adding Bootstrap 3 components
	
	 a. Changed the scrape new data button color to green.
	 b. Change font size of Mars Fact table and add border.


[1]:[]
[2]:[]
[3]:[]
