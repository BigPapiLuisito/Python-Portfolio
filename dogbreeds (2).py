#luis
#dogbreeds.py
#Create a project that meets the requirements of the CREATE task by using dog breeds.

#initalization
import pandas as pd
import webbrowser
data = pd.read_csv("Dogs - Sheet1.csv")
name = data['Name'].tolist()
min_weight = data['Minimum Weight'].tolist()
dog_breed = data['Breed Group'].tolist()
temperament = data['Temperament'].tolist()
image = data['Image'].tolist()
bred = data['BredFor'].tolist()
tiny = []
small = []
medium = []
large = []
dog = []
weight = []
emotion = []
attribute = []
#function
def menu(size, breed, purpose):
    print("Welcome to the menu! Here are your options!")
    while True:
        print("Option 1: We will identify and weight of the dog you want!")
        print("Option 2: We will ask for the type of dog you want and identify the temperaments!")
        print("Option 3: We will ask for attributes that you want and identify whichs dogs fit with your description!")
        print("Option 4: QUIT")
        choice = input()
        if choice == "1":
            for i in range(len(min_weight)):
                if min_weight[i] <= size:
                    print(f"Perfect, here are the weights that are less than or equal to your preference of size!")
                    if size <= 10:
                        dog.append(name[i])
                        tiny.append(min_weight[i])
                        print(f"Here are your options for a dog and it weight! Here are its weight {tiny} and the type of dog {dog}")
                        tiny.clear()
                        dog.clear()
                    elif size >= 11 and size < 25:
                        dog.append(name[i])
                        small.append(min_weight[i])
                        print(f"Here are your options for a dog and it weight! Here are its weight {small} and the type of dog {dog}")
                        dog.clear()
                        small.clear()
                    elif size >= 26 and size < 60:
                        dog.append(name[i])
                        medium.append(min_weight[i])
                        print(f"Here are your options for a dog and it weight! Here are its weight {medium} and the type of dog {dog}")
                        dog.clear()
                        medium.clear()
                    elif size >= 60:
                        dog.append(name[i])
                        large.append(min_weight[i])
                        print(f"Here are your options for a dog and it weight! Here are its weight {large} and the type of dog {dog}")
                        large.clear()
                        dog.clear()
            print("Thank you and return if you want to find more options!")
            continue
        elif choice == "2":
            while True:
                try:
                    for i in range(len(name)):
                        if breed in name[i]:
                            dog.append(name[i])
                            emotion.append(temperament[i])
                            print(f"Here are the {dog} feelings: {emotion}")
                            print("Here's an image of your dog.")
                            webbrowser.open(image[i])
                    print("Thank you for stopping by!")
                    break
                except:
                    print("Yikes there's we don't have that in our data... Try Again!")
                    break
            dog.clear()
            emotion.clear()
            continue
        elif choice == "3":
            for i in range(len(bred)):
                if purpose in bred[i]:
                    dog.append(name[i])
                    attribute.append(bred[i])
                    print(f"Here are the attributes: {attribute} and here's the dog: {dog}")
            print("Thank you for stopping by!")
            continue
        else:
            break


#main
menu(35, "AmericanFoxhound", "lapdog")

#source of information
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
