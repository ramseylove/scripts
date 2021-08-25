import requests
import json

id = 7868
server_url = 'https://url_to_server.com'
key = 'define_api_key'

events_get = 'flowersets_get/'
event_get = 'flowerset_get/'


payload = {'code':key}


events = requests.get(f'{msgr}{events_get}{event_id}', params=payload)

flower_sets = events.json()


for sets in flower_sets:
    flower_set_id = sets['id']
    flower_set = requests.get(f'{msgr}{event_get}{flower_set_id}', params=payload)
    flower_json = flower_set.json()
    #r_str = json.dumps(flower_json, indent=2)
    
    flower_set_card_url = flower_json['card_image']
    filename = flower_set_card_url[56:]
    
    if filename != 'no_card.jpg' or '':
        image = requests.get(flower_set_card_url)
        print(flower_set_card_url)
    
        with open(f'images/{filename}', 'wb') as f:
            f.write(image.content)
