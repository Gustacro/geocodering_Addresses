# Load packages

from pygeocoder import Geocoder
import pandas as pd
import numpy as np
import os
import csv

wrks = (r"/home/gustacro/Desktop")
database = os.path.join(wrks,"02_Historic_places_US.csv")
df = pd.read_csv(database)
df['Address'] = df['full_address']

# for Address in df['full_address']:
    #print(Address)

# # Inputs
# address = "228 RICHMOND ST, philadelphia"
#
# view Address that we are going to get the latitude and longitude
# print(address)
# Verify that an address is valid (i.e. in Google's system)

with open('outfile.csv', 'w') as newfile:
    wr = csv.writer(newfile, quoting=csv.QUOTE_ALL)
    for index, row in df.iterrows():
        objectid = row['c1']
        loc = row['c2']
        city = row['c3']
        state = row['c4']
        full_address = row['c5']
        
        address_validation = Geocoder.geocode(full_address).valid_address
        
        # view if address is valid
        print(address_validation)
    
        # save the address into a a new variable
        result_address = Geocoder.geocode(full_address)
        lat = result_address.coordinates[0]
        lng = result_address.coordinates[1]
    
        # print coordinates for the address given.
        print(result_address.coordinates)
        final_list = [lat, lng, full_address]
        print(final_list)
        wr.writerow(final_list)
