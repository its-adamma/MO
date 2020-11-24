from twilio.rest import Client

# Confirmation SMS to physicians detailing mask quantity and ETA

account_sid = "ACCOUNT SID"

auth_token  = "AUTH TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="NUMBER", 
    from_="NUMBER",
    body="Hi, Adamma. Your request for 2,000 masks is on it's way! Mask Oakland Volunteer Dennis will arrive outside the main entrance at approx. 2:30p.")

print(message.sid)