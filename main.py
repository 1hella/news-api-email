from send_email import send_email

import requests

api_key = "cc378c31bde441f799a822ff3fe7e1ac"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-01-17&sortBy=publishedAt&apiKey" \
      f"={api_key}"

request = requests.get(url)
content = request.json()

message = ""

for article in content["articles"]:
    message += "\n" + article['title']
    message += "\n" + article['description']
    message += "\n"

message = message.encode(encoding="utf8")
send_email(message)
