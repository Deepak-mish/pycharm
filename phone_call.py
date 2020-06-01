from twilio.rest import TwilioRestClient as call

from_Number = "+19164398375"
To_Number = "+919990744107"
src_Path = ""

client = call("AC05b247cf47771cfc0bdf1a6fd96a14e1", "7de6be67a9701cef9f4131e05b554389")

print("call initiated")
client.calls.create(to=To_Number, from_=from_Number, url=src_Path, method='GET')
print("call has been twigged successfully")
