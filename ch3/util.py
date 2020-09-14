import json

def load_english_title():
    with open("./jawiki-country.json") as f:
        for line in f:
            archive = json.loads(line)
            if archive["title"] == "イギリス":
                return archive