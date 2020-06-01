import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.pexels.com/search/nature/'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all element for image tag
image_tag = soup.findAll('img')

# create dictionory for image
if not os.path.exists('arts'):
    os.makedirs('arts')

os.chdir('arts')

# image file name variables
x = 0

for image in image_tag:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('art-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                print(x)
                x += 1
    except:
        pass
