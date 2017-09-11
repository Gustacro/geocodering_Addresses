# Load packages

from pygeocoder import Geocoder
import pandas as pd
import numpy as np
import os

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
for Address in df['full_address']:
    print(Address)
    address_validation = Geocoder.geocode(Address).valid_address

# view if address is valid
    print(address_validation)

# save the address into a a new variable
    result_address = Geocoder.geocode(Address)

# print coordinates for the address given.
    print(result_address.coordinates)