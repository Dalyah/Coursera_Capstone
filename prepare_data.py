# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:37:37 2020

@author: Daliyah.Aljamal
"""
import numpy as np 
import pandas as pd
import json

#STEP 1: Read KSA districts data
data = pd.read_json('data/districts.json')
print(len(data['boundaries'][10][0]))

# STEP 2: Filter data to include only riyadh data (city_id=3, region_id=1)
riyadh_data = data[data['region_id'] == 1]
riyadh_data = riyadh_data[riyadh_data['city_id'] == 3]

# STEP 3: select the center boundary for each district
lat_list = []
lng_list = []
for boundaries in riyadh_data['boundaries']:
    lat = []
    lng = []
    for boundary in boundaries[0]:
        lat.append(boundary[0])
        lng.append(boundary[1])
    lat = np.array(lat)
    lng = np.array(lng)
    center_lat = np.median(lat)
    center_lng = np.median(lng)
    #print(center_lat, center_lng)
    lat_list.append(center_lat)
    lng_list.append(center_lng)

# Step 4: Drop unneeded columns
riyadh_data.drop(['boundaries', 'city_id','region_id', 'district_id','name_ar'],
                 axis=1, inplace=True)

# Step 5:  Add latitude and longitude columns
riyadh_data['latitude'] = lat_list
riyadh_data['longitude'] = lng_list

# Step 6: rename columns
riyadh_data.rename(columns = {'name_en' : 'district'}, inplace = True)

print(riyadh_data.head())
print(riyadh_data.shape)
riyadh_data.to_csv('data/riyadh_districts.csv')
