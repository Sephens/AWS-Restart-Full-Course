import json
filename = "car_fleet.json"
data = ""

try:
    with open(filename, 'r') as file:
        data = json.load(filename)
        print(data)
except:
    print("error! Cannot read the file")
