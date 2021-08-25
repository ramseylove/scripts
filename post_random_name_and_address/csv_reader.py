import csv
import random

with open('first_name.csv', 'r', encoding='utf-8-sig') as entry_file:
    first_name = csv.reader(entry_file)

with open('last_name.csv', 'r', encoding='utf-8-sig') as entry_file:
    last_name = csv.reader(entry_file)

with open('street_name.csv', 'r', encoding='utf-8-sig') as entry_file:
    street_name = csv.reader(entry_file)

with open('city_state_zip.csv', 'r', encoding='utf-8-sig') as entry_file:
    city_st_zip_dict = csv.reader(entry_file)
    
    for line in city_st_zip_dict:
        print(line)
    
    



#names_dict['First Names']
#names_dict['Last Names']
#names_dict['Street names']


