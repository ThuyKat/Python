# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
damages_adjust = []
for each in damages:
  if each[-1] in conversion.keys():
    new_each = each[:-1] + str(conversion[each[-1]])
    damages_adjust.append(new_each)
  else:
    damages_adjust.append(each)
print(damages_adjust)

# 2 
# Create a Table

dict_main = {}
for i in range(0,34):
  
  dict_main[names[i]] = {}
  dict_main[names[i]]["Name"] = names[i]

  dict_main[names[i]]["Month"] = months[i]
  dict_main[names[i]]["Year"] = years[i]
  dict_main[names[i]]["Max Sustained Wind"]= max_sustained_winds[i]
  dict_main[names[i]]["Areas Affected"]= areas_affected[i]
  dict_main[names[i]]["Damage"]= damages_adjust[i]
  dict_main[names[i]]["Deaths"]= deaths[i]
  
# Create and view the hurricanes dictionary

print (dict_main)
# 3
# Organizing by Year
updated_years = []
for each in years:
  if each not in updated_years:
    updated_years.append(each)
print(updated_years)
# create a new dictionary of hurricanes with year and key
target_dict = {}
for each in updated_years:
  target_dict[each] = []
  for value in dict_main.values():
    if value["Year"] == each:
      target_dict[each].append(value)
    else:
      pass
print(target_dict)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
count_dict = {}
for each_list in areas_affected:
  for each_item in each_list:
    if each_item in count_dict.keys():
      count_dict[each_item] +=1
    else:
      count_dict[each_item] = 1
print(count_dict)

# 5 
# Calculating Maximum Hurricane Count
max_area = 'Central America'
max_area_count = 0
# find most frequently affected area and the number of hurricanes involved in
for k, v in count_dict.items():
  if v > max_area_count:
    max_area = k
    max_area_count = v
print(max_area, max_area_count)

# 6
# Calculating the Deadliest Hurricane
max_mortality_cane = 'Cuba I'
max_mortality = 0
# find highest mortality hurricane and the number of deaths
for k,v in dict_main.items():
  if v["Deaths"] > max_mortality:
    max_mortality_cane = k
    max_mortality = v["Deaths"]
print(max_mortality_cane, max_mortality)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
mor_dict = {}
for k in range(1,6):
  mor_dict[k] = []
for k, v in dict_main.items():
  if v["Deaths"] > 10000:
    mor_dict[5].append(v)
  else:
    for i in range (0,5):
      if mortality_scale[i] < v["Deaths"] <= mortality_scale[i+1]:
        mor_dict[i+1].append(v)
print(mor_dict)

# 8 Calculating Hurricane Maximum Damage
max_damage_cane = 'Cuba I'
max_damage = 0

# find highest damage inducing hurricane and its total cost
for k, v in dict_main.items():
  if v["Damage"] == "Damages not recorded":
    pass
  elif float(v["Damage"]) > max_damage:
    max_damage = float(v["Damage"])
    max_damage_cane = k
print(max_damage_cane,max_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
dam_dict = {}
for k in range (1,6):
  dam_dict[k] = []
for k, v in dict_main.items():
  if v["Damage"] == "Damages not recorded":
    pass
  elif float(v["Damage"]) > 50000000000:
    dam_dict[5].append(v)
  else:
    for i in damage_scale.keys():
      if damage_scale[i] < float(v["Damage"]) <= damage_scale[i+1]:
        dam_dict[i+1].append(v)
print(dam_dict)

with open('file.txt', 'w', newline='\n') as file1:
    file1.write('Line 1\nLine 2\nLine 3')
    print(file1.read())

