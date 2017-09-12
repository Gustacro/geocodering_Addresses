import pandas as pd
import numpy as np
import os
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim()

database= r"E:\Geocode\programming_at_work\03_Historic_places_US_LOCAL_2_PART.csv"
df = pd.read_csv(database)
df['Address'] = df['location']+ ","+ df["city"]+","+ df["state"]
#print(df)

df["coordinates"] = df["Address"].apply(geolocator.geocode)
print(df["coordinates"])

df["latitude"]= df["coordinates"].apply(lambda x: x.latitude if x != None else None)
df["longitude"]= df["coordinates"].apply(lambda x: x.longitude if x != None else None)
print (df)
df.to_csv(r'E:\Geocode\programming_at_work\03_outfile.csv')

