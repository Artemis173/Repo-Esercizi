#Edwin
print ("Hello World")

# Use a variable to represent a person's name, 
# and print a message to that person. 
# Your message should be simple , such as, 
# "Hello Eric, would youl like to learn some python today?"
#
name: str = "Archer"

print (f"Ciao {name} ti va di imparre un po di Python insieme?")

# Use a variable to represent a person's name, 
# and then print that name person's in lowercase, uppercase, and title case

name: str = "Archer"

print (f"Ciao {name.lower()}")
print (f"Ciao {name.upper()}")
print (f"Ciao {name.title()}")

# Find a qoute from a famous person you admire. Point the qoute and the name of its author
# Your output should look a something like the following,
# includin the question mark: Alber Einstein once said, "Aperson who never made a mistake never tried anything new."

name: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""
name: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""

print (f"{name} once said, {message}")
print (f"{name} once said, {message}")

# Repeat exercise 2.5, but this time, rerpresent the fammous person's name using a variable called famous_person.
# The compose your message and represent it with a new variable called message
# Print your message

famous_person: str = "Gilgamesh"
message: str = "\"Hero of justice? A world where no one is hurt? Don't be absurd. Humanity is the name for an animal that cannot find joy in life without sacrifice\""

print (f"{famous_person} once said, {message}")

# Python has a removesuffix() method tht works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do

filename: str = "python_notes.txt"

print (f"Nome del file senza suffisso, {filename.removesuffix('.txt')}")

# Store the name of few of you friends in a list called names.
# Print each person's name by accessing each element in the list, one at a time.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
index = ["0", "1", "2", "3"]

print (names [0])
print (names [1])
print (names [2])
print (names [3])

# Start with the list you used in Exercise 3-1, but instead of just printing each person's name,
# print them a message to them. The text of each message should be the same,
# but each message should be personalized with the person's name.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Salve {first_name}")
print (f"Salve {second_name}")
print (f"Salve {third_name}")
print (f"Salve {fourth_name}")

# Think of your favorite mode of transportation, such as motorcycle or a car, and maake a list that stores several examples.
# Use your list to print a series of statement about these items, such as "I would like to own a honda Motorcycle"

veicoles = ["Motorcycle", "Car", "Byclycle", "Scooter"]
first_veicole = veicoles [0]
second_veicole = veicoles [1]
third_veicole = veicoles [2]
fourth_veicole = veicoles [3]

print (f"I would like to own a {first_veicole}")
print (f"I wouldn't like to own a {second_veicole}")
print (f"I own a {third_veicole}")
print (f"I own a {fourth_veicole}")

# If you could invite anyone, living or decesead, to dinner, who would you invite? 
# Make a list that includes at least three people you'd like to invite to dinner, Then use your list to print a message to each person invitin them to dinnes.

names = ["Archer", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")

# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list

names.remove ("Archer")
print (names)

names = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]
first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")

# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

names.insert (0, "Ushiwaka")
names.insert (3, "Leonida")
names.append ("Quetzal")

print (names)

first_name = names [0]
second_name = names [1]
third_name = names [2]
fourth_name = names [3]
fifth_name = names [4]
sixth_name = names [5]
seventh_name = names [6]

print (f"Hello {first_name}, would you like to come to dinner at my place?")
print (f"Hello {second_name}, would you like to come to dinner at my place?")
print (f"Hello {third_name}, would you like to come to dinner at my place?")
print (f"Hello {fourth_name}, would you like to come to dinner at my place?")
print (f"Hello {fifth_name}, would you like to come to dinner at my place?")
print (f"Hello {sixth_name}, would you like to come to dinner at my place?")
print (f"Hello {seventh_name}, would you like to come to dinner at my place?")

print (f"Hello {names}, would you like to come to dinner at my place? We're more than before because the table is bigger")

# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program fromWorking with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner. Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print (names)

print (f"Hello {names.pop(0)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(1)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(2)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(1)}, for some problems I cant invite more than two peolpe. Sorry!")
print (f"Hello {names.pop(2)}, for some problems I cant invite more than two peolpe. Sorry!")

print (names)

print (f"Hello {first_name}, you are still invited!")
print (f"Hello {second_name}, you are still invited!")

del names[0]
del names[0]

print (names)

# Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

Places = ["Babylon", "Camelot", "Avalon", "Eden", "Fuyuki"]
print (Places)

Places.sort()
print (Places)
Places.sort(reverse=True)
print (Places)
Places.reverse()
print (Places)
Places.reverse()
print (Places)
Places.sort()
print (Places)
Places.sort(reverse=True)
print (Places)

# Working with one of the programs from Exercises 3,
# use len() to print a message indicating the number of people you’re inviting to dinner.

names = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]

print (f"La lunghezza di {names} è: {len(names)}")

# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

