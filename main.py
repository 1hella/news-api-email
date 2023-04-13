from send_email import send_email
import datetime
import requests
now = datetime.date.today()
date_to_request = now - datetime.timedelta(days=1)

topic = "tesla"
api_key = "cc378c31bde441f799a822ff3fe7e1ac"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      f"&from={date_to_request}" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}" \
      "&language=en"

request = requests.get(url)
content = request.json()
print(content)
message = "Subject: Today's news"

for article in content["articles"][:20]:
    message += "\n" + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2 * "\n"


message = message.encode(encoding="utf8")
send_email(message)
