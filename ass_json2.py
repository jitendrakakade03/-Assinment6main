import json
Dictionary = {
    "Tamilnadu" : "Chennai",
    "Kerala" : "Thiruvnanthapuram",
    "Karnataka" : "Bangaluru",
    "Telangana" : "Hyderabad",
    "Goa" : "Panaji",
    "Uttarpradesh" : "Lucknow",
    "Maharastra" : "Mumbai"
}
print(Dictionary)
with open("state_capital.json","w") as f:
    json.dump(Dictionary,f)
