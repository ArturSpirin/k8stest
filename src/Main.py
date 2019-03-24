import requests

message = "Hello world!"
hook = "559162162677809162/lnw015w8c-tM2bHL1dSfeGavQB6dA3a7d0gi8RuWAICGmqOGxK5E3Evbrtdkeg5rrGeA"  # replace w/ ur hook
response = requests.post("https://discordapp.com/api/webhooks/{hook}".format(hook=hook),
                         json={"content": message})
