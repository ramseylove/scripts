from collections import namedtuple
import random


first_name = [ 'James', 'John', 'Robert', 'Micheal', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbra', 'Susan', 'Jessica', 'Sarah', 'Karen' ]

last_name = [ 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Meyer', 'Valentine', 'Nichols' ]

street_name = ['Park Ave', 'Main Ave', 'Sixth St', 'Oak Ln', 'Pine St', 'Maple Ave', 'Cedar Rd', 'Elm Ave', 'Washington St', 'Lake st', 'Hill rd', 'Lincoln Blvd', 'Lake View', 'Golf Resort rd', '9th St', 'Dogwood ave', 'Magnolia Ave', 'Second Ave']

#csz_tuple = namedtuple('csz', ['city', 'state', 'zip'])
city_state_zip = [ ['Springfield', 'MA', '1101'], ['Washington', 'FL', '32427'], ['Franklin', 'AL', '36083'], ['Lebanon', 'Ks', '66952'], 
    ['Clinton', 'WA', '98236'], ['Greenville', 'UT', '84731'], ['Bristol', 'IA', '50611'], ['Fairview', 'NC', '28730'], 
    ['Salem', 'OR', '97301'], ['Madison', 'TN', '37116'], ['Georgetown', 'NY', '13072'], ['Arlington', 'IL', '61312'], 
    ['Ashland', 'NJ', '8003'], ['Dover', 'OH', '44622'], ['Oxford', 'CA', '93030'], ['Jackson', 'WY', '83002'], ['Burlington', 'WV', '26710'], 
    ['Manchester', 'MN', '56007'], ['Milton', 'WI', '53563'], ['Newport', 'AK', '72112'] ]


while count >= 0:
    rand_first = random.choice(first_name)
    rand_last = random.choice(last_name)
    rand_street = random.choice(street_name)
    rand_num = random.randint(100, 9999)
    rand_csz = random.choice(city_state_zip)

    full = f'''
    {rand_first} {rand_last}
    {rand_num} {rand_street}
    {rand_csz[0]}, {rand_csz[1]} {rand_csz[2]}
    '''
    print(full)
    count -= 1





