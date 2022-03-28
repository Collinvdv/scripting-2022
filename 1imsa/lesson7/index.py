from bs4 import BeautifulSoup
import requests
import numpy as np

# url = "https://en.wikipedia.org/wiki/Soup"
# r = requests.get(url)
# text = r.text     #returns html as a string

# soup = BeautifulSoup(r.text)

# a_tags = soup.find_all('a',{ "class" : "interlanguage-link-target" }) # <a class="interlanguage-link-target"><span></span> ifjeoiroin </a>
# print(a_tags)

# for tag in a_tags:
#     print(tag.get('lang')) # .get() -> attribute van html gaan opvragen 
#     print(tag.get_text()) # . get_text() -> innerHTML

# 


# Exercise 1:
# Scrape all the projects from collinvandervorst.be
# requestPortfolio = requests.get("https://collinvandervorst.be/").text
# portfolioBS = BeautifulSoup(requestPortfolio,  "html.parser")

# projects = portfolioBS.find_all("", { "class" : "c-projects__item-title"})

# for project in projects:
#     print(project.get_text().strip())

# requestHomepageXO = requests.get("https://extrema.be/").text
# homepageBS = BeautifulSoup(requestHomepageXO, "html.parser")

# artists = []

# # artist in H2
# artistsTags = ["h2", "h3", "h4", "h5"]

# for tagName in artistsTags:
#     artistsElements = homepageBS.find_all(tagName, { "class" : "artists_naam"})

#     for artist in artistsElements:
#         artists.append(artist.get_text().strip())

# # final result
# artists.sort()
# artistNP = np.unique(np.array(artists))
# print(artistNP)















# Excercise 2:
# Get all the eurosongfestival winners (https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival)
# Percentage taal winners
# Percentage land winnaars
# 1969 WHY Y SCREW ME? 





# Excercise 2:
# Get the winner of ultratop singles top 50