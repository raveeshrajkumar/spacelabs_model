## Importing Packages
import requests
import json

##Endpoint for the FASTAPI application
url = "http://127.0.0.1:8000/predict"

##Headers for the HTTP Request
headers = {
    
    'accept': 'application/json',
 
}

##Parameters for the POST request payload
params = {
  "apogee": -1000,
  "perigee": 2034,
  "incl": 3452,
  "arg_perigee": -1000,
  "raan": 2345
}

##Send a POST request to the FastAPI endpoint
response = requests.post(url,headers = headers, data = json.dumps(params))

##Print the response 
print("===============")

print(response.json())