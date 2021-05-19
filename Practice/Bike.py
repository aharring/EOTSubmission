# Using JCDecaux CSV for Dublin bike data
# Regex to separate long/lat field in to two columns
# List sample 10 addresses from 5500 row file
# Calculate distance from picked address and list the 10 closest open bike centres
# Using re, pandas, mpu and numpy
# 
# Very basic - no error checks, goal was to check out pandas a little and play with regex again
# Teamwork with my brother just stepping through a project with him
# 
import pandas as pd
import re               # RegEx used to extract Lat & Long
import mpu		# Used to calculate distance between two points
import numpy as np

def displayMenu():
    print("\nWelcome - What would you like to do?\n")
    print("\t(f) Find nearest bike station?")
    print("\t(v) View map of available stations")
    print("\t(q) Quit\n")
    choice = input("Type one letter (f/v/q):").strip()
    return choice

# Read in the data frame. Manipulate to extract long/lat/Time - Assumes duplicate addresses & attempts to remove

#bikeData = pd.read_csv("BDD.csv") 	# Read in the Bike Data. Assumption currently is the file exists & is in the same dir.
bikeData = pd.read_csv("BikeApiCombined.csv")
bikeData.drop_duplicates(subset="name", keep = 'first', inplace = True) # Dropping duplicates here - may need a copy of DF for other calculations
print(bikeData)

bikeData['lat'] = bikeData.position.str.extract(r':(.*?),', expand=True)           # Split out lattitude. Append it to dataframe
bikeData['lng'] = bikeData.position.str.extract(r'lng\':(.*?)}', expand=True)      # Split out longitude. Append it to dataframe
bikeData['distance'] = 0.0                                                         # Add the distance column to the DF & initialise to float
bikeData.sort_values(by=['status','name'], inplace = True, ascending = [False, True]) # Sort the data alphabetically within Open, Closed
bikeData.reset_index(drop=True, inplace = True)                                    # Reorder the index

# Add processing for the time maniuplation

# This function assumes you are at a current bike station and you want to find the nearest 5 
# It only displays the first 5 locations from the dataframe for you to choose the location from
# This is just for visual purposes - in reality if you had a fully coded app
# The input search would start auto completing the address you were typing in 

def doFindNearestBike(bikeData):

    print("\n"+bikeData['name'][:10].to_string()+"\n")  # print the first 10 addresses (name) only
    index = int(input("\nPlease enter starting station number (0-9): ").strip())
    if index >= 0 and index <= 9 :
        bikeData['lng'] = bikeData.lng.astype(float)                               # Explicitly cast lng as float, not object
        bikeData['lat'] = bikeData.lat.astype(float)                               # Explicitly cast lat as float, not object
        startingCoords = (bikeData['lat'][index], bikeData['lng'][index])
        for i in range (len(bikeData)) :                                           # for i in len(bikeData) to loop over entire DF
            #bikeData['distance'][i] = mpu.haversine_distance(startingCoords, (bikeData['lat'][i], bikeData['lng'][i]))
            bikeData.loc[i,'distance'] = mpu.haversine_distance(startingCoords, (bikeData['lat'][i], bikeData['lng'][i]))
        # print (bikeData['distance'])  Just to verify distance is set
    s1 = bikeData['status']
    s2 = bikeData['distance']                                                       
    s3 = ~bikeData['available_bikes']>0                                            

    results = bikeData.iloc[np.lexsort((s3,s2,s1))]
    results = results[results['distance'] !=0]                                     # Remove the source station with distance 0
    results = results[results['status'] != 'CLOSED']                               # Remove closed stations 
    # For the purpose of example only 10 stations are listed to choose for the starting point
    # But the results will be the 10 closest out of the 100 or so stations
    
    print("\nThe Nearest 10 Open stations with bikes available\n\nDistance Status\tAvailable\t\tStation Name\n")
    print(results[['distance', 'status', 'available_bikes', 'name']].head(10).to_string(index=False, header=False))

def doDisplayMap():
    print("In doDisplayMap")

# Simple menu to demonstrate user input & processing
choice = displayMenu()
while(choice != 'q'):
    if choice == 'f':
       doFindNearestBike(bikeData) 
    elif choice == 'v':
       doDisplayMap()
    elif choice !='q':
       print("\n\nplease select either f,v or q")
    choice=displayMenu() 
