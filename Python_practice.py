print ("Hello World")
counties = ["Arapahoe","Denver","Jeferson"]
counties
if "elpasso" in counties:
    print("El Paso is in the list of counties.")
else:
    print ("El Paso is not in the list of counties.")

counties_dict ={"Arapahoe": 422829, "Denver": 463353,"jefferson":432438}

for county in counties_dict:
    print (county)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county}  county has {voters}  registered voters.")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    