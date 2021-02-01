import os
from twilio.rest import Client


def send_sms():
    account_sid = os.environ['enter account sid']
    auth_token = os.environ['enter auth token']

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Hello",
        from_='number',
        to='number'
    )

    print(message.sid)
