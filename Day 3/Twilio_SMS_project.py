#!/bin/python
from twilio.rest import Client

#Account Details
account_sid="AC7aa6343e8e54be5538c4b0f96f47c6e7"
auth_token="1939c91291c0cf74136ded37cf324fbe"
client=Client(account_sid,auth_token)

#Sending Message
message=client.messages.create(
    body="I will love you",
    to="+919672000167",
    from_="+17854343356")
print(message.sid)


