import csv

data = []

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

planet_data_Rows = data[1:]
# print(planet_data_Rows)

planet_mass = []
planet_radius = []
planet_names = []

for planet_data in planet_data_Rows:
    print(planet_data[3][3])
# print(planet_mass)