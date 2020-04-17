# make a dictionary containing three major rivers and country each river runs through
rivers = {"Amazonka": "Brazil, Colombia, Peru",
          "Don": "Russia",
          "Volga": "Russia",
          "Nile": "Egipt, Sudan, Uganda, Tanzania",
          "Mississippi": "USA"}

# use a loop to print a sentence about each river
print('\n')
for river, country in rivers.items():
    print(f"The {river} runs through {country}")

# use a loop to print the name of each river included in the dictionary
print("\n")
for river in rivers.keys():
    print(f"{river}")

# use a loop to print the name of each country included in the dictionary
print("\n")
for country in rivers.values():
    print(f"{country}")

