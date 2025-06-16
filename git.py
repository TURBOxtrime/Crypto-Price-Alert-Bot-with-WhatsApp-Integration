import requests
from requests import Session
import json
from twilio.rest import Client

#twilio content
account_sid="YOUR TWILIO SID"
auth_token="AUTH_TOKEN"
generated_number='whatsapp:+NUMBER_GENRATED BY TWILIO'
whatsapp_number='whatsapp:+YOUR WHATSAPP NUMBER'

#crypto data
crypto_api="YOUR CRYPTO API"
crypto_url = 'CRYPTO URL'
message=""

#sheety
sheety_endpoint="sheety endpoint"
data=requests.get(sheety_endpoint)
values_json=data.json()
value=[]
currunt_prises={}
to_compair={}

for i in range(len(values_json["sheet1"])):
    x=values_json["sheet1"][i]["name"]
    value.append(x)
    to_compair[x] = {
    "lowest": f"{float(values_json['sheet1'][i]['lowest']):.12f}",
    "higest": f"{float(values_json['sheet1'][i]['higest']):.12f}"
    }

coins=",".join(value)


#coin value api

parameters = {
  'symbol':coins,
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': crypto_api,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(crypto_url, params=parameters)
  data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#get the current price
for i in value:
    valuee=data["data"][i]["quote"]["USD"]["price"]
    valuee=f"{valuee:.12f}"
    currunt_prises[i]=valuee

#compairison and message writing
for i in value:
   if float(currunt_prises[i])>float(to_compair[i]["lowest"]):
      message+=f"{i} is ready to sell, current price is {float(currunt_prises[i])}.\n"
   elif float(currunt_prises[i])<float(to_compair[i]["higest"]):
    message+=f"{i} is ready to purchase, current price is {float(currunt_prises[i])}.\n" 


# send whatsapp message
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=message,
    from_=generated_number,  # Twilio sandbox number
    to=whatsapp_number  # Replace with your verified WhatsApp number
)

print("Message SID:", message.sid)