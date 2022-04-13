# uitleg
from itertools import count
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

# finalArtists = []

# tagnames = ["h2", "h3", "h4"]

# for tagname in tagnames:
#     artists = extremahomepageBS.find_all(tagname, { "class": "artists_naam"})

#     for artist in artists:
#         if artist.get_text() not in finalArtists:
#             finalArtists.append(artist.get_text())

# finalArtists.sort()
# print(len(finalArtists))




# Excercise 3:
# Get all the eurosongfestival winners (https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival)
# Percentage per land
# 1969 WHY Y SCREW ME?
# url = "https://nl.wikipedia.org/wiki/Lijst_van_winnaars_van_het_Eurovisiesongfestival"
# request = requests.get(url) 
# wikiEurovisionBS = BeautifulSoup(request.text, "html.parser")

# tableRowElements = wikiEurovisionBS.find("table", { "class" : "wikitable"}).find("tbody").find_all("tr")

# winners = []

# for row in tableRowElements:
#     columns = row.find_all("td")
#     if len(columns) == 6:
#         countryColumn = columns[1]
#         countryName = countryColumn.get_text().strip()

#         if "(" in countryName:
#             countryName = countryName[:-3].strip()

#         winners.append(countryName)

# finalResult = {}

# for winner in winners:
#     if winner in finalResult.keys():
#         finalResult[winner] = round((finalResult[winner] + 1) / len(winners) * 100, 2)
#     else:
#         finalResult[winner] = round(1 / len(winners) * 100, 2)

# print(finalResult)

# nederland 1% 
# zwitserland 2%





# Excercise 4:
# Get the winner of ultratop singles top 50
# 1st place - 50 points
# 2th place - 49 points
# ..

for year in range(2018, 2022):
    url = "https://www.ultratop.be/nl/ultratop50/" + str(year) + "/"
    request = requests.get(url)
    weeksBS= BeautifulSoup(request.text, "html.parser")
    dates = weeksBS.find("select", { "id" : "chartdate"}).find_all("option")

    weeks = []
    for week in dates:
        weeks.append(week.get("value"))

    # print(weeks)
    print("-----", year)
    scoreboard = {}

    for week in weeks:
        url = "https://www.ultratop.be/nl/ultratop50/" + str(year) + "/" + week
        print("Call naar " + week)
        request = requests.get(url)

        latestSongBS = BeautifulSoup(request.text, "html.parser")
        charts = latestSongBS.find_all("div", { "class" : "chart_title"})

        chartIndex = 0

        for chart in charts:
            artistName = chart.find("a").find("b").get_text()
            track = chart.find("a").get_text().replace(artistName, "")

            fulltrack = artistName + " - " + track

            if fulltrack in scoreboard.keys():
                scoreboard[fulltrack] = scoreboard[fulltrack] + (50 - chartIndex)
            else:
                scoreboard[fulltrack] = 50 - chartIndex

            chartIndex+=1


    winner = max(scoreboard, key=scoreboard.get)
    print(winner)