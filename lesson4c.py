# A python for loop can also be used to iterate throuh a list, tuple, string or even a dictionary..

name = "Moses"

for letter in name:
    if letter == "m":
        print("the letter is m")
    else:
        print(letter)

print("===========================")
# Below is a list of counties.
counties = ["Nairobi", "Mombasa", "Kisumu", "Kajiado"]

print(counties)

for county in counties:
    print(county)
    if county == "Kisumu":
        print("Not Found Kisumu")

print("===========================")
for county in counties:
    if county == "Nairobi":
        print("Found Nairobi")

# The for loop can also be used to iterate through a dictionary.

player = {
    "name": "Mbappe",
    "age": "29",
    "teams": ["PSG","Monaco","France"],
    "nationality": "French"
}

for key in player:
    print (key)
print("===========================")
for values in player:
    print(player[values])
# print(player["name"])


print('==========================')
# loop throughout the teams the player has played for
#print(player["teams"])

for team in player["teams"]:
    print(team)
  


