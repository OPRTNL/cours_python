# https://codeavecjonathan.com/res/programmation.txt
# https://codeavecjonathan.com/res/pizzas1.json
# https://codeavecjonathan.com/res/exemple.html

from os import write
import requests
import json

# requete JSON
"""
response = requests.get("https://codeavecjonathan.com/res/pizzas1.json")
if response.status_code == 200:
    response.encoding = "utf-8"
    pizzas = json.loads(response.text)
    print(pizzas)
else:
    print("Erreur a revoir" + str(response.status_code))


print(response.text)
"""

# requete HTML
"""
response = requests.get("https://codeavecjonathan.com/res/exemple.html")
if response.status_code == 200:
    response.encoding = "utf-8"
    print(response.text)
    """

# Requete image
response = requests.get("https://photographylife.com/wp-content/uploads/2018/11/Moeraki-Boulders-New-Zealand.jpg")
if response.status_code == 200:
    file = open('papillon.jpg',"wb")
    file.write(response.content)
    file.close()
    print("c'est bon chef")