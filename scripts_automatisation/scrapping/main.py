from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

f = open("data.csv","w")

file = open('doc.html', 'r')
html_content = file.read()
file.close()
 
driver = webdriver.Chrome(ChromeDriverManager().install())

body = BeautifulSoup(html_content, 'html.parser')
# print(body.findAll("h3"))

listexpo = body.findAll("h3")




for i in  listexpo:
    url = i.find('a')['href']
    nom = i.find('a').text
    print(nom)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    tel = soup.findAll('div',class_="text")[0].text
    time.sleep(.5)
    f.write(tel)
    f.write(", ")
    f.write(nom)
    f.write(",\n")



f.close()

"""
desciption = body.find("p", class_="description")
print("paragraphe de description " + desciption.text)

list_p = body.findAll('div',class_="centre")

#print(list_p)
print(list_p[0].text)


div_info = body.find('div',class_="info")
print(div_info)
if div_info:
    print(div_info.find('img')['src'])
else:
    print("pas cool")
"""