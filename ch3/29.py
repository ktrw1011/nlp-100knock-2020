import requests

# 国旗画像はFlag of the United Kingdom.svgで与えられることが分かっている
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Flag of the United Kingdom.svg",
    "iiprop": "url",
}

res = requests.get(
    url="https://en.wikipedia.org/w/api.php",
    params=PARAMS
)

response_json = res.json()
print(f'[Flag of the United Kingdom.svg] url: {response_json["query"]["pages"].popitem()[1]["imageinfo"][0]["url"]}')