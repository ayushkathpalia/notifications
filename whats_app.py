from twilio.rest import Client

account_sid = 'enter account sid'
auth_token = 'enter auth token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='number',
    body="Hello Saurabh. This is your bot: JARVIS, reporting on duty!",
    to='number'
)

print(message.sid)
