dict = {
    "usa": "washington",
    "britannia": "london",
    "russia": "moscow",
    "kazakhstan": "astana",
    "china": "beijing"
}

for keys, values in dict.items():
    print(keys.upper() + ": " + values.capitalize())