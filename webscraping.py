import requests
import bs4

url = "https://techsoftindia.co.in"  # input("enter your url")
response = requests.get(url)
filename = "temp.html"
bs = bs4.BeautifulSoup(response.text, "html.parser")

formatted_text = bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
    f.write(formatted_text)

list_img = bs.find_all('img')
#print(list_img)

no_of_img = len(list_img)
# print(no_of_img)