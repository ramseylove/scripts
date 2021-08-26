import datetime as dt
import random
import requests

base_url = 'http://your.url.com'

event_id = '4706'

# currently need to define the cookie found in dev_tools because auth is poorly implemented
session = 'ksadjoicvoiewr32'


def create_random_entries(count=10):
  
  first_name = [ 'James', 'John', 'Robert', 'Micheal', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbra', 'Susan', 'Jessica', 'Sarah', 'Karen' ]

  last_name = [ 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Meyer', 'Valentine', 'Nichols' ]

  street_name = ['Park Ave', 'Main Ave', 'Sixth St', 'Oak Ln', 'Pine St', 'Maple Ave', 'Cedar Rd', 'Elm Ave', 'Washington St', 'Lake st', 'Hill rd', 'Lincoln Blvd', 'Lake View', 'Golf Resort rd', '9th St', 'Dogwood ave', 'Magnolia Ave', 'Second Ave']

  city_state_zip = [ ['Springfield', 'MA', '1101'], ['Washington', 'FL', '32427'], ['Franklin', 'AL', '36083'], ['Lebanon', 'Ks', '66952'], 
      ['Clinton', 'WA', '98236'], ['Greenville', 'UT', '84731'], ['Bristol', 'IA', '50611'], ['Fairview', 'NC', '28730'], 
      ['Salem', 'OR', '97301'], ['Madison', 'TN', '37116'], ['Georgetown', 'NY', '13072'], ['Arlington', 'IL', '61312'], 
      ['Ashland', 'NJ', '8003'], ['Dover', 'OH', '44622'], ['Oxford', 'CA', '93030'], ['Jackson', 'WY', '83002'], ['Burlington', 'WV', '26710'], 
      ['Manchester', 'MN', '56007'], ['Milton', 'WI', '53563'], ['Newport', 'AK', '72112'] ]


  while count >= 0:
    csz = random.choice(city_state_zip)
    person = {
      'first_name': random.choice(first_name),
      'last_name': random.choice(last_name),
      'house_num': random.randint(100, 9999),
      'street': random.choice(street_name),
      'city': csz[0],
      'state': csz[1],
      'zip': csz[2]
    }

    name_and_address = f'''
    {person['first_name']} {person['last_name']}
    {person['house_num']} {person['street']}
    {person['city']}, {person['state']} {person['zip']}
    '''
    print(name_and_address)
    count -= 1
    yield person

for item in create_random_entries():
  print(item)

def post_entry(event_id, *count):
  
  url = "base_url/api/entry"

  for person in create_random_entries(count=count):
    payload={'event_id': event_id,
    'first_name': person['first_name'],
    'last_name': person['last_name'],
    'address': person['house_num'] + person['street'],
    'city': person['city'],
    'state': person['state'],
    'zip': person['zip'],
    'email': '',
    'phone': '',
    'ipad_timestamp': str(int(dt.datetime.now().timestamp())),
    'device_id': 'D1C7A145-5AE8-4CBB-9953-5EC7145AE532',
    'app_version': '3.4'}
  
    headers = {
      'ci_session': session
    }

    response = requests.request("POST", url, headers=headers, data=payload )

    print(response.text)



