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
# Percentage land winnaars
# 1969 WHY Y SCREW ME?

# requestWiki = requests.get("https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival").text
# wikiBS = BeautifulSoup(requestWiki,  "html.parser")

# rows = wikiBS.find("table", {"class" : "wikitable"}).find_all("tr")
# countryWinners = []

# # # mapping van countries
# for row in rows:
#     columns = row.find_all("td")
#     if len(columns) == 6: #hier filter ik 2020 alvast uit
#         country = columns[1].get_text().strip()

#         if "(" in country:
#             country = country[:-3].strip()

#         countryWinners.append(country)

# print(countryWinners)
# # # unique countries
# uniqueCountries = np.unique(np.array(countryWinners))

# countriesDict = {}
# for country in uniqueCountries:
#     countryAmount = countryWinners.count(country)

#     countriesDict[country] = countryAmount / len(countryWinners) * 100

# print(countriesDict)









# Excercise 2:
# Get the winner of ultratop singles top 50
# 1st place - 50 points
# 2th place - 49 points
# ..

requestWeeks = requests.get("https://www.ultratop.be/nl/ultratop50/2022/20220326").text
ultratopPageBS = BeautifulSoup(requestWeeks,  "html.parser" )
chartDateElements = ultratopPageBS.find("select", { "id" : "chartdate"}).find_all("option")

weeks = []

for element in chartDateElements:
    weeks.append(element.get("value"))

gradebook = {}

for week in weeks:
    print("Call naar " + "https://www.ultratop.be/nl/ultratop50/2022/" + week)
    requestPlaylist = requests.get("https://www.ultratop.be/nl/ultratop50/2022/" + week).text
    playlistBS = BeautifulSoup(requestPlaylist,  "html.parser")

    songs = playlistBS.find_all("div", { "class" : "chart_title"})


    for songIndex in range(0, len(songs)):
        # track opgezocht
        song = songs[songIndex]
        points = 50 - songIndex
        artistname = song.find("b").get_text()
        songname = song.get_text().replace(artistname, "").strip()
        track = artistname + " - " + songname

        # save to gradebook
        if track in gradebook: #.has_key() check if key is excisting
            gradebook[track] += points
        else:
            gradebook[track] = points


winner = max(gradebook, key=gradebook.get)
print(winner + " met het aantal punten van " + gradebook)