from fbchat import Client

from fbchat.models import Message
#facebook user credentials
username = "mishras2871998@gmail.com"
password = "9990744107"
#login
client = Client(username, password)

#logout
client.logout()
