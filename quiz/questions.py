# The questions are from opentdb.com

import requests

request_params = {
    'amount': 10,
    'category': 18,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=request_params)
response.raise_for_status() # this will raise exceptions if encountered, comes with 'requests'
data = response.json()
questions = data['results']
