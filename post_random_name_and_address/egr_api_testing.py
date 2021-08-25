import requests
import json

#https://mgrexpression-mgrexpression-dev.azurewebsites.net/assets/uploads/flower_images/86B5F65D-59AC-45EF-B7D9-C642A43383EF-7851-1567530429733-Flower_2_smallflower.jpg
#url = 'https://mgrapi-v1.azurewebsites.net/api/flowerSets_get/7804?code=2LkdNZluFaleEaVn3PW8wh9fIP1a7Sj8FJfuwejpWKUOyUziZYfipg=='

msgr = 'https://egrfa.azurewebsites.net/api/'
atria = 'https://mgrapi-v1.azurewebsites.net/api/'
events_get = 'flowersets_get/'
event_get = 'flowerset_get/'
msgr_key = 'p2OPCrGvD0ScKZQRrPJM41GG1oPInIigEV9UBeIaLm0CtB6wUpaWeQ=='
atria_key = '2LkdNZluFaleEaVn3PW8wh9fIP1a7Sj8FJfuwejpWKUOyUziZYfipg=='

payload = {'code':msgr_key}
#7804
event_id = 7868
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
