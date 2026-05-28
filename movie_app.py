#Movie_app.py
#I want to code movie app that allows the user to identify using these constraints and generate an output based on the parameter they put.

#Initalization
import pandas as pd
import time
#Function
data = pd.read_csv("Netflix Content - Sheet1.csv")
type = data['Type'].tolist()
title = data['Title'].tolist()
country = data['Country'].tolist()
date_added = data['Data Added'].tolist()
year = data['Release Year'].tolist()
rating = data['Rating'].tolist()
genre = data['Genre'].tolist()
filter = []
def menu(location, variety, calendar, category, ranking):
        print("Welcome to THE Movie App!")
        time.sleep(1)
        print("This app helps with everything! Whether you want to watch a new movie, a specific, or even find what movies suit you!")
        time.sleep(1)
        print("Its not only movies! There are TV shows as well!")
        time.sleep(1)
        print("What do you want to do? Here are your options...")
        time.sleep(1)
        while True:
            print("Option 1: I want to watch a new movie/TV show!")
            print("Option 2: I want to watch a movie/TV show based on the country!")
            print("Option 3: I want to watch a old/recent movie/TV show!")
            print("Option 4: I want to watch a movie/TV show based on the genre!")
            print("Option 5: QUIT...")
            choice = input()
            if choice == "1":
                print("Welcome to the 1st option!")
                time.sleep(1)
                print("So you want to find a new movie and/or new tv shows.")
                time.sleep(1)
                print("OK! Let's find you a new show/movie to watch!")
                for i in range(len(title)):
                    if location in country[i] and category in genre[i] and ranking in rating[i]:
                        filter.append(title[i])
                        print(f"Here are your options based on the data... {filter}")
                        filter.clear()
                    continue
            elif choice == "2":
                print("Welcome to the 2nd option!!")
                time.sleep(1)
                print("Let's start the process!")
                time.sleep(1)
                print("What type do you want?: Movie or TV shows")
                time.sleep(1)
                for i in range(len(title)):
                    if variety == "Movie" and location in country[i]:
                        print(f"OK! You want your type to be {variety}")
                        time.sleep(1)
                        print(f"OK! You want your movie to be in {location}!")
                        print("OK! GENERATING A MOVIE...")
                        filter.append(title[i])
                        print(f"OK! Here are your options: {filter}")
                        filter.clear()
                        continue
            elif choice == "3":
                print("Welcome to the 3rd option!")
                time.sleep(1)
                print("So... You want to watch an older movie or a more recent movie ay...")
                time.sleep(1)
                print("Well.. What year do you want the movie to be released and Ill generate the movie to that year!")
                time.sleep(1)
                for i in range(len(year)):
                    if calendar == year[i]:
                        print("GENERATING A MOVIE/TV SHOW...")
                filter.append(title[i])
                print(f"OK! Here are your options: {filter}")
                filter.clear()
                continue
            elif choice == "4":
                print("Welcome to the 4th option!")
                time.sleep(1)
                print("So you want to watch a movie/tv show based on the genre! So many good genres such as actions or drama!!!")
                time.sleep(1)
                print("But it's your preference... What genre do you want to see in a movie/tv show?")
                for i in range(len(title)):
                    if category in genre[i]:
                        print(f"OK! You want your genre to be {category}")
                        time.sleep(1)
                        print("GENERATING A MOVIE/TV SHOW...")
                        filter.append(title[i])
                        print(f"OK! Here are your options: {filter}")
                        filter.clear()
                        continue
            else:
                print("I hope you got everything that you needed!")
                time.sleep(1)
                print("I hope you enjoyed your selections of movies/tv shows... or not.")
                time.sleep(1)
                print("GOODBYE.")
                break


#Main
menu("Brazil", "Movie", "1998", "Drama", "R")

