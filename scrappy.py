from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://ofertas.mercadolibre.com.ar/ofertas-de-la-semana#c_id=/home/week-deal/element"

# abre la conexión y agarra la página
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parsea el html
page_soup = soup(page_html, "html.parser")

# agarra cada producto
containers = page_soup.findAll("div", {"class":"rowItem item highlighted item--grid item--has-row-logo new with-reviews"})



for container in containers:
    nombre_producto = container.findAll("span", {"class":"main-title"})
    precio_viejo = container.findAll("span", {"class":"price-old"})
    precio_nuevo = container.findAll("span", {"class":"price__fraction"})
    descuento = container.findAll("div", {"class":"item__discount"})

    print(nombre_producto[0].text)
    print("Precio anterior: ", precio_viejo[0].text.strip())
    print("Precio en oferta: ", precio_nuevo[0].text)
    print("Descuento: ", descuento[0].text + "\n")



