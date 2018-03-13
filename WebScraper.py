from urllib.request import urlopen as uOpen
from bs4 import BeautifulSoup as soup

target = 'https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100007708%20600536049%20600536050%20600565061%20600565504%20600565674%20601107975%20601203793%20601204369%20601210955%20601205646%20601202919%20601203927%20601203901%20601294835%20601295933%20601194948%20601296707&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_2'

#open connection, grab page, and then close connection
Client = uOpen(target)
html = Client.read()
Client.close()

#html parsing
soupy = soup(html, "html.parser")

#grabbing each product
containers = soupy.findAll("div", {"class":"item-container"})

print("Welcome to the NewEgg GPU WebScraper!\n")



for container in containers:
    manufacturer = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    title = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("Manufacturer: " +manufacturer)
    print("Title: " +title)
    print("Shipping: " +shipping +"\n")