names: list = ["Semiranis", "Gilgamesh", "Enkidu", "Saber"]
names.insert (len(names)//2, "Emiya")
print (names)

names.append ("Rin")
print (names)

print (f"Hello {names.pop(0)}, sorry see you another time")
print (f"Hello {names.pop(3)}, sorry see you another time")
del names[1]
del names[2]

print (names)
names.sort()
names.reverse()

# Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

First_name = {"Gilgamesh": "Gilgamesh", "Enkidu": "Enkidu", "Semiranis": "Semiranis"}
Last_name = {"Gilgamesh": "Re degli Eroi", "Enkidu": "Uruk", "Semiranis": "Queen"}
Age = {"Gilgamesh": "40", "Enkidu": "??", "Semiranis": "32"}
City = {"Gilgamesh": "Babylon", "Enkidu": "Uruk", "Semiranis": "Ur"}
 
All_Gilgamesh = First_name ["Gilgamesh"],Last_name ["Gilgamesh"], Age ["Gilgamesh"], City  ["Gilgamesh"]
print (All_Gilgamesh)
All_Enkidu = First_name ["Enkidu"], Last_name ["Enkidu"], Age ["Enkidu"], City  ["Enkidu"]
print (All_Enkidu)
All_Semiranis = First_name ["Semiranis"], Last_name ["Semiranis"], Age ["Semiranis"], City ["Semiranis"]
print (All_Semiranis)

# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. 
#`For even more fun, poll a few friends and get some actual data for your program.

Numbers = {"Gilgamesh": "Infinite", "Enkidu": "1", "Semiranis": "3", "Saber": "12", "Archer": "100"}
All_numbers = Numbers["Gilgamesh"], Numbers["Enkidu"], Numbers["Semiranis"], Numbers["Saber"], Numbers["Archer"]
print (All_numbers)

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#`Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
 # You might print the word followed by a colon and then its meaning, 
 # or print the word on one line and then print its meaning indented on a second line.
 # Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

Word_1 = {"If": "Allows for conditional execution of a statement or group of statements based on the value of an expression."}
Word_2 = {"Del": "Allows you to remove references to objects from a given namespace or container type"}
Word_3 = {"Insert": "Used to add items to the list at any specified position by the user"}
Word_4 = {"Append": "Use to add items to the end of a given list"}
Word_5 = {"Len()": "Used to return an integer value which indicates the number of items in an object"}

Lista_word: list = (Word_1, Word_2, Word_3, Word_4, Word_5)

for dizionario in Lista_word:
    for k, v in dizionario.items():
        print (f"{k}\n{v}")


# Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people,
# and store all three dictionaries in a list called people. Loop through your list of people.
# As you loop through the list, print everything you know about each person.

First_name = {"Gilgamesh": "Gilgamesh", "Enkidu": "Enkidu", "Semiranis": "Semiranis", "Saber": "Arthur", "Archer": "Emiya"}
Last_name = {"Gilgamesh": "Re degli Eroi", "Enkidu": "Uruk", "Semiranis": "Queen", "Saber": "Pendragon", "Archer": "Shirou"}
Age = {"Gilgamesh": "40", "Enkidu": "??", "Semiranis": "32", "Saber": "35", "Archer": "29"}
City = {"Gilgamesh": "Babylon", "Enkidu": "Uruk", "Semiranis": "Ur", "Saber": "Camelot", "Archer": "Fuyuki"}
 
All_Gilgamesh = First_name ["Gilgamesh"],Last_name ["Gilgamesh"], Age ["Gilgamesh"], City  ["Gilgamesh"]
All_Enkidu = First_name ["Enkidu"], Last_name ["Enkidu"], Age ["Enkidu"], City  ["Enkidu"]
All_Semiranis = First_name ["Semiranis"], Last_name ["Semiranis"], Age ["Semiranis"], City ["Semiranis"]
All_Saber = First_name["Saber"], Last_name["Saber"], Age["Saber"], City["Saber"]
All_Archer = first_name["Archer"], Last_name["Archer"], Age["Archer"], City["Archer"]

Lista_Personaggi: list = (All_Archer, All_Enkidu, All_Gilgamesh, All_Saber, All_Semiranis)

for dizionario in Lista_Personaggi:
    for k, v in dizionario.items():
        print (f"{k}\n{v}")

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include 
# the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your 
# list and as you do, print everything you know about each pet. 

pets1 = {'pet_name':'Luna','pet_kind':'cat','pet_owner':'Elisa Somari'}
pets2 = {'pet_name':'Rex','pet_kind':'dog','pet_owner':'Mirko Lattanzio'}
pets3 = {'pet_name':'Kira','pet_kind':'platypus','pet_owner':'Aiko Suzuki'}
pets4 = {'pet_name':'Pluto','pet_kind':'dog','pet_owner':'John Doe'}
pets5 = {'pet_name':'ScoobyDoo','pet_kind':'horse','pet_owner':'Marcus Rothschild'}
pets = [pets1,pets2, pets3, pets4, pets5]

for pet in pets:
    for k, v in pet.items():
        print (f"{k}\n{v}")

# Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
# and store one to three favorite places for each person. To make this exercise a bit more interesting, 
# ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name 
# and their favorite places.

Places = {'Marco':['Babylon','Fuyuki'],'Saber':['Fuyuki','London'],'Enkidu':'Uruk'}

for info in Places.items():
    print(f"{k}'s favorite places are: {v}")

# Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

for info in Numbers.items():
    print(f"Here are the names of your friends and their favorite numbers: ")

for info in Numbers.items():
    print(f"{k[0]}: {k[1]}")
    
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.
cities = {'Rome':{'country':'Italy','population':'2.8 million','fact':'Home of the Colosseum'},
        'Los Angeles':{'country':'California, U.S.A','population':'3.8 million','fact':'Hollywood\'s HQ'},
        'Singapore':{'country':'Singapore','population':'5.6 million','fact':'One of the world\'s greenest cities'}
    }

for city in cities.items():
    print(f"{city[0]} is a city located in {city[1]['country']}",
          f"with a population of {city[1]['population']} people",
          f"and it is {city[1]['fact']}")


# Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
# Use one of the example programs from this chapter, and extend it by adding new keys and values, 
# changing the context of the program, or improving the formatting of the output.

for info in Numbers.items():
    info[1].append(8086)

print(f"Your friends added a new favorite number: ")

for info in Numbers.items():
    print(f"{info[0]}: {info[1]}")