from bs4 import BeautifulSoup

file = open('recette.html', 'r')
html_content = file.read()
file.close()

body = BeautifulSoup(html_content, 'html.parser')
print(body.find("h1").text)

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