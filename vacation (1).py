#luis
#vacation.py
#Create a Python program that displays an image and a description from a selected theme each time the user desires a recommendation.
# The images must be stored as URLs in an array. Additionally, you will have an array of descriptions to go along with the images.

#initalization
import webbrowser
url = ["https://www.pushpintravelmaps.com/cdn/shop/articles/LondonSkyline_1.jpg?v=1558042739", "https://thattravelista.com/wp-content/uploads/2020/08/France-Paris-12.jpg",
       "https://onegirlwholeworld.com/wp-content/uploads/2021/01/rome_italy_first-timers_IMG_2370.jpg", "https://s.abcnews.com/images/Travel/GTY_hawaii_kab_140620_16x9_992.jpg?w=1600" ]
description = ["I would recommend going to the UK, London. London is filled with iconic sights to view, going from buildings, bridges, to landmarks",
               "I would recommend going to France, Paris. While Paris is very well known for Eiffel Tower, it's also known as the city of love.",
                "I would recommend going to Italy, Rome. It has very good food, the history is electric, and its full of charm and beautfil fountains",
                 "I would recommend going to the USA, Hawaii. It has many traditional foods, skip the buffet and go to the local to find tasting food." ]

#function
def travel_location():
    print("Welcome! I've got some questions to determine the best and efficient trips that you want to go!")
    print("Do you want to go that is known for food or be as a tourist?: ")
    if input() == "food":
              print("Alright, I'll make sure you eat good!")
              print("OK, do you want to go to Europe or North America?: ")
              if input() == "Europe":
                     print("OK! I got the perfect place for you to go!")
                     print(description[2])
                     webbrowser.open(url[2])
              else:
                     print("OK! I got the perfect place for you to go!")
                     print(description[3])
                     webbrowser.open(url[3])
    else:
       print("Alright, I'll make sure you have beautiful views to take photos")
       print("OK, do you want to go based on history or for love?: ")
       if input() == "history":
              print("OK! I got the perfect place for you to go")
              print(description[0])
              webbrowser.open(url[0])
       else:
              print("OK! I got the perfect place for you to go!")
              print(description[1])
              webbrowser.open(url[1])
#main
travel_location()

#Source Of Information
#Picture of UK, London
#AUTHOR NAME: Push Pin Travel Maps
#URL[0]:https://www.pushpintravelmaps.com/blogs/pinning-away/7-sights-you-must-see-in-london-uk?srsltid=AfmBOorS1FIBKfDxNe2EfHrfOb46zpDSDhNW9ZbonoLTabqm5WA4CMLa
#DATE: May 21, 2018
#ARTICLE NAME: 7 Sights You Must See In London, UK

#Picture of France, Paris
#AUTHOR NAME: That Travelista
#URL[1]: https://thattravelista.com/paris-france-attractions-things-to-do/
#DATE: March 24, 2025
#ARTICLE NAME: 20 Top Attraction and Things to do in Paris, France

#Picture of Italy, Rome
#AUTHOR NAME:
#uRL[2]: https://onegirlwholeworld.com/europe/what-to-do-rome-italy/
#DATE: February 10, 2021
#ARTICLE: A First-Timer's Guide To Rome, Italy

#Picture of USA, Hawaii
#AUTHOR NAME: Gabe Sagile
#URL[3]:https://abcnews.com/travel/skip-honolulu-hawaii/story?id=24235702
#DATE: June 21, 2014
#ARTICLE NAME: See This, Skip That: Honolulu
