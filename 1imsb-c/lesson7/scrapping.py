# uitleg
from typing import final
from bs4 import BeautifulSoup
import requests

# url = "https://en.wikipedia.org/wiki/Soup"
# request = requests.get(url)
# soupBS = BeautifulSoup(request.text)

# links = soupBS.find_all("a", { "class" : "interlanguage-link-target"}) #all links

# # .get() -> value van een class atribute gaan teruggeven <a class="interlanguage-link target" title="language"
# # .get_text() -> innerHTML van een  bepaalde tag
# for link in links:
#     print(link.get("title"))
#     print(link.get_text())


# Exercise 1:
# https://collinvandervorst.be/
# projects 
# O: Bogaert Dirk
# O: De kleine deugd
# ..

# url = "https://collinvandervorst.be/"
# request = requests.get(url) 
# collinhomepageBS = BeautifulSoup(request.text)

# projects = collinhomepageBS.find_all("h4", { "class" : "c-projects__item-title"})

# for project in projects:
#     print(project.get_text().strip())



# Excercise 2:
# Give me all the artists of "https://extrema.be/"

url = "https://extrema.be/"
request = requests.get(url) 
extremahomepageBS = BeautifulSoup(request.text, "html.parser")

finalArtists = []

tagnames = ["h2", "h3", "h4"]

for tagname in tagnames:
    artists = extremahomepageBS.find_all(tagname, { "class": "artists_naam"})

    for artist in artists:
        if artist.get_text() not in finalArtists:
            finalArtists.append(artist.get_text())

finalArtists.sort()
print(len(finalArtists))




# Excercise 3:
# Get all the eurosongfestival winners (https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival)
# Percentage per land
# 1969 WHY Y SCREW ME?










# Excercise 4:
# Get the winner of ultratop singles top 50
# 1st place - 50 points
# 2th place - 49 points
# ..
