import requests
import json
import polyline
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def decode_polyline(polyline_str):
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {'latitude': 0, 'longitude': 0}
    
    while index < len(polyline_str):
        for unit in ['latitude', 'longitude']:
            shift, result = 0, 0
            
            while True:
                byte = ord(polyline_str[index]) - 63
                index += 1
                result |= (byte & 0x1f) << shift
                shift += 5
                if not byte >= 0x20:
                    break
            
            if result & 1:
                changes[unit] = ~(result >> 1)
            else:
                changes[unit] = result >> 1
        
        lat += changes['latitude']
        lng += changes['longitude']
        
        coordinates.append([lat / 1e5, lng / 1e5])
    
    return coordinates

origin = "48.516707,29.211951"
destination = "48.195792,35.806096"  

url = "https://maps.googleapis.com/maps/api/directions/json"
params = {
    "origin": origin,
    "destination": destination,
    "key": GOOGLE_API_KEY,
    "mode": "driving",
    "alternatives": "false" 
}

response = requests.get(url, params=params)
data = response.json()

response = requests.get(url, params=params)
data = response.json()

if data["status"] == "OK":
    route = data["routes"][0]
    all_coords = []
    
    for leg in route["legs"]:
        for step in leg["steps"]:
            step_polyline = step["polyline"]["points"]
            step_coords = polyline.decode(step_polyline)
            all_coords.extend(step_coords)
    
    with open('route.json', 'w') as f:
        json.dump(all_coords, f, indent=2)
    
    print(f"✅ Saved {len(all_coords)} points")