import requests
import json

r = requests.get('http://routingnumbers.herokuapp.com/api/data.json?rn=041202582')

# assert print(r) == '<Response [200]>'

# assert 'state' in json_data
print(r.json())

testString = str(r.json())

assert 'zip' in testString