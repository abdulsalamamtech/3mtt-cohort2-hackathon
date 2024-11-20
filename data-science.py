
################################################################

### Crime Information
#- https://colab.research.google.com/drive/1GK53bBYtcJJmBt8RYtBOIYeMV_-WAVXf?usp=sharing





################################################################
### Road Accident Information
#- https://colab.research.google.com/drive/1bJGcWBM_lPNuaWhXEcvUWx4Au6V3URUo?usp=sharing





################################################################
### Natural Disasters Information
#- https://colab.research.google.com/drive/1eImm0wgdNmHaWYj6axluRr58bSaJ2hVn?usp=sharing



import matplotlib.pyplot as plt

# Data without Health Force
total_affected = 75095
total_households = 16422
displaced_individuals = 18643
habitable_houses = 0.20
partially_damaged_houses = 0.21
destroyed_houses = 0.29
locations_assessed = 68
lgas_assessed = 20
crop_farming_locations = 0.88

# Pie chart: House condition
plt.figure(figsize=(10, 6))
plt.pie([habitable_houses, partially_damaged_houses, destroyed_houses], labels=['Habitable but needs repair', 'Partially damaged but needs repair', 'Destroyed'], autopct='%1.1f%%')
plt.title('House Condition')
plt.show()



print("\n\n\n\n\n")


# Data (with Health Force)
total_affected = 75095
total_households = 16422
displaced_individuals = 18643
habitable_houses = 0.20
partially_damaged_houses = 0.21
destroyed_houses = 0.29
locations_assessed = 68
lgas_assessed = 20
crop_farming_locations = 0.88

# Pie chart: House condition 
plt.figure(figsize=(10, 6))
plt.pie([habitable_houses, partially_damaged_houses, destroyed_houses], labels=['Habitable but needs repair', 'Partially damaged but needs repair', 'Destroyed'], autopct='%1.1f%%')
plt.title('House Condition (with Health Force)')
plt.show()




# Bar chart: Affected population
plt.figure(figsize=(10, 6))
plt.bar(['Total Affected', 'Displaced Individuals'], [total_affected, displaced_individuals])
plt.title('Affected Population')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()



print("\n\n\n\n\n")



# Bar chart: Affected population (with Health Force)
plt.figure(figsize=(10, 6))
plt.bar(['Total Affected', 'Displaced Individuals'], [total_affected, displaced_individuals])
plt.title('Affected Population (with Health Force)')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()



# Pie chart: Primary source of income
plt.figure(figsize=(10, 6))
plt.pie([crop_farming_locations, 1 - crop_farming_locations], labels=['Crop/Vegetable Farming', 'Other'], autopct='%1.1f%%')
plt.title('Primary Source of Income')
plt.show()




print("\n\n\n\n\n")



# Pie chart: Primary source of income (with Health Force)
plt.figure(figsize=(10, 6))
plt.pie([crop_farming_locations, 1 - crop_farming_locations], labels=['Crop/Vegetable Farming', 'Other'], autopct='%1.1f%%')
plt.title('Primary Source of Income (with Health Force)')
plt.show()



# Bar chart: Assessment details
plt.figure(figsize=(10, 6))
plt.bar(['Locations Assessed', 'LGAs Assessed', 'Households Affected'], [locations_assessed, lgas_assessed, total_households])
plt.title('Assessment Details')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()




print("\n\n\n\n\n")




# Bar chart: Assessment details (with Health Force)
plt.figure(figsize=(10, 6))
plt.bar(['Locations Assessed', 'LGAs Assessed', 'Households Affected'], [locations_assessed, lgas_assessed, total_households])
plt.title('Assessment Details (with Health Force)')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()






################################################################
### Fire Disasters Information
#- https://colab.research.google.com/drive/1GUFcTgz4JCoF-AQVqCIPfTVxNxJhWJ81?usp=sharing




import matplotlib.pyplot as plt

# Data without Health Force
people_rescued = 27
people_lost = 9
fire_incidents = 54

# Bar chart: People rescued and lost
plt.figure(figsize=(10, 6))
plt.bar(['People Rescued', 'People Lost', 'Fire Incidents'], [people_rescued, people_lost, fire_incidents])
plt.title('Fire Incidents and Rescue Efforts')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()




print("\n\n\n\n\n")




# Data with Health Force
people_rescued = 57
people_lost = 2
fire_incidents = 54

# Bar chart: People rescued and lost
plt.figure(figsize=(10, 6))
plt.bar(['People Rescued', 'People Lost', 'Fire Incidents'], [people_rescued, people_lost, fire_incidents])
plt.title('Fire Incidents and Rescue Efforts (with Health Force)')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()

# Source
#https://gazettengr.com/kano-fire-service-rescues-27-people-in-two-months/




# Data without Health Force
property_saved = 370000000
property_destroyed = 141000000

# Calculate total property value affected
total_property_affected = property_saved + property_destroyed

# Pie chart: Property saved and destroyed
plt.figure(figsize=(10, 6))
plt.pie([property_saved, property_destroyed], labels=['Property Saved', 'Property Destroyed'], autopct='%1.1f%%')
plt.title('Property Affected by Fire Incidents')
plt.show()



print("\n\n\n\n\n")



# Data with Health Force
property_saved = 740000000
property_destroyed = 71000000

# Calculate total property value affected
total_property_affected = property_saved + property_destroyed

# Pie chart: Property saved and destroyed
plt.figure(figsize=(10, 6))
plt.pie([property_saved, property_destroyed], labels=['Property Saved', 'Property Destroyed'], autopct='%1.1f%%')
plt.title('Property Affected by Fire Incidents')
plt.show()

# Source
#https://gazettengr.com/kano-fire-service-rescues-27-people-in-two-months/




# Data without Health Force
emergency_calls = 22
false_alarms = 3

# Bar chart: Emergency calls and false alarms
plt.figure(figsize=(10, 6))
plt.bar(['Emergency Calls', 'False Alarms'], [emergency_calls, false_alarms])
plt.title('Fire Service Response')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()




print("\n\n\n\n\n")




# Data with Health Force
emergency_calls = 22
false_alarms = 1

# Bar chart: Emergency calls and false alarms
plt.figure(figsize=(10, 6))
plt.bar(['Emergency Calls', 'False Alarms'], [emergency_calls, false_alarms])
plt.title('Fire Service Response')
plt.xlabel('Category')
plt.ylabel('Number')
plt.show()

# Source
#https://gazettengr.com/kano-fire-service-rescues-27-people-in-two-months/
