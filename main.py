import requests

response  = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

response.raise_for_status() # If the status code is in the 4xx or 5xx range (indicating an error), 
                            # it raises an HTTPError exception,
                            # which you can catch and handle using a try/except block 

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)