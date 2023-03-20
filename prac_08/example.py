"""
Pseudocode
places = empty list
get place
while place is not empty
    add place to places
    get place
if length of places >0
    display place
    longest_place = empty string
    for place in places
        if length of place > length of the longest_place
            longest_place = place
        print place,longest_place
else print I went nowhere
"""
places = []
longest_place = ""
place = input("Place: ").title()
while place != "":
    places.append(place)
    place = input("Place: ").title()
if len(places) > 0:
    print("On my holiday, I went to: ")
    for place in places:
        if len(place) > len(longest_place):
            longest_place = place
        print(place)
    print(f"The place with the longest name was {longest_place}")
else:
    print("I went nowhere :(")
